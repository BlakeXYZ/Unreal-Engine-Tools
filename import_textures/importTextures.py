import unreal
import sys, os
from functools import partial  # if you want to include args with UI method calls
from PySide2 import QtUiTools, QtWidgets, QtGui

import unreal_stylesheet

sys.path.append(rf'C:\Users\blake\Documents\Unreal Projects\blakeXYZ_UE_Utils')         # allow for import of custom modules "import viewport_utils.py 

"""
Be sure to add your default python modules directory path to Unreal:
Project Settings -> Python -> Additional Paths
    
Default location of installed modules:
C:\\Users\\blake\\AppData\\Local\\Programs\\Python\\Python39\\Lib\\site-packages
    
This code required PySide2 module which may need to be installed.
To install required modules open windows command prompt and enter:
pip install [MODULENAME]

"""

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
                ui_dir = os.path.join(script_dir, 'importTextures.ui')
                self.subWidget_filePath_ui_dir = os.path.join(script_dir, 'importTextures_subWidget_filePath.ui') # load SubWidget and add self. to be callable in Functions


                #load the created UI widget
                self.mainWidget = QtUiTools.QUiLoader().load(ui_dir)
	      
                #attach the widget to the instance of this class (aka self)
                self.mainWidget.setParent(self)

                #find interactive elements of UI
                self.btn_openFiles = self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_openFiles')
                self.gridLayout_filePaths = self.mainWidget.findChild(QtWidgets.QGridLayout, 'gridLayout_filePath')
                self.btn_close = self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_closeWindow')
                self.textEdit_consoleLog = self.mainWidget.findChild(QtWidgets.QTextEdit, 'textEdit_consoleLog')
                self.btn_clearConsole =  self.mainWidget.findChild(QtWidgets.QPushButton, 'btn_clearConsole')


                #assign clicked handler to buttons
                self.btn_openFiles.clicked.connect(self.appendFiles)
                self.btn_close.clicked.connect(self.closewindow)
                self.btn_clearConsole.clicked.connect(self.clear_consoleLog_text) 

                # List to ensure no DUPLICATES get added
                self.stored_fileNames = []  # Initialize the list here

                # Setup for Dynamic Grid / Flow Layou
                self.column = 0
                self.row = 1
                self.max_columns = 4  # Maximum number of columns
                self.stored_gridWidgets = []  # Store added item widgets



        """
        Your code goes here.
        """

        def appendFiles(self):
                """
                Work with QFileDialog
                """
                current_consoleLog =  self.textEdit_consoleLog.toHtml()
                # self.textEdit_consoleLog.setHtml(f'{current_consoleLog} hello')


                dir = rf'C:\Users\blake\Pictures\Wallpaper'
                fileNames = QtWidgets.QFileDialog.getOpenFileNames(self, ("Open Image"), dir, ("Image Files (*.png *.jpg *.psd)")) # returns tuple: ( [ list of file paths], your filter: 'Image Files (*.png *.jpg *.bmp)')

                for fileName in fileNames[0]:
                        if fileName in self.stored_fileNames: # LOG & CONTINUE if duplicates in self.stored_fileNames list
                                current_consoleLog =  self.textEdit_consoleLog.toHtml()
                                self.textEdit_consoleLog.setHtml(f'{current_consoleLog}Warning: {fileName} is already selected!')
                                continue


                # Only allow if no Duplicates are in stored list
                        self.stored_fileNames.append(fileName)

                        #load the created UI widget
                        subWidget_filePath = QtUiTools.QUiLoader().load(self.subWidget_filePath_ui_dir)

                # Add subwidget to mainWidget's QGridLayout (mainWidget.gridLayout_filePath) 
                        self.gridLayout_filePaths.addWidget(subWidget_filePath, self.row, self.column)

                        #find interactive elements of subwidget UI
                        lineEdit_filePath = subWidget_filePath.findChild(QtWidgets.QLineEdit, 'lineEdit_filePath')
                        img_filePath = subWidget_filePath.findChild(QtWidgets.QLabel, 'img_filePath')
                        btn_filePath_remove = subWidget_filePath.findChild(QtWidgets.QPushButton, 'btn_filePath_remove')

                        # connect btn to remove filePath widget
                        btn_filePath_remove.clicked.connect(partial(self.remove_subWidget, subWidget_filePath)) # Feed in Method then Argument

                # Add Filename to Subwidget's Object: LineEdit
                        lineEdit_filePath.setText(fileName)
                        # Create a QPixmap from the file
                        pixmap = QtGui.QPixmap(fileName)
                        # Set Pixmap property in QLabel Object named 'img_filePath'
                        img_filePath.setPixmap(pixmap)


                #store gridWidgets into List to rearrange later on
                        self.stored_gridWidgets.append(subWidget_filePath)

                        self.column += 1
                        if self.column >= self.max_columns:
                                self.column = 0
                                self.row += 1

                        self.UTILITY_reorganize_gridLayout()

                self.UTILITY_move_consoleLog_cursor_to_end()
        

        def remove_subWidget(self, my_subwidget):
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


        def clear_consoleLog_text(self):
                self.textEdit_consoleLog.setHtml(f'Console Log...')

                # Set the desired color using CSS style
                color = "#715101" 
                colored_text = f'<span style="color: {color};">Console Log...</span>'
                
                self.textEdit_consoleLog.setHtml(colored_text)


     # Ensure the latest text is visible at the bottom
        def UTILITY_move_consoleLog_cursor_to_end(self):
                cursor = self.textEdit_consoleLog.textCursor()
                cursor.movePosition(cursor.End)
                self.textEdit_consoleLog.setTextCursor(cursor)
                self.textEdit_consoleLog.ensureCursorVisible()


        def resizeEvent(self, event):
                """
                Called on automatically generated resize event
                """
                self.mainWidget.resize(self.width(), self.height())
        
        def closewindow(self):
                """
                Close the window.
                """
                self.destroy()
                
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