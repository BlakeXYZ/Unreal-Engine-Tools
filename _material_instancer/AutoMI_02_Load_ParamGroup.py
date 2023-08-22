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



def filter_textures_by_user_selected_paramGroup(LIST_all_texture_paramGroups, LIST_all_textures, user_selected_paramGroup):

    print('============== RUNNING FILTER ==============')
    for texture in LIST_all_textures:
        if texture.get_editor_property("group") == user_selected_paramGroup:
                print(f'SELECTED Texture Parameter group name --    {texture.get_editor_property("group")}')
                print(f'Texture Parameter name --                   {texture.get_editor_property("parameter_name")}')
                print(f'Texture Parameter file --                   {texture.get_editor_property("texture")}')

