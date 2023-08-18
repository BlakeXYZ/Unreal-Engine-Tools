"""
UTILITY FUNCTIONS FOR ASSETS (CONTENT BROWSER)

    Common Unreal Classes:

        EditorUtilityLibrary
        EditorAssetLibrary
        AssetRegistryHelper
        AssetToolsHelpers

"""


import unreal


def UTILITY_import_files(my_import_file_list, my_destination_path):

    '''
    Import Files into Project
    '''

    print('Calling: UTILITY_import_files')

    # create asset_tools object
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
    # create asset_import_data object
    asset_import_data = unreal.AutomatedAssetImportData()

    # Setup Import Attributes
    asset_import_data.destination_path = my_destination_path
    asset_import_data.filenames = my_import_file_list
    asset_import_data.replace_existing = True


    print('Importing the following files:')
    for filename in asset_import_data.filenames:
        print(filename)

    try:
    # asset tool: import assets automated using --> my asset_import_data 
        asset_tools.import_assets_automated(asset_import_data)
        print('Import successful!')
    except Exception as e:
        print('Import failed with error:')
        print(e)






#   TODO: After Import of Textures, store them as type 'Asset'



