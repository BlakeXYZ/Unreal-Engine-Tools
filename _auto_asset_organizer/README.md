<p align="center">
<img src="https://github.com/BlakeXYZ/Unreal-Engine-Tools/assets/37947050/06b00649-f1cb-4519-8c07-4eae4cbeaa14">
</p>

## <ins>Overview</ins>



<div align="center">Batch Automate moving of Assets into new Folders based on User selected Assets and User input Folder names.
</div>
<br>

<p align="center">
   
<img src="https://github.com/BlakeXYZ/Unreal-Engine-Tools/assets/37947050/2f0ccaa9-be51-4b83-b4d6-8cdfcd959654" width="700">
</p>


#### Pipeline Problem:

- Manually organizing the Content Browser is a tedious task and as a project's asset library grows, organization is vital to keeping you and your team's sanity. Creating Folder names one by one and dragging and dropping uniquely selected assets into their respective folders is time consuming. This tool solves this pipeline problem by Batch Automating the creation of Folders and the moving of Selected Assets.


#### Built with:
- UE 5.1.1
- UE Editor Utility Widgets + Blueprints





______
## <ins>Installation</ins>
<details open>
<summary><h4>1. Download Tool</h4></summary>
<br>

   - Download '[Unreal-Engine-Python-Projects](https://github.com/BlakeXYZ/Unreal-Engine-Python-Projects)' Repo
   - Extract _auto_asset_organizer Folder 
<p align="center">
<img src="https://github.com/BlakeXYZ/Unreal-Engine-Python-Projects/assets/37947050/d58cfd07-b09b-479f-9301-f23240f209f2" width="700">
</p>
</details>
<details open>
<summary><h4>3. Add "Auto Asset Organizer" Tool into UE Project</h4></summary>
<br>
   
   - Create
<p align="center">
<img src="https://github.com/BlakeXYZ/Unreal-Engine-Python-Projects/assets/37947050/1bdbf43e-3cf7-4dce-9fb5-c573a338d6eb" width="400">
<br>
</p>
</details>
<details open>
<summary><h4>4. Add Additional PYTHONPATHS</h4></summary>
<br>
   
   - Edit > Project Settings > Python
   - Add '_auto_material_instancer' folder as Additional Path
   - Prompted to RESTART UE, please do so
<p align="center">
<img src="https://github.com/BlakeXYZ/Unreal-Engine-Python-Projects/assets/37947050/fb5a49d7-8d01-401b-b374-dde9c0c86146" width="700">
</p>

**Upon Restart, your Main Menu should now contain a new Item which launches the _auto_material_instancer tool!**

<p align="center">
<img src="https://github.com/BlakeXYZ/Unreal-Engine-Python-Projects/assets/37947050/c7d07bac-3a87-44b9-a9e1-884728bee34d" width="700">
</p>
</details>

____________

## <ins>Quick Start</ins>

<details open>
<summary><h4>Tool Vocabulary</h4></summary>
<br>
   
- **_Master Material_** : User Material you wish to Instance
- **_Material Expression_** : Building blocks for creating Materials, colloquially known as 'Nodes'
- **_Parameter Group_** : User Material Expression Group you assign to Texture2D Expressions
- **_Suffix Pattern_** : User Naming Convention on Textures, anything after last '_' (underscore) is stored as suffix.
     - ex: Some_Texture_123abc, suffix = '_123abc'
  

> ❗ Assigning **_Parameter Groups_** and having **_Suffix Patterns_** are central to the tool.
<br>



</details>



<details open>
<summary><h4>Selected Master Material Requirements</h4></summary>
<br>
   
1. User **_Parameter Group_** is assigned to Texture2D Material Expressions you wish to auto fill with imported Textures. 
   <br>
2. Texture2D 'Material Expression Texture Base' must follow your custom **_Suffix Pattern_** / Naming convention.
   <br>
   <br>

<p align="center">
<img src="https://github.com/BlakeXYZ/Unreal-Engine-Python-Projects/assets/37947050/dbdd326b-1a0b-4897-9eec-1e00bcbe36cb" width="700">
</p>
<br>
</details>
<details open>
<summary><h4>Selected Master Material Example image</h4></summary>
<br>
<p align="center">
<img src="https://github.com/BlakeXYZ/Unreal-Engine-Python-Projects/assets/37947050/026c831c-2ad2-4d52-8d0f-2c971f5a64ea" width="700">
</p>
</details>

<details open>
<summary><h4>Selected Texture Files Requirements</h4></summary><br>
   
1. Texture File Names must contain a Suffix that matches one of the **_Suffix Patterns_** found in your Selected Master Material
   <br>
2. User must use at minimum, one (1) **_Suffix Pattern_** 
   - ex: Patterns Found: '_BC' '_N', Selected Texture Files: 'Another_Skin_BC' + no '_N' File _will_ work
   <br>
> :information_source: The following selected Texture Files will create 3 Material Instances based on Texture Files 'Group Name' (Anything before Suffix) <br>
> ex: Material Instance : 'MI_My_Material_Skin_01' that intakes '_BC' and '_N'
<p align="center">
<img src="https://github.com/BlakeXYZ/Unreal-Engine-Python-Projects/assets/37947050/607d44aa-0940-468b-b376-b1d5e48be8aa" width="700">
</p>
<br>
</details>

______
## <ins>Documentation</ins>

<details open> 
<summary><h4>Debugging - Output Log</h4></summary>
<br>
   
- **Please check Unreal Engine’s Output Log if the Tool is not working as expected.**
- **The tool will throw ‘ValidationError’ and ‘Warning’ alerts with context-specific explanations.**

Log examples:
```
LogPython: Error: utils.AutoMI_01_Load_Mat.ValidationError: Please select Asset of <class "Material">
-- Currently Selected Asset "Material_INSTANCE" is of <class 'MaterialInstanceConstant'>
```
```
LogPython: Warning: SKIPPING - Selected Texture File: "noMatchingSuffix_ORM" DOES NOT MATCH ANY SUFFIX PATTERNS.
Full file path: C:/Users/blake/Pictures/Textures/noMatchingSuffix_ORM.jpg
```

</details>

<details open>
<summary><h4>Tool Constraints</h4></summary>
<br>

```
#--- Accepted File Types
accepted_QFileDialog_fileTypes = ['*.bmp', '*.float', '*.jpeg', '*.jpg', '*.pcx', '*.png',
 '*.psd', '*.tga', '*.dds', '*.exr', '*.tif', '*.tiff']
```
```
#--- Imports Files into current directory
my_asset_import_data.destination_path = self.current_directory
```
```
#--- Removes M_ when building Material Instances
if single_selected_material_name.startswith('M_'):
   single_selected_material_name = single_selected_material_name[2:]
```
```
#--- Creates a Material Instance asset with a unique name based on the group name.
mi_asset = asset_tools.create_asset(f"MI_{single_selected_material_name}_{group}", parent_folder, None, material_factory)

#   ex: Master Material: 'My_Material' + Texture: 'Skin_01_BC' 
#       creates Material Instance named: 'MI_My_Material_Skin_01'
```



</details>


<details open>
<summary><h4>init_unreal .py</h4></summary>
<br>
   
On Initialization we are running two important steps:
   
- **sys.path.append(libs_subdir)**
   - This sets up 3rd Party Python Library Dependencies (ex: PySide2, Unreal Stylesheet)
- **def build_menu()**
   - This builds an easy access Menu inside our LevelEditor.MainMenu, in which we can launch our Tool.
</details>

______


