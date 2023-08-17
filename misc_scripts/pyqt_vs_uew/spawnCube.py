 
import unreal
import sys, os
from functools import partial  # if you want to include args with UI method calls
from PySide2 import QtUiTools, QtWidgets

import unreal_stylesheet

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
                ui_dir = os.path.join(script_dir, 'spawnCube.ui')
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


        def spawn_cube(self):
                my_rot_values = (self.X_rot.value(), self.Y_rot.value(), self.Z_rot.value())
                print(f'Cube Spawned with Rotation: {my_rot_values}')

                location = unreal.Vector()
                rotation = unreal.Rotator(*my_rot_values) # use '*' Operator to unpack my_rot_values tuple and pass elements in as arguments

                # Get the System to Control the Actors
                editor_actor_subs = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)

                # We want to create a StaticMeshActor
                actor_class = unreal.StaticMeshActor

                # Place it in the level
                static_mesh_actor =  editor_actor_subs.spawn_actor_from_class(actor_class, location, rotation)

                # Load and add cube to it
                static_mesh = unreal.EditorAssetLibrary.load_asset("/Engine/BasicShapes/Cube")
                static_mesh_actor.static_mesh_component.set_static_mesh(static_mesh)



        def printActors(self):
                """
                Print all Level Actors
                """

                for actor in unreal.EditorActorSubsystem().get_all_level_actors():
                        print(actor.get_actor_label())
                        


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