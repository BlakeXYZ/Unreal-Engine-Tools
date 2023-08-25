import unreal

import sys, os, importlib
from typing import List  # Import the List type from the typing module

# import AutoMI_01_Load_Mat
# importlib.reload(AutoMI_01_Load_Mat)           # Reloads imported .py file, without, edits to this imported file will not carry over


# allow for import of custom python scripts
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)  

class ValidationError(Exception):
    pass



### TODO: MAKE this FUNCTION CALLABLE in main code: material_instancer and CALL DICT_all_textures_suffixes 

class SelectTextureFiles:
    def __init__(self, filePaths, stored_filePaths, DICT_all_textures_suffixes, DICT_grouped_filePaths_config):

        self.filePaths = filePaths
        self.stored_filePaths = stored_filePaths
        self.DICT_all_textures_suffixes = DICT_all_textures_suffixes
        self.DICT_grouped_filePaths_config = DICT_grouped_filePaths_config
    
    #   Get texture file list to IMPORT
    def validate_texture_files_and_build_dictionary(self):

        # Initialize at very beginning, we want to keep memory of past instances (if QFileDialog is opened multiple times)
        if not self.DICT_grouped_filePaths_config:
            self.DICT_grouped_filePaths_config = {}

        for filePath in self.filePaths:
            
            # Check that ensures filePath is not added to Dictionary TWICE
            if filePath in self.stored_filePaths:
                continue

            # Get the base filename (without directory)
            baseFileName = os.path.basename(filePath)
            # Remove the file extension
            fileNameWithoutExtension, fileExtension = os.path.splitext(baseFileName)

            ###### GETTING SUFFIX LOGIC and VALIDATION
            ##
            ##
            # Split texture_file_name from the RIGHT by "_" and get last part as suffix
            split_file_name = fileNameWithoutExtension.rsplit("_", 1) # split only once from the right

            try:
                root, suffix = split_file_name
            except:
                # VALIDATE if filePath contains any SUFFIX
                unreal.log_warning(f'SKIPPING - Selected Texture File: "{fileNameWithoutExtension}" DOES NOT CONTAIN A SUFFIX. Full file path: {filePath}')
                continue

            # VALIDATE if filePath Suffixes are in selected material textures suffixes
            if suffix not in self.DICT_all_textures_suffixes.values():
                unreal.log_warning(f'SKIPPING - Selected Texture File: "{fileNameWithoutExtension}" DOES NOT MATCH ANY MASTER MATERIAL TEXTURE SUFFIXES. Full file path: {filePath}')
                continue
            
            if root not in self.DICT_grouped_filePaths_config: # add new root list
                self.DICT_grouped_filePaths_config[root] = []

            # Create a dictionary entry for the current filePath
            self.DICT_grouped_filePaths_config[root].append({
                'filePath': filePath,
                'fileName': fileNameWithoutExtension,
                'suffix': suffix
            })


            ##
            ##
            ######


        return self.DICT_grouped_filePaths_config














######                                                          ######
######                   BLOCK OUT CODE                         ######    
######                                                          ######

# #
# #   Get A Materials Paramter Group and print out all INFO
# # AutoMI_01_Load_Mat
# def get_single_selected_material():

#         import AutoMI_01_Load_Mat
#         importlib.reload(AutoMI_01_Load_Mat)           # Reloads imported .py file, without, edits to this imported file will not carry over

#         single_selected_material = AutoMI_01_Load_Mat.get_single_selected_material()

#         ###
#         # Call TexParamData Class and Store selected Material's "all_texture_paramGroups" + "all_textures"
#         inst_TexParamData = AutoMI_01_Load_Mat.TexParamData(single_selected_material.get_path_name())
#         LIST_all_matExpression_paramGroups =   inst_TexParamData.return_LIST_all_matExpression_paramGroups()
#         LIST_all_matExpressions =              inst_TexParamData.return_LIST_all_matExpressions()
#         #
#         ###
            
#         # print('============== RUNNING FILTER ==============')
#         # for matExpressions in LIST_all_matExpressions:
#         #     if matExpressions.get_editor_property("group") == LIST_all_matExpression_paramGroups[0]:
#         #             print(matExpressions)
#         #             print(f'SELECTED Texture Parameter group name --    {matExpressions.get_editor_property("group")}')
#         #             print(f'Texture Parameter name --                   {matExpressions.get_editor_property("parameter_name")}')
#         #             print(f'Texture Parameter file --                   {matExpressions.get_editor_property("texture")}')
#         #             print('============================')



#         # # Create an empty dictionary to store SUFFIX for each texture
#         LIST_all_filtered_matExpressions = []
#         DICT_all_textures_suffixes = {}

#         for matExpression in LIST_all_matExpressions:
#             if matExpression.get_editor_property("group") == LIST_all_matExpression_paramGroups[0]: # FILTER out matExpressions based on comboBox_LIST_all_matExpression_paramGroups.currentText()
                    
