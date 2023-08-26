import unreal

import sys, os, importlib
from typing import List  # Import the List type from the typing module

# allow for import of custom python scripts
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)  



# LIST_stored_fileNames = [rf'C:/Users/blake/Pictures/Wallpaper/a.jpg',]

# class ValidationError(Exception):
#     pass


# def import_files(stored_filePaths, destination_path):

#     '''
#     Import Files into Project
#     '''

#     destination_path = unreal.EditorUtilityLibrary.get_current_content_browser_path()

#     # create asset_tools object
#     asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
#     # create asset_import_data object
#     my_asset_import_data = unreal.AutomatedAssetImportData()

#     # Setup Import Attributes
#     my_asset_import_data.destination_path = destination_path
#     my_asset_import_data.filenames = stored_filePaths
#     my_asset_import_data.replace_existing = True


#     print('Importing the following files:')
#     for filename in my_asset_import_data.filenames:
#         print(filename)
#         asset_tools.import_assets_automated(my_asset_import_data)


# # Compares ALL assets in current browser to stored_fileNames
# # stores matching assets into 'stored_assets' list
# ##
# # This is way to only select imported assets if there are multiple assets in current content browser path
# def get_recently_imported_assets() -> List[unreal.Texture2D]:

#     # list assets in current directory
#     current_directory = unreal.EditorUtilityLibrary.get_current_content_browser_path()
#     Editor_Asset_Lib = unreal.EditorAssetLibrary
#     list_asset_paths = Editor_Asset_Lib.list_assets(current_directory)
    
#     # initiliaze List for ASSETS in current content browser that were recently imported
#     stored_assets = []

#     for asset_path in list_asset_paths:

#         # Load the asset to expose properties (Details Panel View in UE)
#         loaded_asset = Editor_Asset_Lib.load_asset(asset_path)
#         print(f'----------------- Currently Loaded Asset: {loaded_asset.get_fname()}')

#         try: # Try and see if loaded_asset has 'asset_import_data'

#             # Get the source file path of the asset
#             asset_import_data = loaded_asset.get_editor_property('asset_import_data')
#             source_filepath = asset_import_data.get_first_filename()

#             # CHECK if content browser asset's source_filepath is in 'stored_fileNames'
#             if source_filepath not in LIST_stored_fileNames:
#                 unreal.log_warning(f'{loaded_asset.get_fname()} is NOT in "stored_fileNames"')
#                 continue

#             # CHECK if loaded asset is Texture2D
#             if not isinstance(loaded_asset, unreal.Texture2D):
#                 unreal.log_warning(f'{loaded_asset.get_fname()} is NOT instance of "unreal.Texture2D"')
#                 continue

#         # IF CHECKS PASS: append 'loaded_asset' to list named 'stored_assets'
#             print(f'{loaded_asset.get_fname()} appended to "stored_assets" list')
#             stored_assets.append(loaded_asset)

#         except AttributeError: # not all assets have asset import data
#             unreal.log_warning(f'{loaded_asset.get_fname()} DOES NOT CONTAIN editor property: "asset_import_data"')
#             pass

#     return stored_assets





######                                                          ######
######                   BLOCK OUT CODE                         ######    
######                                                          ######

# AutoMI_01_Load_Mat
def BLOCK_OUT_code():

        import AutoMI_01_Load_Mat
        importlib.reload(AutoMI_01_Load_Mat)           # Reloads imported .py file, without, edits to this imported file will not carry over

        single_selected_material = AutoMI_01_Load_Mat.get_single_selected_material()

        ###
        # Call TexParamData Class and Store selected Material's "all_texture_paramGroups" + "all_textures"
        inst_TexParamData = AutoMI_01_Load_Mat.TexParamData(single_selected_material.get_path_name())
        LIST_all_matExpression_paramGroups =   inst_TexParamData.return_LIST_all_matExpression_paramGroups()
        LIST_all_matExpressions =              inst_TexParamData.return_LIST_all_matExpressions()
        #
        ###

