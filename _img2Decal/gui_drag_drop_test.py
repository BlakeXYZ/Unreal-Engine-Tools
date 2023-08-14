import sys, os
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QPushButton, QTextEdit, QLabel, QVBoxLayout
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.uic import loadUi

class listWidget(QListWidget):
    def __init__(self, parent=None):
        super(listWidget, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setSelectionMode(QListWidget.ExtendedSelection)  # Enable multi-item selection
        self.setSelectionBehavior(QListWidget.SelectItems)    # Select the entire row when an item is clicked

        self.Stored_Image_Dir_Paths = []  # Initialize the list here

        self.accepted_file_type_list = ['.png', '.jpg']



    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):

        select_user_consoleLog_Widget = self.parent().parent().findChild(QTextEdit, "user_consoleLog_Widget") # Select Aunt / Uncle which = user_consoleLog_Widget

        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            urls = event.mimeData().urls()

            for url in urls:
                if url.isLocalFile():
                    file_path = str(url.toLocalFile())
                    shortened_filepath = os.path.basename(file_path)
                    print(file_path)
                    if file_path not in self.Stored_Image_Dir_Paths:                # Check for duplicates in self.Image_Dir_Paths
                        if file_path.endswith(tuple(self.accepted_file_type_list)): # Only allow certain file type (look thru custom list)
                                                    
                            self.Stored_Image_Dir_Paths.append(file_path)                       # Store Images

                            icon = QtGui.QIcon(file_path)                                       # Create QIcon
                            icon_and_file_path = QtWidgets.QListWidgetItem(icon, file_path)     # Create the row with Icon + Text
                            self.setIconSize(QtCore.QSize(75, 75))                              # Set the size of the icons in the list widget

                            self.addItem(icon_and_file_path)                                    # Add Item (icon_and_file_path)

                        #  else if incorrect bFile Type' print inside user_consoleLog_Widget
                        else: 
                            # Get the current content of the widget
                            current_log = select_user_consoleLog_Widget.toHtml()
                            # Print Out on User Console Log
                            formatted_accepted_file_types = ', '.join(self.accepted_file_type_list)
                            file_type_log_01 = f'{current_log}{shortened_filepath} not accepted! -- Please use "{formatted_accepted_file_types}" file types'

                            ## ADD output_text string into "myOutputText" Widget
                            select_user_consoleLog_Widget.setHtml(file_type_log_01)
                            event.ignore()

                    # else if Duplicate is Present .... file_path is inside self.Stored_Image_Dir_Paths:  
                    else:
                        # Get the current content of the widget
                        current_log = select_user_consoleLog_Widget.toHtml()
                        file_duplicate_log_01 = f'{current_log}{shortened_filepath} is already selected!'
                        ## ADD output_text string into "myOutputText" Widget
                        select_user_consoleLog_Widget.setHtml(file_duplicate_log_01)
                        event.ignore()
        else:
            event.ignore()

    def removeSelectedItems(self):
        selected_items = self.selectedItems()
        if not selected_items:
            return

        for item in selected_items:
            path = item.text()
            self.Stored_Image_Dir_Paths.remove(path)    # Remove From Custom Stored List
            self.takeItem(self.row(item))               # Remove From Q List Widget


class mainWidget(QMainWindow):
    def __init__(self):
        super(mainWidget, self).__init__()
        loadUi('gui_drag_drop_test.ui', self)
        self.setWindowTitle("gui_drag_drop_test")

        # create instance of listWidget as an instance variable
        self.my_listWidget = listWidget()
        # Add the custom widget to the groupBox (listWidget_Container)
        self.listWidget_Container.layout().addWidget(self.my_listWidget)

        # Register Search button to removeSelectedItems method
        self.my_remove_selected_Button.clicked.connect(self.my_listWidget.removeSelectedItems)

        # my_clear_console_Button
        self.my_clear_console_Button.clicked.connect(self.__clear_console)

    def __clear_console(self):                                                                   ## RESET BUTTON
        self.user_consoleLog_Widget.clear()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWidget()
    window.show()
    app.exec_()