#                     texture_file_name = matExpression.get_editor_property("texture").get_name()
                    
#                     ## GETTING SUFFIX LOGIC and VALIDATION
#                     #
#                     # Split texture_file_name from the RIGHT by "_" and get last part as suffix
#                     split_file_name = texture_file_name.rsplit("_", 1) # split only once from the right
#                     if len(split_file_name) > 1:
#                             suffix = split_file_name[1]
#                     else:
#                         raise ValidationError(f'Selected Material:""{single_selected_material.get_name()}" >> Node:"{matExpression.get_editor_property("parameter_name")}" >> Texture File:"{texture_file_name}"  MASTER MATERIAL TEXTURE FILES MUST CONTAIN SUFFIXES')
#                     #
#                     ##

#                     LIST_all_filtered_matExpressions.append(matExpression)
#                     # Make KEY : VALUE pair - matExpression : Suffix
#                     DICT_all_textures_suffixes[matExpression] = suffix
                        


#         for matExpression in LIST_all_matExpressions:
#              print(matExpression.get_editor_property("texture").get_name())
#              print(DICT_all_textures_suffixes[matExpression])

#         print(DICT_all_textures_suffixes)

#         print("Loaded Material Suffixes")
#         for key, value in DICT_all_textures_suffixes.items():
#             print(f'_{value}')




#         return DICT_all_textures_suffixes
                    


# ### TODO: MAKE this FUNCTION CALLABLE in main code: material_instancer and CALL DICT_all_textures_suffixes 

# #   Get texture file list to IMPORT
# def importAssets(DICT_all_textures_suffixes):

    
#     """
#     Import assets into project.
#     """
#     # list of files to import
#     files = [
#         rf'C:\Users\blake\Pictures\Wallpaper\a_collection_01_BC.jpg',
#         rf'C:\Users\blake\Pictures\Wallpaper\a_collection_01_N.jpg',
#         rf'C:\Users\blake\Pictures\Wallpaper\b_collection_02_BC.jpg'

#     ]




#     # Initialize an empty dictionary
#     DICT_grouped_filePaths_config = {}

#     for filePath in files:
#         # Get the base filename (without directory)
#         baseFileName = os.path.basename(filePath)
#         # Remove the file extension
#         fileNameWithoutExtension, fileExtension = os.path.splitext(baseFileName)

#         ###### GETTING SUFFIX LOGIC and VALIDATION
#         ##
#         ##
#         # Split texture_file_name from the RIGHT by "_" and get last part as suffix
#         split_file_name = fileNameWithoutExtension.rsplit("_", 1) # split only once from the right


#         # build Dictionary lists based on root of fileNameWithoutExtension
#         if len(split_file_name) == 2:
#             root, suffix = split_file_name 
#             if root not in DICT_grouped_filePaths_config: # add new root list
#                 DICT_grouped_filePaths_config[root] = []

#             # Create a dictionary entry for the current filePath
#             DICT_grouped_filePaths_config[root].append({
#                 'filePath': filePath,
#                 'fileName': fileNameWithoutExtension,
#                 'suffix': suffix
#             })

#             # VALIDATE if filePath Suffixes are in selected material textures suffixes
#             if suffix not in DICT_all_textures_suffixes.values():
#                 raise ValidationError(f'Suffix ""{suffix}" in file "{fileNameWithoutExtension}" DOES NOT MATCH ANY MASTER MATERIAL TEXTURE SUFFIXES. Full file path: {filePath}')
#         else:
#         # VALIDATE if filePath contains any SUFFIX
#             raise ValidationError(f'Selected Texture File: ""{fileNameWithoutExtension}" DOES NOT CONTAIN A SUFFIX. Full file path: {filePath}')
        
#         ##
#         ##
#         ######

#     # Iterate through the file groups and print configuration
#     for root_group, files in DICT_grouped_filePaths_config.items():
#          print(f'=== Root Group: {root_group}')
#          for file_info in files:
#             print(f'File Path:                  {file_info["filePath"]}')
#             print(f'File Name:                  {file_info["fileName"]}')
#             print(f'Suffix:                     {file_info["suffix"]}')
#             print('-')










#     # # create asset tools object
#     # assetTools = unreal.AssetToolsHelpers.get_asset_tools()
#     # # create asset import data object        
#     # assetImportData = unreal.AutomatedAssetImportData()
#     # # set assetImportData attributes
#     # assetImportData.destination_path = '/Game/Python/Material_Instancer/Textures'
#     # assetImportData.filenames = fileNames
#     # assetImportData.replace_existing = True
#     # assetTools.import_assets_automated(assetImportData)



# def run():
#     print("=")
#     print("=")


#     print("========== running get_single_selected_material ===========")
#     DICT_all_textures_suffixes = get_single_selected_material()

    
#     print("========== running importAssets ===========")
#     importAssets(DICT_all_textures_suffixes)

# run()


######                                                          ######
######################################################################    
######                                                          ######