# AutoMI_02_Load_ParamGroup
# filter_matExpressions_by_user_selected_paramGroup():

        import AutoMI_02_Load_ParamGroup
        importlib.reload(AutoMI_02_Load_ParamGroup)           # Reloads imported .py file, without, edits to this imported file will not carry over

        ###
        # Call LoadParamGroup Class and return 'all_filtered_matExpressions' and 'all_textures_suffixes'
        inst_LoadParamGroup = AutoMI_02_Load_ParamGroup.LoadParamGroup(LIST_all_matExpressions, LIST_all_matExpression_paramGroups[0], single_selected_material)
        LIST_all_filtered_matExpressions, \
        DICT_all_filtered_matExpressions_textures_suffixes = inst_LoadParamGroup.filter_matExpressions_by_user_selected_paramGroup()
        #
        ###


# AutoMI_03_Select_Tex_Files
# def validate_texture_files_and_build_dictionary(self, filePaths, stored_filePaths):

        """
        Import assets into project.
        """
        # list of files to import
        files = [
            rf'C:\Users\blake\Pictures\Wallpaper\a_BC.jpg',
            rf'C:\Users\blake\Pictures\Wallpaper\a_N.jpg',
            rf'C:\Users\blake\Pictures\Wallpaper\b_BC.png',


        ]

        LIST_stored_filePaths = []

        DICT_grouped_filePaths_config = {}


        import AutoMI_03_Select_Tex_Files
        importlib.reload(AutoMI_03_Select_Tex_Files)           # Reloads imported .py file, without, edits to this imported file will not carry over

        ###
        # Call LoadParamGroup Class and return 'DICT_grouped_filePaths_config'
        inst_SelectTextureFiles = AutoMI_03_Select_Tex_Files.SelectTextureFiles(files, LIST_stored_filePaths, DICT_all_filtered_matExpressions_textures_suffixes, DICT_grouped_filePaths_config)
        DICT_grouped_filePaths_config = inst_SelectTextureFiles.validate_texture_files_and_build_dictionary()
        #
        ###
        # # Format and print DICT_all_filtered_matExpressions_textures_suffixes
        # print("DICT_all_filtered_matExpressions_textures_suffixes:")
        # for key, value in DICT_all_filtered_matExpressions_textures_suffixes.items():
        #     print(f"{key}: {value}")

        # print('-')
        # print('-')

        # Format and print DICT_grouped_filePaths_config
        print("DICT_grouped_filePaths_config:")
        for group, file_list in DICT_grouped_filePaths_config.items():
            print(group + ":")
            for file_info in file_list:
                print(f"  filePath:         {file_info['filePath']}")
                print(f"  fileName:         {file_info['fileName']}")
                print(f"  suffix:           {file_info['suffix']}")


        LIST_stored_filePaths = [
            rf'C:\Users\blake\Pictures\Wallpaper\a_BC.jpg',
            rf'C:\Users\blake\Pictures\Wallpaper\a_N.jpg',
            rf'C:\Users\blake\Pictures\Wallpaper\b_BC.png',

        ]

        return LIST_stored_filePaths


            
# # AutoMI_04_Build_MI
# def build_material_instances(self):

        # import AutoMI_04_Build_MI
        # importlib.reload(AutoMI_04_Build_MI)           # Reloads imported .py file, without, edits to this imported file will not carry over

        # destination_path = unreal.EditorUtilityLibrary.get_current_content_browser_path()
        

        # AutoMI_04_Build_MI.import_files(self.stored_filePaths, destination_path)

        # unreal.log(f'Successfully Imported to Path: {destination_path}')



###### working with

#       LIST_stored_filePaths
#       DICT_grouped_filePaths_config
#       DICT_all_filtered_matExpressions_textures_suffixes


#       destination_path = unreal.EditorUtilityLibrary.get_current_content_browser_path()





######



class ValidationError(Exception):
    pass



