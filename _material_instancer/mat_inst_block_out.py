import unreal

import sys, os
from typing import List  # Import the List type from the typing module

# allow for import of custom python scripts
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)  



#       VALIDATION CODE
#           Before  Importing Images
#           and Connecting Images into Material Instance...
#
#       - ENSURE only Texture2d File Formats are Selectable in File Dialog
#       - CHECK if single selected Content Browser Asset
#       - COMPARE Master Mat Tex Params NAMES suffix     == stored_fileNames suffix
#       - COMPARE Master Mat Tex Params COUNT            == stored_fileNames COUNT 

#   IF CHECKS PASS continue to...
#
#       - Import Images
#       - get_recently_imported_assets
#       - Build Material Instance of Selected Master Material
#       - Slot in imported_assets (Texture2d) into Material Instance




stored_fileNames = [rf'C:/Users/blake/Pictures/Wallpaper/a.jpg',]

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
    editor_asset_lib = unreal.EditorAssetLibrary
    list_asset_paths = editor_asset_lib.list_assets(current_directory)
    
    # initiliaze List for ASSETS in current content browser that were recently imported
    stored_assets = []

    for asset_path in list_asset_paths:

        # Load the asset to expose properties (Details Panel View in UE)
        loaded_asset = editor_asset_lib.load_asset(asset_path)
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
    
        


# returns selected assets inside content browser
# filters out selection to a single asset of <class Material>
def get_single_selected_content_browser_material() -> List[unreal.Material]:

    editor_utility = unreal.EditorUtilityLibrary()
    selected_assets = editor_utility.get_selected_assets()

    stored_master_material = []

    # CHECK if number of selected assets is ONE
    if len(selected_assets) != 1:
        unreal.log_warning(f'Please select only 1 Master Material in Content Browser')
        return  # Exit the function if the condition is not met

    # CHECK if selected asset is instance of <class Material>
    for asset in selected_assets:
        if not isinstance(asset, unreal.Material):
            unreal.log_warning(f'Currently Selected Asset "{asset.get_name()}" is a {type(asset)}')
            unreal.log_warning(f'Please select Asset of <class "Material">')
            continue

    # IF CHECKS PASS then append asset to 'stored_master_material'
        unreal.log(f'Master Material: "{asset.get_name()}" selected!')
        stored_master_material.append(asset)

    return stored_master_material


def run():
    get_single_selected_content_browser_material()


    # import_files()





run()

