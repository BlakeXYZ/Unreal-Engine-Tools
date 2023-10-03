#! python3
import unreal

### A tool that move selected Content Browser assets and 
### moves them into child folder based on Asset Type
###

# TODO: Check if Assets are sitting in correct subdirectory (ex: user accidentally moves FX asset into Material folder)

def get_selected_content_browser_assets():
    # https://docs.unrealengine.com/5.0/en-US/PythonAPI/class/EditorUtilityLibrary.html?highlight=editorutilitylibrary#unreal.EditorUtilityLibrary
    editor_utility = unreal.EditorUtilityLibrary()
    selected_assets = editor_utility.get_selected_assets()

    return selected_assets


def move_to_folders(my_asset):

    folder_config = {
        'folder_per_type': [
            {'type': (unreal.MaterialInstance, unreal.Material),    'folder': '/Materials'},
            {'type': unreal.Texture,                                'folder': '/Textures'},
            {'type': (unreal.NiagaraSystem, unreal.ParticleSystem),  'folder': '/FX'},            
        ]
    }

    # print('Using a for each loop')
    for asset in my_asset:
        print('--------------')

    # Get Asset Name, Path, and Folder
        name = asset.get_name()
        old_asset_path = asset.get_path_name()
        parent_folder = unreal.Paths.get_path(old_asset_path)

        # See Asset Type
        print(f'{name} is a class type of {type(asset)}')

    # Iterate over each prefix_info in the 'folder_per_type' list in the rename_config dictionary
        for folder_info in folder_config['folder_per_type']:
        # Retrieve the asset_type and asset_prefix from the current prefix_info dictionary
            asset_type =    folder_info['type']
            asset_folder =  folder_info['folder']

        # Check if the my_asset is an instance of the current asset_type
            if isinstance(asset, asset_type):
            # If the conditions are met, prepend the asset_prefix to the name and return the modified name
                print(f'{name} --> {asset_folder}')
                # return asset_folder + name

            # Create a new folder in the specified directory path
                new_folder = parent_folder + asset_folder

            # Statement to prevent duplicating and moving into a new Grand Child Folder. Example /Parent/Materials/Materials etc.
                if parent_folder.endswith(asset_folder):
                    print(f'{asset_folder} already exists')
                    continue

            # If Directory Does not Exist, Create a new one
                if not unreal.EditorAssetLibrary.does_directory_exist(new_folder):
                    unreal.EditorAssetLibrary.make_directory(new_folder)
                else:
                    print(f'{new_folder} already Exists')

            # Place into New Asset Path
                new_asset_path = new_folder + '/' + name
                rename_success = unreal.EditorAssetLibrary.rename_asset(old_asset_path, new_asset_path)
                print(f'moving... {old_asset_path} --> {new_asset_path}')

                if not rename_success:
                    unreal.log_error(f'Could Not Rename {old_asset_path}')


def run():

    unreal.log('*****')
    unreal.log('****')
    unreal.log('*** Running File Organizer ***')
    unreal.log('**')

    my_selected_assets = get_selected_content_browser_assets()
    move_to_folders(my_selected_assets)

run()

