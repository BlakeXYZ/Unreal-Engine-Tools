import unreal

import sys, os, importlib
from typing import List  # Import the List type from the typing module

import AutoMI_01_Load_Mat
importlib.reload(AutoMI_01_Load_Mat)           # Reloads imported .py file, without, edits to this imported file will not carry over


# allow for import of custom python scripts
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)  

class ValidationError(Exception):
    pass

class LoadParamGroup:
    def __init__(self, LIST_all_matExpressions, user_selected_paramGroup, single_selected_material):

        self.LIST_all_matExpressions = LIST_all_matExpressions
        self.user_selected_paramGroup = user_selected_paramGroup
        self.single_selected_material = single_selected_material
        
        # Create an empty dictionary to store SUFFIX for each texture
        self.LIST_all_filtered_matExpressions = []
        self.DICT_all_filtered_matExpressions_textures_suffixes = {}

    def filter_matExpressions_by_user_selected_paramGroup(self):

        for matExpression in self.LIST_all_matExpressions:
            if matExpression.get_editor_property("group") == self.user_selected_paramGroup: # FILTER out matExpressions based on comboBox_LIST_all_matExpression_paramGroups.currentText()
                    
                    texture_file_name = matExpression.get_editor_property("texture").get_name()
                    
                    ### GETTING SUFFIX LOGIC and VALIDATION
                    #
                    # Split texture_file_name from the RIGHT by "_" and get last part as suffix
                    split_file_name = texture_file_name.rsplit("_", 1) # split only once from the right
                    if len(split_file_name) > 1:
                            suffix = split_file_name[1]
                    else:
                        raise ValidationError(f'Selected Material:""{self.single_selected_material.get_name()}" >> Node:"{matExpression.get_editor_property("parameter_name")}" >> Texture File:"{texture_file_name}"  MASTER MATERIAL TEXTURE FILES MUST CONTAIN SUFFIXES')
                    #
                    ###

                    self.LIST_all_filtered_matExpressions.append(matExpression)
                    # Make KEY : VALUE pair - matExpression : Suffix
                    self.DICT_all_filtered_matExpressions_textures_suffixes[matExpression] = suffix
                        

        return self.LIST_all_filtered_matExpressions, self.DICT_all_filtered_matExpressions_textures_suffixes



