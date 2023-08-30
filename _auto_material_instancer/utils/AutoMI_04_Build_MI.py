import unreal

import sys, os, importlib
from typing import List  # Import the List type from the typing module


# allow for import of custom python scripts
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)  

class ValidationError(Exception):
    pass

class BuildMaterialInstances:

    def __init__(self, LIST_stored_filePaths, DICT_grouped_filePaths_config, DICT_all_filtered_matExpressions_textures_suffixes, single_selected_material):
        


        self.LIST_stored_filePaths = LIST_stored_filePaths
        self.DICT_grouped_filePaths_config = DICT_grouped_filePaths_config

        # Variables for 'build_material_instances'
        self.DICT_all_filtered_matExpressions_textures_suffixes = DICT_all_filtered_matExpressions_textures_suffixes
        self.single_selected_material = single_selected_material



        self.current_directory = unreal.EditorUtilityLibrary.get_current_content_browser_path()



    def import_files(self):

        '''
        Import Files into Project
        '''
        # create asset_tools object
        asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
        # create asset_import_data object
        my_asset_import_data = unreal.AutomatedAssetImportData()

        # Setup Import Attributes
        my_asset_import_data.destination_path = self.current_directory
        my_asset_import_data.filenames = self.LIST_stored_filePaths
        my_asset_import_data.replace_existing = True

        asset_tools.import_assets_automated(my_asset_import_data)


    # Compares ALL assets in current browser to LIST_stored_filePaths
    # stores matching assets into 'stored_assets' list
    ##
    # This is way to only select imported assets if there are multiple assets in current content browser path

    #=== RUN INSIDE function below: insert_recent_assets_into_DICT_grouped_filepaths_config
    def store_recently_imported_assets(self) -> List[unreal.Texture2D]:

        # initiliaze List for ASSETS in current content browser that were recently imported
        LIST_recently_imported_assets = []

        LIST_all_current_dir_asset_paths = []

        # Get the asset registry #########################
        Asset_Registry = unreal.AssetRegistryHelpers.get_asset_registry()

        # Get the asset data for the specified folder path
        asset_data_list = Asset_Registry.get_assets_by_path(self.current_directory , recursive=True)

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

                # CHECK if content browser asset's source_filepath is in 'stored_fileNames'
                if asset_filepath not in self.LIST_stored_filePaths:
                    continue

                # CHECK if loaded asset is Texture2D
                if not isinstance(asset, unreal.Texture2D):
                    continue

            # IF CHECKS PASS: append 'loaded_asset' to list named 'stored_assets'
                LIST_recently_imported_assets.append(asset)

            except AttributeError: # not all assets have asset import data
                pass

        return LIST_recently_imported_assets


    # We need config of 'DICT_grouped_filePaths_config' + DATA of 'LIST_recently_imported_assets' 
    #       insert each ASSET into corresponding DICT of filePaths config
    
    #=== RUN INSIDE function below: build_material_instances
    def insert_recent_assets_into_DICT_grouped_filepaths_config(self):

        # Running custom class method
        LIST_recently_imported_assets = self.store_recently_imported_assets()

        for asset in LIST_recently_imported_assets: 
            asset_name = (asset.get_name())
            # Iterate through DICT_grouped_filePaths_config and check for matching conditions
            for group, file_list in self.DICT_grouped_filePaths_config.items():
                for file_info in file_list:

                    unreal.log_warning(f'printing file info- fileName and asset_name')
                    print(file_info['fileName'])
                    print(asset_name)
                    if file_info['fileName'] == asset_name:
                        # Add the asset to the file_info dictionary under 'assetData'
                        file_info['assetData'] = asset
                        

        return self.DICT_grouped_filePaths_config
    


    def build_material_instances(self):


        # Running custom class methods
        self.import_files()
        updated_DICT_grouped_filePaths_config = self.insert_recent_assets_into_DICT_grouped_filepaths_config()

        # Asset Path:
        # Get Parent Path
        parent_mat_asset_path = self.single_selected_material.get_path_name()
        parent_folder = unreal.Paths.get_path(parent_mat_asset_path)

        # Get Selected Master Material Root Name
        single_selected_material_name = self.single_selected_material.get_name()
        if single_selected_material_name.startswith('M_'):
            single_selected_material_name = single_selected_material_name[2:]

        # for each filePath GROUP ---- make a Material Instance
        for group, file_list in updated_DICT_grouped_filePaths_config.items():

            # Build the Material Instance
            asset_tools = unreal.AssetToolsHelpers.get_asset_tools()
            material_factory = unreal.MaterialInstanceConstantFactoryNew()

            # Create a Material Instance asset with a unique name based on the group name.
            mi_asset = asset_tools.create_asset(f"MI_{single_selected_material_name}_{group}", parent_folder, None, material_factory)

            # Assign Parent to Instance
            unreal.MaterialEditingLibrary.set_material_instance_parent(mi_asset, self.single_selected_material)


            #  for each file_info ----- find matching file expression
            #                           and 
            #                           set newly created Material Instance values
            for file_info in file_list:
                file_suffix =   file_info['suffix']
                asset_data =    file_info['assetData']

                for matExpression, matExpressionSuffix in self.DICT_all_filtered_matExpressions_textures_suffixes.items():
                    if matExpressionSuffix == file_suffix:

                        # set mi_asset values ---- find matching matExpression and assign Texture2d ( file_info['assetData'] )
                        unreal.MaterialEditingLibrary.set_material_instance_texture_parameter_value(mi_asset, matExpression.get_editor_property('parameter_name'), asset_data)




