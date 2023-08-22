import unreal

import sys, os
from typing import List  # Import the List type from the typing module

# allow for import of custom python scripts
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)  






stored_fileNames = [rf'C:/Users/blake/Pictures/Wallpaper/a.jpg',]

class ValidationError(Exception):
    pass




def import_files(my_import_file_list, my_destination_path):

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
    my_asset_import_data.filenames = my_import_file_list
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
