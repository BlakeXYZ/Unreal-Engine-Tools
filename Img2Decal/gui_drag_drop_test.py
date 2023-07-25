import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidget, QPushButton
from PyQt5.uic import loadUi

class listWidget(QListWidget):
    def __init__(self, parent=None):
        super(listWidget, self).__init__(parent)
        self.setAcceptDrops(True)
        self.setSelectionMode(QListWidget.ExtendedSelection)  # Enable multi-item selection
        self.setSelectionBehavior(QListWidget.SelectItems)    # Select the entire row when an item is clicked

        self.Stored_Image_Dir_Paths = []  # Initialize the list here

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.setDropAction(Qt.CopyAction)
            urls = event.mimeData().urls()

            selected_image_dir_paths = []

            for url in urls:
                if url.isLocalFile():
                    file_path = str(url.toLocalFile())
                    if file_path not in self.Stored_Image_Dir_Paths:  # Check for duplicates in self.Image_Dir_Paths
                        selected_image_dir_paths.append(file_path)
                        self.Stored_Image_Dir_Paths.append(file_path)
                    else:
                        event.ignore()

            self.addItems(selected_image_dir_paths)

    def removeSelectedItems(self):
        selected_items = self.selectedItems()
        if not selected_items:
            return

        for item in selected_items:
            path = item.text()
            self.Stored_Image_Dir_Paths.remove(path)
            self.takeItem(self.row(item))


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
        self.my_pushButton.clicked.connect(self.my_listWidget.removeSelectedItems)


 




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = mainWidget()
    window.show()
    app.exec_()
