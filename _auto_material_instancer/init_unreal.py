import os
import sys
import unreal

# Pre Reqs - in Project Settings > Python > Additional Paths: ADD Script Directory
# Append libs_subdir to setup 3rd Party Python Libraries (ex: PySide2)
script_dir = os.path.dirname(os.path.abspath(__file__))
libs_subdir = os.path.join(script_dir, 'libs')
sys.path.append(libs_subdir)  


unreal.log_warning(f"RUNNING INIT UNREAL py INSIDE script dir: {script_dir}")
unreal.log_warning(f"APPENDING libs_subdir: {libs_subdir}")


# Build Py Tool menu on LevelEditor.MainMenu
def build_menu():


    ToolMenus = unreal.ToolMenus.get()

    get_main_menu = ToolMenus.find_menu("LevelEditor.MainMenu")


    entry = unreal.ToolMenuEntry(
                                name="Python.Tools",
                                # If you pass a type that is not supported Unreal will let you know,
                                type=unreal.MultiBlockType.MENU_ENTRY,
                                # this will tell unreal to insert this entry into the First spot of the menu
                                insert_position=unreal.ToolMenuInsert("", unreal.ToolMenuInsertType.FIRST)
    )

    entry.set_label("Auto Material Instancer")
    # this is what gets executed on click
    entry.set_string_command(unreal.ToolMenuStringCommandType.PYTHON, '', string='import AutoMI; import importlib; importlib.reload(AutoMI)')

    
    add_custom_menu = get_main_menu.add_sub_menu("MyCustomMenu", "MyPythonAutomation", "BXYZPythonToolsName", "BXYZ Python Tools")

    # add our new entry to the new 
    custom_menu = ToolMenus.find_menu("LevelEditor.MainMenu.BXYZPythonToolsName")
    custom_menu.add_menu_entry("Scripts",entry)

    ToolMenus.refresh_all_widgets()

build_menu()