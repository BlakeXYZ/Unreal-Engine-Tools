import unreal
import sys, os, importlib     
from typing import List                   
from functools import partial  # if you want to include args with UI method calls

from PySide2 import QtUiTools, QtWidgets, QtGui

import unreal_stylesheet

# allow for import of custom python scripts
script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(script_dir)                                     

class ValidationError(Exception):
    pass


class my_importTextures_GUI(QtWidgets.QWidget):
        """
        Create a default tool window.
        """
        # store ref to window to prevent garbage collection
        window = None
        def __init__(self, parent = None):
                """
                Import UI and connect components
                """
                super(my_importTextures_GUI, self).__init__(parent)
                        
                # Get the directory where the script is located
                script_dir = os.path.dirname(os.path.abspath(__file__))
                ui_dir = os.path.join(script_dir, 'material_instancer.ui')
                self.subWidget_filePath_ui_dir = os.path.join(script_dir, 'material_instancer_subWidget_filePath.ui') # load SubWidget and add self. to be callable in Functions


                #load the created UI widget
                self.mainWidget = QtUiTools.QUiLoader().load(ui_dir)
	      
                #attach the widget to the instance of this class (aka self)
                self.mainWidget.setParent(self)

                ###
                ###
                #find interactive elements of UI
                self.btn_get_single_selected_material = self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_get_single_selected_material')
                self.lineEdit_loaded_material_name = self.mainWidget.findChild(QtWidgets.QLineEdit, 'lineEdit_loaded_material_name')
                self.comboBox_LIST_all_matExpression_paramGroups = self.mainWidget.findChild(QtWidgets.QComboBox, 'comboBox_LIST_all_matExpression_paramGroups')

                self.btn_select_texture_files = self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_select_texture_files')
                self.gridLayout_filePaths = self.mainWidget.findChild(QtWidgets.QGridLayout, 'gridLayout_filePath')

                self.btn_build_material_instance =  self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_build_material_instance')
                self.btn_close = self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_closeWindow')

                ###
                ###
                #assign clicked handler to buttons
                self.btn_get_single_selected_material.clicked.connect(self.get_single_selected_material)
                self.comboBox_LIST_all_matExpression_paramGroups.activated.connect(self.filter_matExpressions_by_user_selected_paramGroup)

                self.btn_select_texture_files.clicked.connect(self.select_texture_files)

                self.btn_build_material_instance.clicked.connect(self.build_material_instance)
                self.btn_close.clicked.connect(self.close_window)

                ###
                ###
                # List to ensure no DUPLICATES get added
                self.stored_fileNames = []  # Initialize the list here
                # update button state
                self.UTILITY_btn_build_material_instance_state()

                # Setup for Dynamic Grid / Flow Layou
                self.column = 0
                self.row = 1
                self.max_columns = 4  # Maximum number of columns
                self.stored_gridWidgets = []  # Store added item widgets


        """

        GUI Interaction Functions

        """

        def select_texture_files(self):
                """
                Work with QFileDialog
                """

                # QFileDialog file type filter
                accepted_QFileDialog_fileTypes = ['*.bmp', '*.float', '*.jpeg', '*.jpg', '*.pcx', '*.png', '*.psd', '*.tga', '*.dds', '*.exr', '*.tif', '*.tiff']
                my_QFileDialog_filter = f"Image Files ({' '.join(accepted_QFileDialog_fileTypes)})"
                filePaths = QtWidgets.QFileDialog.getOpenFileNames(self, ("Select Files to Import"), '', my_QFileDialog_filter) # returns tuple: ( [ list of file paths], your filter: 'Image Files (*.png *.jpg *.bmp)')

                for filePath in filePaths[0]: # fileNames is a tuple where the first element is the list of file paths

                        ###### TODO: compare fileName suffixes to self.DICT_all_textures_suffixes
                        ##
                        ##

                        # Get the base filename (without directory)
                        baseFileName = os.path.basename(filePath)
                        # Remove the file extension
                        fileNameWithoutExtension, _ = os.path.splitext(baseFileName)
                        
                        print(fileNameWithoutExtension)
                        print(filePath)

                        ##
                        ##
                        ######



                        if filePath in self.stored_fileNames: # LOG & CONTINUE if duplicates in self.stored_fileNames list
                                unreal.log(f'{filePath} is already selected!')
                                continue

                # IF CHECKS PASS: append 'fileName' to stored_fileNames list
                        self.stored_fileNames.append(filePath)

                # update button state
                        self.UTILITY_btn_build_material_instance_state()

                        #load the created UI widget
                        subWidget_filePath = QtUiTools.QUiLoader().load(self.subWidget_filePath_ui_dir)

                # Add subwidget to mainWidget's QGridLayout (mainWidget.gridLayout_filePath) 
                        self.gridLayout_filePaths.addWidget(subWidget_filePath, self.row, self.column)

                        #find interactive elements of subwidget UI
                        lineEdit_filePath = subWidget_filePath.findChild(QtWidgets.QLineEdit, 'lineEdit_filePath')
                        img_filePath = subWidget_filePath.findChild(QtWidgets.QLabel, 'img_filePath')
                        btn_filePath_remove = subWidget_filePath.findChild(QtWidgets.QPushButton, 'btn_filePath_remove')

                        # connect btn to remove subWidget_filePath
                        btn_filePath_remove.clicked.connect(partial(self.remove_subWidget, subWidget_filePath)) # Using library: Partial to Feed in Method then Argument

                # Add Filename to Subwidget's Object: LineEdit
                        lineEdit_filePath.setText(filePath)
                        # Create a QPixmap from the file
                        pixmap = QtGui.QPixmap(filePath)
                        # Set Pixmap property in QLabel Object named 'img_filePath'
                        img_filePath.setPixmap(pixmap)


                #store gridWidgets into List to rearrange later on
                        self.stored_gridWidgets.append(subWidget_filePath)

                        self.column += 1
                        if self.column >= self.max_columns:
                                self.column = 0
                                self.row += 1

                        self.UTILITY_reorganize_gridLayout()
        

        def remove_subWidget(self, my_subwidget):

                # Remove fileName in stored_fileNames list
                lineEdit_filePath = my_subwidget.findChild(QtWidgets.QLineEdit, 'lineEdit_filePath')
                if lineEdit_filePath.text() in self.stored_fileNames:
                        self.stored_fileNames.remove(lineEdit_filePath.text())

                # Remove sub widget from main window
                self.gridLayout_filePaths.removeWidget(my_subwidget)
                my_subwidget.deleteLater()

                # Remove the widget from the item_widgets list
                self.stored_gridWidgets.remove(my_subwidget)

                # Reorganize the layout after removing an item
                self.UTILITY_reorganize_gridLayout()
                
                # update button state
                self.UTILITY_btn_build_material_instance_state()


        def UTILITY_reorganize_gridLayout(self):
                """
                 reorganizes the grid layout by iterating through the stored widgets, 
                 determining their new row and column positions based on the index, 
                 and then adjusting the row count if necessary to ensure the layout appears correctly with the specified number of columns.
                """
                for index, widget in enumerate(self.stored_gridWidgets):
                        row = index // self.max_columns
                        column = index % self.max_columns
                        self.gridLayout_filePaths.addWidget(widget, row, column)

                if len(self.stored_gridWidgets) % self.max_columns == 0:
                        self.row -= 1

                self.gridLayout_filePaths.update()


        ### UX Assembly Line function, ensures step by step experience
        # Checks if Current Combo Box text == a Param Group in Material
        def UTILITY_btn_select_texture_files_state(self):
                if self.comboBox_LIST_all_matExpression_paramGroups.currentText() in self.LIST_all_matExpression_paramGroups:
                        self.btn_select_texture_files.setEnabled(True)
                else:
                        self.btn_select_texture_files.setEnabled(False)

        
        ### UX Assembly Line function, ensures step by step experience
        # Checks if list of 'stored_fileNames' is not zero
        def UTILITY_btn_build_material_instance_state(self):
                if len(self.stored_fileNames) == 0:
                        self.btn_build_material_instance.setEnabled(False)
                else:
                        self.btn_build_material_instance.setEnabled(True)

                ## TIP: how to see properties of a widget: QtWidgets.QPushButton.setEnabled()



        def resizeEvent(self, event):
                """
                Called on automatically generated resize event
                """
                self.mainWidget.resize(self.width(), self.height())
        

        def close_window(self):
                """
                Close the window.
                """
                self.destroy()
                

        """

        Connect Logic to GUI

        """
        # AutoMI_01_Load_Mat
        def get_single_selected_material(self):

                import AutoMI_01_Load_Mat
                importlib.reload(AutoMI_01_Load_Mat)           # Reloads imported .py file, without, edits to this imported file will not carry over

                self.single_selected_material = AutoMI_01_Load_Mat.get_single_selected_material()

                ###
                # Call TexParamData Class and Store selected Material's "all_texture_paramGroups" + "all_textures"
                inst_TexParamData = AutoMI_01_Load_Mat.TexParamData(self.single_selected_material.get_path_name())
                self.LIST_all_matExpression_paramGroups =   inst_TexParamData.return_LIST_all_matExpression_paramGroups()
                self.LIST_all_matExpressions =              inst_TexParamData.return_LIST_all_matExpressions()
                #
                ###

                print(f'TOTAL TEXTURE COUNT: {len(self.LIST_all_matExpressions)}')

                self.lineEdit_loaded_material_name.setText(self.single_selected_material.get_name())
                self.comboBox_LIST_all_matExpression_paramGroups.clear()
                self.comboBox_LIST_all_matExpression_paramGroups.addItem('-- Select Group --')
                self.comboBox_LIST_all_matExpression_paramGroups.addItems(self.LIST_all_matExpression_paramGroups)

                self.UTILITY_btn_select_texture_files_state()



        # AutoMI_02_Load_ParamGroup
        def filter_matExpressions_by_user_selected_paramGroup(self):

                import AutoMI_02_Load_ParamGroup
                importlib.reload(AutoMI_02_Load_ParamGroup)           # Reloads imported .py file, without, edits to this imported file will not carry over

                ###
                # Call LoadParamGroup Class and return 'all_filtered_matExpressions' and 'all_textures_suffixes'
                inst_LoadParamGroup = AutoMI_02_Load_ParamGroup.LoadParamGroup(self.LIST_all_matExpressions, self.comboBox_LIST_all_matExpression_paramGroups.currentText(),  self.single_selected_material)
                self.LIST_all_filtered_matExpressions, \
                self.DICT_all_textures_suffixes = inst_LoadParamGroup.filter_matExpressions_by_user_selected_paramGroup()
                #
                ##

                # For Each matExpression print out it's Texture's Name and Suffix
                for matExpression in self.LIST_all_filtered_matExpressions:
                        print(matExpression.get_editor_property("texture").get_name())
                        print(self.DICT_all_textures_suffixes[matExpression])

              

                # Change State of 'select_texture_files' button - continue on in UX Assembly Line
                self.UTILITY_btn_select_texture_files_state()



        # AutoMI_04_Build_MI
        def build_material_instance(self):

                import AutoMI_04_Build_MI
                importlib.reload(AutoMI_04_Build_MI)           # Reloads imported .py file, without, edits to this imported file will not carry over

                destination_path = unreal.EditorUtilityLibrary.get_current_content_browser_path()
                file_names = self.stored_fileNames

                AutoMI_04_Build_MI.import_files(file_names, destination_path)

                unreal.log(f'Successfully Imported to Path: {destination_path}')










def openWindow():
        """
        Create tool window.
        """
        if QtWidgets.QApplication.instance():
                # Id any current instances of tool and destroy
                for win in (QtWidgets.QApplication.allWindows()):
                        if 'toolWindow' in win.objectName(): # update this name to match name below
                                win.destroy()
        else:
                QtWidgets.QApplication(sys.argv)
        
        # load UI into QApp instance

        # style your QApp, requires a QApplication instance
        unreal_stylesheet.setup()  # <== Just 1 line of code to make the magic happen
        
        my_importTextures_GUI.window = my_importTextures_GUI() # create instance
        my_importTextures_GUI.window.show()
        my_importTextures_GUI.window.setObjectName('toolWindow') # update this with something unique to your tool
        my_importTextures_GUI.window.setWindowTitle('my_importTextures_GUI')
        unreal.parent_external_window_to_slate(my_importTextures_GUI.window.winId())
        
openWindow()