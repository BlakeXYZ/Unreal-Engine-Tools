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



######                                                          ######
######                   BLOCK OUT CODE                         ######    
######                                                          ######

#TODO: SETUP "CHECKPOINT" code
#
#   Get A Materials Paramter Group and print out all INFO
# AutoMI_01_Load_Mat
def get_single_selected_material():

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
            
        # print('============== RUNNING FILTER ==============')
        # for matExpressions in LIST_all_matExpressions:
        #     if matExpressions.get_editor_property("group") == LIST_all_matExpression_paramGroups[0]:
        #             print(matExpressions)
        #             print(f'SELECTED Texture Parameter group name --    {matExpressions.get_editor_property("group")}')
        #             print(f'Texture Parameter name --                   {matExpressions.get_editor_property("parameter_name")}')
        #             print(f'Texture Parameter file --                   {matExpressions.get_editor_property("texture")}')
        #             print('============================')



        # # Create an empty dictionary to store SUFFIX for each texture
        LIST_all_filtered_matExpressions = []
        DICT_all_textures_suffixes = {}

        for matExpression in LIST_all_matExpressions:
            if matExpression.get_editor_property("group") == LIST_all_matExpression_paramGroups[0]: # FILTER out matExpressions based on comboBox_LIST_all_matExpression_paramGroups.currentText()
                    
                    texture_file_name = matExpression.get_editor_property("texture").get_name()
                    
                    ## GETTING SUFFIX LOGIC and VALIDATION
                    #
                    # Split texture_file_name from the RIGHT by "_" and get last part as suffix
                    split_file_name = texture_file_name.rsplit("_", 1) # split only once from the right
                    if len(split_file_name) > 1:
                            suffix = split_file_name[1]
                    else:
                        raise ValidationError(f'Selected Material:""{single_selected_material.get_name()}" >> Node:"{matExpression.get_editor_property("parameter_name")}" >> Texture File:"{texture_file_name}"  MASTER MATERIAL TEXTURE FILES MUST CONTAIN SUFFIXES')
                    #
                    ##

                    LIST_all_filtered_matExpressions.append(matExpression)
                    # Make KEY : VALUE pair - matExpression : Suffix
                    DICT_all_textures_suffixes[matExpression] = suffix
                        


        for matExpression in LIST_all_matExpressions:
             print(matExpression.get_editor_property("texture").get_name())
             print(DICT_all_textures_suffixes[matExpression])
                    



    





# TODO: Store LIST_ALL_TEXTURES into DICTIONARY


#   Get texture file list to IMPORT
def importAssets():

    
    """
    Import assets into project.
    """
    # list of files to import
    filePaths = [
        rf'C:\Users\blake\Pictures\Wallpaper\a_BC.jpg',
        rf'C:\Users\blake\Pictures\Wallpaper\bboy_N.jpg',

    ]
    # Initialize an empty dictionary
    DICT_fileNames = {}

    for filePath in filePaths:
        # Get the base filename (without directory)
        baseFileName = os.path.basename(filePath)
        # Remove the file extension
        fileNameWithoutExtension, fileExtension = os.path.splitext(baseFileName)

        ## GETTING SUFFIX LOGIC and VALIDATION
        #
        # Split texture_file_name from the RIGHT by "_" and get last part as suffix
        split_file_name = fileNameWithoutExtension.rsplit("_", 1) # split only once from the right
        if len(split_file_name) > 1:
                suffix = split_file_name[1]
        else:
            raise ValidationError(f'Selected Texture File: ""{fileNameWithoutExtension}" DOES NOT CONTAIN A SUFFIX. full file path: {filePath}')
        #
        ##

        # Create a dictionary entry for the current file
        DICT_fileNames[filePath] = {
            'fileName': fileNameWithoutExtension,
            'suffix': suffix
        }

    # Now, DICT_fileNames contains information about each file
    for filePath, info_dict in DICT_fileNames.items():
        print(f'File Path:                  {filePath}')
        print(f'File Name:                  {info_dict["fileName"]}')
        print(f'Suffix:                     {info_dict["suffix"]}')
        print()









    # # create asset tools object
    # assetTools = unreal.AssetToolsHelpers.get_asset_tools()
    # # create asset import data object        
    # assetImportData = unreal.AutomatedAssetImportData()
    # # set assetImportData attributes
    # assetImportData.destination_path = '/Game/Python/Material_Instancer/Textures'
    # assetImportData.filenames = fileNames
    # assetImportData.replace_existing = True
    # assetTools.import_assets_automated(assetImportData)



def run():
    print("=")
    print("=")
    print("========== running get_single_selected_material ===========")
    get_single_selected_material()
    print("========== running importAssets ===========")
    importAssets()

run()


######                                                          ######
######################################################################    
######                                                          ######

