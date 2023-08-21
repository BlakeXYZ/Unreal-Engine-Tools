from unittest.mock import Base
import unreal

import sys, os
from typing import List  # Import the List type from the typing module

# allow for import of custom python scripts
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)  



#       USER REQUIREMENTS
#           Make a MATERIAL EXPRESSION GROUP name & Apply to all textures you wish to often replace
#           Proper Naming Convention for Imported Textures ('_BC, _N, _ORM' etc.)
# 
#       VALIDATION CODE
#           Before  Importing Images
#           and Connecting Images into Material Instance...
#
#       - ENSURE only Texture2d File Formats are Selectable in File Dialog                      ☒ - material_instancer.py > my_QFileDialog_filter
#       - CHECK if single selected Content Browser Asset                                        ☒ - def get_single_selected_content_browser_material()
#       - FILTER all Material Nodes with Mat Expression GROUP (class TexParamInfo)              ☒
#       - COMPARE Master Mat Tex Params COUNT            == stored_fileNames COUNT              ☐
#       - COMPARE Master Mat Tex Params NAMES suffix     == stored_fileNames suffix             ☐


#   IF CHECKS PASS continue to...
#
#       - Import Files
#       - get_recently_imported_assets
#       - Build Material Instance of Selected Master Material
#       - Slot in imported_assets (Texture2d) into Material Instance



# Advantage of get + storing all Tex Params using "MATERIAL EXPRESSION GROUP name" VS. "get_texture_parameter_names"
#
#   get_texture_parameter_names relies restricts user (example: find all '_Normal' maps, may include more than one in Material Node Network)
#                                                     Forces user to name all Texture2dParams, prone to user error.
#
#   MATERIAL EXPRESSION GROUP name is more flexible, do not need to name each Texture2dParams, only need to find Params with Group then store Param's Texture's Suffix



stored_fileNames = [rf'C:/Users/blake/Pictures/Wallpaper/a.jpg',]

class ValidationError(Exception):
    pass

# filters out selection to a single asset of <class Material>
def get_single_selected_material() -> List[unreal.Material]:

    editor_utility = unreal.EditorUtilityLibrary()
    selected_assets = editor_utility.get_selected_assets()

    stored_single_material = []

    # CHECK if number of selected assets is ONE
    if len(selected_assets) != 1:
        raise ValidationError(f'Please select only 1 Master Material in Content Browser')

    
    selected_asset = selected_assets[0]
    # CHECK if selected asset is instance of <class Material>
    if not isinstance(selected_asset, unreal.Material):
        unreal.log_error(f'Please select Asset of <class "Material">')
        raise ValidationError(f'Currently Selected Asset "{selected_asset.get_name()}" is a {type(selected_asset)}')


# IF CHECKS PASS then append asset to 'stored_single_material'
    unreal.log(f'Master Material: "{selected_asset.get_name()}" selected!')
    stored_single_material.append(selected_asset)

    return stored_single_material


def get_selected_material_tex_params():

    try:
        stored_master_material = get_single_selected_material()
        success = True  # Flag to track success
    except ValidationError as e:
        unreal.log_error(str(e))
        success = False  # Flag indicating failure

    # Continue only if 'single_selected_material' is VALID
    if success:
        stored_master_material = stored_master_material[0]


        



class TexParamData:
    def __init__(self, material_path, user_defined_paramGroup=None):

        self.material_path = material_path
        self.user_defined_paramGroup = user_defined_paramGroup

        self.LIST_textures_in_user_defined_paramGroup = []
        self.LIST_all_paramGroups = []

    def walk_material_node_system(self):
        # Load your material asset
        my_material_asset = unreal.load_asset(self.material_path)

        # Store all MaterialProperty methods (Base Color, Normal, Roughness, etc.)
        material_property_list = [method for method in dir(unreal.MaterialProperty) if method.startswith("MP_")]

        for material_property in material_property_list:
            # print(f'Walking {material_property}...')
            # Search inside MY_MATERIAL_ASSET and locate INPUT NODE for each Material Property
            my_material_expression = unreal.MaterialEditingLibrary.get_material_property_input_node(
                my_material_asset, getattr(unreal.MaterialProperty, material_property))

            if my_material_expression is None:
                continue

            # Start the recursive traversal
            self.recursively_walk_input_nodes(my_material_asset, my_material_expression)

    def recursively_walk_input_nodes(self, material_asset, material_expression):
        # Get the inputs for the current material expression
        input_nodes = unreal.MaterialEditingLibrary.get_inputs_for_material_expression(material_asset, material_expression)

        # Iterate through the all of the Selected Material's input nodes
        for input_node in input_nodes:
            if input_node is None:
                continue
            
            # if node inside Material is Texture2d Input Node (TextureSampleParameter2d) 
            if isinstance(input_node, unreal.MaterialExpressionTextureSampleParameter2D):

                # Storing Textures ONLY inside user defined Parameter Group
                if input_node.get_editor_property("group") == self.user_defined_paramGroup:
                    if input_node not in self.LIST_textures_in_user_defined_paramGroup:
                        self.LIST_textures_in_user_defined_paramGroup.append(input_node)

                # Storing all Texture Parameter Groups inside a List
                if input_node.get_editor_property("group") not in self.LIST_all_paramGroups:
                    self.LIST_all_paramGroups.append(input_node.get_editor_property("group"))

            # Recursively call the function for the child node
            self.recursively_walk_input_nodes(material_asset, input_node)

    def get_texture_group_in_tex_param_list(self):
        for tex_param in self.LIST_textures_in_user_defined_paramGroup:
            print('========================================')
            print(tex_param)
            try:
                print(f'Texture Parameter group name --             {tex_param.get_editor_property("group")}')
                print(f'Texture Parameter name --                   {tex_param.get_editor_property("parameter_name")}')
                print(f'Texture Parameter file --                   {tex_param.get_editor_property("texture")}')
            except:
                pass

    def execute(self):
        self.walk_material_node_system()
        self.get_texture_group_in_tex_param_list()

    def return_LIST_textures_in_user_defined_paramGroup(self):
        self.walk_material_node_system()
        return self.LIST_textures_in_user_defined_paramGroup

    def return_LIST_all_paramGroups(self):
        self.walk_material_node_system()
        return self.LIST_all_paramGroups

