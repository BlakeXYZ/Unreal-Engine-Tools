<p align="center">
<img src="https://github.com/BlakeXYZ/Unreal-Engine-Python-Projects/assets/37947050/5cc0c648-8982-4adc-93f1-49bd91ee1265">
</p>

## <ins>Overview</ins>



<h4 align="center">Batch Automate creation of Material Instances based on User selected Master Material, Param Group, and Textures.
</h4>

<p align="center">
   
<img src="https://github.com/BlakeXYZ/Unreal-Engine-Python-Projects/assets/37947050/12ffa665-6fbb-4e49-ac02-c8d8681af04a" width="700">
</p>


Pipeline Problem:

Manually creating a Material Instance, importing new textures and slotting each texture into correct Parameter Group Texture Slots is time consuming. Especially if you have to setup many Material Instances at once. (e.g. setting up several weapon 'skin' variants) This tool solves this time consuming pipeline problem by Batch Automating Material Instances.


Built with:
- UE 5.1.1
- UE embedded Python 3.9.7
- PySide2 ([see libs](https://github.com/BlakeXYZ/Unreal-Engine-Python-Projects/tree/main/_auto_material_instancer/libs))

______
## <ins>Installation</ins>
<details>
<summary>1. Activate Python Editor Script Plugin</summary>
   
   - Edit > Plugins > Scripting
   - Prompted to RESTART UE, please do so
<p align="center">
<img src="https://github.com/BlakeXYZ/Unreal-Engine-Python-Projects/assets/37947050/facf1038-dcdf-443d-aa9d-2d5dc3fdbb8c" width="700">
</p>
</details>
<details>
<summary>2. Download Tool</summary>

   - Download 'Unreal-Engine-Python-Projects' Repo
   - Extract _auto_material_instancer Folder 
<p align="center">
<img src="https://github.com/BlakeXYZ/Unreal-Engine-Python-Projects/assets/37947050/d58cfd07-b09b-479f-9301-f23240f209f2" width="700">
</p>
</details>
<details>
<summary>3. Add "Auto Material Instancer" Tool into UE Project</summary>

   - Create new Folder inside /All/Content named Python
   - Right click Python Folder and 'Show in Explorer'
   - Move Tool into /Python File Explorer directory
   - 'Import' changes
   - 'Yes' import options 
<p align="center">
<img src="https://github.com/BlakeXYZ/Unreal-Engine-Python-Projects/assets/37947050/1bdbf43e-3cf7-4dce-9fb5-c573a338d6eb" width="400">
<br>
<br>
<img src="https://github.com/BlakeXYZ/Unreal-Engine-Python-Projects/assets/37947050/bcc4b0b9-fb8b-48e2-8b39-8833e569c3e6" width="700">
<br>
<br>
<img src="https://github.com/BlakeXYZ/Unreal-Engine-Python-Projects/assets/37947050/bd046b38-cfb1-4f61-bea9-352e43346638" width="400">
<br>
<br>
<img src="https://github.com/BlakeXYZ/Unreal-Engine-Python-Projects/assets/37947050/3e9a674d-3910-464f-a52a-1431f9cddce9" width="400">
</p>
</details>
<details>
<summary>4. Add Additional PYTHONPATHS</summary>
   
   - Edit > Project Settings > Python
   - Add '_auto_material_instancer' folder as Additional Path
   - Prompted to RESTART UE, please do so
<p align="center">
<img src="https://github.com/BlakeXYZ/Unreal-Engine-Python-Projects/assets/37947050/fb5a49d7-8d01-401b-b374-dde9c0c86146" width="700">
</p>

#### Upon Restart, your Main Menu should now contain a new Item which launches the _auto_material_instancer tool!

<p align="center">
<img src="https://github.com/BlakeXYZ/Unreal-Engine-Python-Projects/assets/37947050/c7d07bac-3a87-44b9-a9e1-884728bee34d" width="700">
</p>
</details>

____________

## <ins>Quick Start</ins>
<details>
<summary>Selected Master Material Requirements</summary>
            1. Your custom 'Import Parameter Group' is assigned to Param2D Material Expressions you wish to auto fill with imported Textures. 
   <br>
            2. Param2D Material Expression Texture Base must follow your custom SUFFIX PATTERN / Naming convention.
   <br>
   <br>

<p align="center">
<img src="https://github.com/BlakeXYZ/Unreal-Engine-Python-Projects/assets/37947050/dbdd326b-1a0b-4897-9eec-1e00bcbe36cb" width="700">
</p>
</details>
<details>
<summary>Selected Master Material Example image</summary>
<p align="center">
<img src="https://github.com/BlakeXYZ/Unreal-Engine-Python-Projects/assets/37947050/026c831c-2ad2-4d52-8d0f-2c971f5a64ea" width="700">
</p>
</details>
<details>
<summary>Selected Texture Files Requirements</summary>
           1. Texture File Names must contain a Suffix that matches one of the SUFFIX PATTERNS found in your Selected Master Material
   <br>
   <br>
<p align="center">
<img src="https://github.com/BlakeXYZ/Unreal-Engine-Python-Projects/assets/37947050/abbbfd15-4c0a-4267-8ece-8158bce98c02" width="700">
</p>
</details>

______
## <ins>Documentation</ins>

<details>
<summary>Debugging - Output Log</summary>
   
- **Please check Unreal Engine’s Output Log if the Tool is not working as expected.**
- **The tool will throw ‘ValidationError’ and ‘Warning’ alerts with context-specific explanations.**
```
LogPython: Error: utils.AutoMI_01_Load_Mat.ValidationError: Please select Asset of <class "Material">
-- Currently Selected Asset "Material_INSTANCE" is of <class 'MaterialInstanceConstant'>
```
```
LogPython: Warning: SKIPPING - Selected Texture File: "noMatchingSuffix_ORM" DOES NOT MATCH ANY SUFFIX PATTERNS.
Full file path: C:/Users/blake/Pictures/Textures/noMatchingSuffix_ORM.jpg
```

</details>

<details>
<summary>Tool Constraints</summary>

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
```



</details>


<details>
<summary>init_unreal .py</summary>
<br>
On Initialization we are running two important steps:
   
- **sys.path.append(libs_subdir)**
   - This sets up 3rd Party Python Library Dependencies (ex: PySide2, Unreal Stylesheet)
- **def build_menu()**
   - This builds an easy access Menu inside our LevelEditor.MainMenu, in which we can launch our Tool.
</details>

______


