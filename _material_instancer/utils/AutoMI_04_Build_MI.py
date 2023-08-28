import unreal

import sys, os, importlib
from typing import List  # Import the List type from the typing module

# allow for import of custom python scripts
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)  



class ValidationError(Exception):
    pass


# TODO: Build out as CLASS

def import_files(LIST_stored_filePaths, destination_path):

    '''
    Import Files into Project
    '''
    unreal.log_warning("IMPORTING FILES FUNCTION")

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