'''
Logic steps


Select Master Material

Run Class to find and list Parameter Groups

Store All Textures found?



User selects specific Param group 

All Stored Textures list is then iterated through, finding only Textures with User selected Param Group




'''






if __name__ == "__main__":

    material_path = "/Game/Python/Material_Instancer/NewMaterial"



    # material_path = "/Game/Python/Material_Instancer/NewMaterial"
    # mat_parameter_group = 'IMPORT_PARAMS'

    # inst_TexParamData = TexParamData(material_path)
    # LIST_textures_in_user_defined_paramGroup = inst_TexParamData.return_LIST_textures_in_user_defined_paramGroup()

    # LIST_all_paramGroups = inst_TexParamData.return_LIST_all_paramGroups()

    # print(LIST_all_paramGroups)
    # print(LIST_textures_in_user_defined_paramGroup)

    # print('LIST_all_paramGroups')
    # for paramgroup in LIST_all_paramGroups:
    #     print(paramgroup)

    # for tex_param in LIST_textures_in_user_defined_paramGroup:
    #     print('========================================')
    #     print(tex_param)
    #     try:
    #         print(f'Texture Parameter group name --             {tex_param.get_editor_property("group")}')
    #         print(f'Texture Parameter name --                   {tex_param.get_editor_property("parameter_name")}')
    #         print(f'Texture Parameter file --                   {tex_param.get_editor_property("texture")}')
    #     except:
    #         pass


    #     tex_asset = tex_param.get_editor_property("texture")

    #     if isinstance(tex_asset, unreal.Texture2D):
    #         print(f"Loaded Tex Asset in Param: {tex_asset.get_fname()}")


    #     # break #debugging 





# TODO How to find Tex Params based on Details > Material Experssion > Group?



# TODO      - COMPARE Master Mat Tex Params NAMES suffix     == stored_fileNames suffix             
# TODO      - COMPARE Master Mat Tex Params COUNT            == stored_fileNames COUNT











def import_files():

    '''
    Import Files into Project
    '''

    my_destination_path = unreal.EditorUtilityLibrary.get_current_content_browser_path()

    # create asset_tools object
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    # create asset_import_data object
    my_asset_import_data = unreal.AutomatedAssetImportData()

    # Setup Import Attributes
    my_asset_import_data.destination_path = my_destination_path
    my_asset_import_data.filenames = stored_fileNames
    my_asset_import_data.replace_existing = True


    print('Importing the following files:')
    for filename in my_asset_import_data.filenames:
        print(filename)
        asset_tools.import_assets_automated(my_asset_import_data)


# Compares ALL assets in current browser to stored_fileNames
# stores matching assets into 'stored_assets' list
##
# This is way to only select imported assets if there are multiple assets in current content browser path
def get_recently_imported_assets() -> List[unreal.Texture2D]:

    # list assets in current directory
    current_directory = unreal.EditorUtilityLibrary.get_current_content_browser_path()
    Editor_Asset_Lib = unreal.EditorAssetLibrary
    list_asset_paths = Editor_Asset_Lib.list_assets(current_directory)
    
    # initiliaze List for ASSETS in current content browser that were recently imported
    stored_assets = []

    for asset_path in list_asset_paths:

        # Load the asset to expose properties (Details Panel View in UE)
        loaded_asset = Editor_Asset_Lib.load_asset(asset_path)
        print(f'----------------- Currently Loaded Asset: {loaded_asset.get_fname()}')

        try: # Try and see if loaded_asset has 'asset_import_data'

            # Get the source file path of the asset
            asset_import_data = loaded_asset.get_editor_property('asset_import_data')
            source_filepath = asset_import_data.get_first_filename()

            # CHECK if content browser asset's source_filepath is in 'stored_fileNames'
            if source_filepath not in stored_fileNames:
                unreal.log_warning(f'{loaded_asset.get_fname()} is NOT in "stored_fileNames"')
                continue

            # CHECK if loaded asset is Texture2D
            if not isinstance(loaded_asset, unreal.Texture2D):
                unreal.log_warning(f'{loaded_asset.get_fname()} is NOT instance of "unreal.Texture2D"')
                continue

        # IF CHECKS PASS: append 'loaded_asset' to list named 'stored_assets'
            print(f'{loaded_asset.get_fname()} appended to "stored_assets" list')
            stored_assets.append(loaded_asset)

        except AttributeError: # not all assets have asset import data
            unreal.log_warning(f'{loaded_asset.get_fname()} DOES NOT CONTAIN editor property: "asset_import_data"')
            pass

    return stored_assets




# def get_tex_param_names(material_path):
        
#         my_material_asset = unreal.load_asset(material_path)
#         list_of_tex2d_params = unreal.MaterialEditingLibrary.get_texture_parameter_names(my_material_asset)
#         for param in list_of_tex2d_params: print(f'name of param: {param}') # Prints out:        "NAME OF PARAMETER: Base_Color_Param"