def import_files(LIST_stored_filePaths, destination_path):

    '''
    Import Files into Project
    '''

    destination_path = unreal.EditorUtilityLibrary.get_current_content_browser_path()

    # create asset_tools object
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    # create asset_import_data object
    my_asset_import_data = unreal.AutomatedAssetImportData()

    # Setup Import Attributes
    my_asset_import_data.destination_path = destination_path
    my_asset_import_data.filenames = LIST_stored_filePaths
    my_asset_import_data.replace_existing = True

    asset_tools.import_assets_automated(my_asset_import_data)


# Compares ALL assets in current browser to LIST_stored_filePaths
# stores matching assets into 'stored_assets' list
##
# This is way to only select imported assets if there are multiple assets in current content browser path
def store_recently_imported_assets(LIST_stored_filePaths) -> List[unreal.Texture2D]:

    # initiliaze List for ASSETS in current content browser that were recently imported
    LIST_recently_imported_assets = []

    LIST_all_current_dir_asset_paths = []

    # Get the asset registry #########################
    current_directory = unreal.EditorUtilityLibrary.get_current_content_browser_path()
    Asset_Registry = unreal.AssetRegistryHelpers.get_asset_registry()

    # Get the asset data for the specified folder path
    asset_data_list = Asset_Registry.get_assets_by_path(current_directory, recursive=True)

    # Append each Asset into One List
    for asset_data in asset_data_list:
        asset = asset_data.get_asset()
        LIST_all_current_dir_asset_paths.append(asset)


    for asset in LIST_all_current_dir_asset_paths:

        # Load the asset to expose properties (Details Panel View in UE)

        try: # Try and see if loaded_asset has 'asset_import_data'

            # Get the source file path of the asset
            asset_import_data = asset.get_editor_property('asset_import_data')
            asset_filepath = asset_import_data.get_first_filename()
            asset_filepath = asset_filepath.replace("/", "\\")                      # Switch / direction to compare against LIST_stored_filePaths (file selection from GUI)


            # CHECK if content browser asset's source_filepath is in 'stored_fileNames'
            if asset_filepath not in LIST_stored_filePaths:
                unreal.log_warning(f'{asset.get_fname()} is NOT in "LIST_stored_filePaths"')
                continue

            # CHECK if loaded asset is Texture2D
            if not isinstance(asset, unreal.Texture2D):
                unreal.log_warning(f'{asset.get_fname()} is NOT instance of "unreal.Texture2D"')
                continue

        # IF CHECKS PASS: append 'loaded_asset' to list named 'stored_assets'
            print(f'{asset.get_fname()} appended to "LIST_stored_assets" list')
            LIST_recently_imported_assets.append(asset)

        except AttributeError: # not all assets have asset import data
            unreal.log_warning(f'{asset.get_fname()} DOES NOT CONTAIN editor property: "asset_import_data"')
            pass

        
    print(f"PRINTING LIST_recently_imported_assets: {LIST_recently_imported_assets}")
    return LIST_recently_imported_assets


# TODO: We need config of 'DICT_grouped_filePaths_config' + DATA of 'LIST_recently_imported_assets' 
#
#       insert each ASSET into corresponding DICT of filePaths config
#
#


    # TODO: Return DICTs in Blockout Code for Comparison

#       LIST_stored_filePaths
#       DICT_grouped_filePaths_config
#       DICT_all_filtered_matExpressions_textures_suffixes


    # TODO: Make Sure Store_Recently_Added_Assets FilePath Naming Convention matches DICT_grouped_filePaths_config


def run():
    print("=")
    print("=")

    LIST_stored_filePaths = BLOCK_OUT_code()
    destination_path = unreal.EditorUtilityLibrary.get_current_content_browser_path()




    print(f'================== LIST_stored_filePaths: ================== {LIST_stored_filePaths}')

    unreal.log_warning("RUNNING import_files")
    import_files(LIST_stored_filePaths, destination_path)
    unreal.log_warning("RUNNING store_recently_imported_assets")
    # store_recently_imported_assets(LIST_stored_filePaths)



    


run()


######                                                          ######
######################################################################    
######                                                          ######

