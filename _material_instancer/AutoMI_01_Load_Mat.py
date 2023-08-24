import unreal

import sys, os
from typing import List  # Import the List type from the typing module

# allow for import of custom python scripts
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)  

class ValidationError(Exception):
    pass



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
        raise ValidationError(f'Please select Asset of <class "Material"> -- Currently Selected Asset "{selected_asset.get_name()}" is of {type(selected_asset)}')


# IF CHECKS PASS then append asset to 'stored_single_material'
    unreal.log(f'Master Material: "{selected_asset.get_name()}" selected!')
    stored_single_material.append(selected_asset)

    return stored_single_material[0]


class TexParamData:
    def __init__(self, material_path):

        self.material_path = material_path

        self.LIST_all_matExpressions = []
        self.LIST_all_matExpression_paramGroups = []

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

            ###########
            ###########
            ##### This check is purely for immediate nodes connected to each Material Property
            ##### using get_material_property_node
            ##### Once we go in recursively_walk_input_nodes, we then check inside get_inputs_for_material_expression
            # if node inside Material is Texture2d Input Node (TextureSampleParameter2d) 
            if isinstance(my_material_expression, unreal.MaterialExpressionTextureSampleParameter2D):

                # Storing Textures ONLY inside user defined Parameter Group
                if my_material_expression not in self.LIST_all_matExpressions:
                    self.LIST_all_matExpressions.append(my_material_expression)

                # Storing all Texture Parameter Groups inside a List
                if my_material_expression.get_editor_property("group") not in self.LIST_all_matExpression_paramGroups:
                    self.LIST_all_matExpression_paramGroups.append(my_material_expression.get_editor_property("group"))
            ###########
            ###########



            # Start the recursive traversal
            self.recursively_walk_input_nodes(my_material_asset, my_material_expression)

    def recursively_walk_input_nodes(self, material_asset, material_expression):
        # Get the inputs for the current material expression
        input_nodes = unreal.MaterialEditingLibrary.get_inputs_for_material_expression(material_asset, material_expression)

        # Iterate through the all of the Selected Material's input nodes
        for input_node in input_nodes:
            if input_node is None:
                continue
            
            ###########
            ###########
            # if node inside Material is Texture2d Input Node (TextureSampleParameter2d) 
            if isinstance(input_node, unreal.MaterialExpressionTextureSampleParameter2D):

                # Storing all Textures in Material
                if input_node not in self.LIST_all_matExpressions:
                    self.LIST_all_matExpressions.append(input_node)

                # Storing all Texture Parameter Groups as string
                if input_node.get_editor_property("group") not in self.LIST_all_matExpression_paramGroups:
                    paramGroup_name = str(input_node.get_editor_property("group"))
                    self.LIST_all_matExpression_paramGroups.append(paramGroup_name)
            ###########
            ###########

            # Recursively call the function for the child node
            self.recursively_walk_input_nodes(material_asset, input_node)

    def return_LIST_all_matExpressions(self):
        self.walk_material_node_system()
        return self.LIST_all_matExpressions

    def return_LIST_all_matExpression_paramGroups(self):
        self.walk_material_node_system()
        return self.LIST_all_matExpression_paramGroups
    
