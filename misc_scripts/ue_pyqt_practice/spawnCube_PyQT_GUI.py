 
import unreal
import sys, os
from functools import partial  # if you want to include args with UI method calls
from PySide2 import QtUiTools, QtWidgets

import unreal_stylesheet

sys.path.append(rf'C:\Users\blake\Documents\Unreal Projects\blakeXYZ_UE_Py_Utils')         # allow for import of custom modules "import viewport_utils.py"

class UnrealUITemplate(QtWidgets.QWidget):
        """
        Create a default tool window.
        """
        # store ref to window to prevent garbage collection
        window = None
        def __init__(self, parent = None):
                """
                Import UI and connect components
                """
                super(UnrealUITemplate, self).__init__(parent)
                        
                # Get the directory where the script is located
                script_dir = os.path.dirname(os.path.abspath(__file__))
                ui_dir = os.path.join(script_dir, 'PyQT_GUI_example.ui')
                #load the created UI widget
                self.widget = QtUiTools.QUiLoader().load(ui_dir)
	      
                #attach the widget to the instance of this class (aka self)
                self.widget.setParent(self)

                #find interactive elements of UI
                self.btn_spawnCube = self.findChild(QtWidgets.QPushButton, 'btn_spawnCube')
                self.btn_printActors = self.findChild(QtWidgets.QPushButton, 'btn_printActors')
                self.btn_close = self.findChild(QtWidgets.QPushButton, 'btn_closeWindow')
                self.X_rot = self.findChild(QtWidgets.QSpinBox, 'spinBox_X_rot_value')
                self.Y_rot = self.findChild(QtWidgets.QSpinBox, 'spinBox_Y_rot_value')
                self.Z_rot = self.findChild(QtWidgets.QSpinBox, 'spinBox_Z_rot_value')
 

                #assign clicked handler to buttons
                self.btn_spawnCube.clicked.connect(self.spawn_cube)
                self.btn_printActors.clicked.connect(self.printActors)
                self.btn_close.clicked.connect(self.closewindow)


        """
        Your code goes here.
        """
        def spawn_cube(self):
                import viewport_utils 

                my_rot_values = (self.X_rot.value(), self.Y_rot.value(), self.Z_rot.value())
                print(my_rot_values)

                # print("Current working directory:", os.getcwd())
                # print("Python's sys.path:")
                # for path in sys.path:
                #  print(path)

                viewport_utils.spawn_cube(my_rot_values)
        
                

        def printActors(self):
                """
                Print all Level Actors
                """

                import viewport_utils 
                viewport_utils.print_all_level_actors()



        def resizeEvent(self, event):
                """
                Called on automatically generated resize event
                """
                self.widget.resize(self.width(), self.height())
        
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
        
        UnrealUITemplate.window = UnrealUITemplate()
        UnrealUITemplate.window.show()
        UnrealUITemplate.window.setObjectName('toolWindow') # update this with something unique to your tool
        UnrealUITemplate.window.setWindowTitle('Sample Tool')
        unreal.parent_external_window_to_slate(UnrealUITemplate.window.winId())
        
openWindow()