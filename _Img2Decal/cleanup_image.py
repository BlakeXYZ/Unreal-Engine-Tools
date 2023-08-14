## Pyqt5
import typing
from PyQt5 import QtCore
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.uic import loadUi
import sys
##
try: # Try to import the 'rembg' module
    from rembg import remove
except ModuleNotFoundError as e:
    # If the 'rembg' module is not found, handle the error here
    print("Warning: The 'rembg' module is not installed. Background removal functionality will not be available.")
from PIL import Image as pillow_image
import glob

# TODO: Check for file format, convert all in Output Dir to USER SELECTION -- (.png or .tga)

class mainWidget(QMainWindow): #Class that Inherits from QMainWindow
    def __init__(self): # Init func gets executed when you create Instance of Class
        super(mainWidget, self).__init__() # Initialize QMainWindow 
        loadUi('cleanup_image.ui', self) # Load UI inside this class


####################################################################################################################

file_format = 'png'

# Batch Remove Background Using Library: rembg
def remove_background():
        
    input_path = rf'C:\Users\blake\Documents\PYTHON_Scripting\2023\07-22-2023__Rembg_Image\input'
    output_path = rf'C:\Users\blake\Documents\PYTHON_Scripting\2023\07-22-2023__Rembg_Image\output'
    file_pattern = '*.*'  # This will match all files regardless of their extension. You can adjust the pattern as needed.

    # Use glob to get all files matching the pattern in the specified directory
    file_list = glob.glob(rf'{input_path}\{file_pattern}')

    for file in file_list:
    # Extract the file name from the input file path
        file_name = file.split('\\')[-1]
    # Split the file name based on the last period (.) and replace the part after it with "_output.png"
        output_file_name = file_name.rsplit('.', maxsplit=1)[0] + f'_output.{file_format}'
    # Build the output file path by replacing "input" with "output" and changing the file extension to "png"
        output_file_path = rf"{output_path}\{output_file_name}"

        print(f'Processing.... {file_name}')

    # Handle broken images
        try:
            input = pillow_image.open(file)
            output = remove(input)
            output.save(output_file_path)

        except Exception as e:
            # Handle the specific exception here (e.g., IOError, ValueError)
            # You can log the error or take appropriate action
            print(f"An error occurred while processing the image: {e}")


def resize_canvas_to_1x1_ratio():

    output_path = rf'C:\Users\blake\Documents\PYTHON_Scripting\2023\07-22-2023__Rembg_Image\output'
    file_pattern = '*.*'  # This will match all files regardless of their extension. You can adjust the pattern as needed.
    file_list = glob.glob(rf'{output_path}\{file_pattern}') # Use glob to get all files matching the pattern in the specified directory

    for file in file_list:
        input_image = pillow_image.open(file)
    # Determine size of square canvas
        canvas_size = max(input_image.size) 
    # create a new square canvas with transparent background
        canvas = pillow_image.new('RGBA', (canvas_size, canvas_size), (0,0,0,0)) 
    # Calculate the position to paste the image at the center of the canvas
        paste_position = ((canvas_size - input_image.width) // 2, (canvas_size - input_image.height) // 2) 
    # Paste the original image onto the canvas
        canvas.paste(input_image, paste_position) 
        canvas.save(file)

        # Get the dimensions (width and height) of the image
        input_image = pillow_image.open(file)
        width, height = input_image.size
        print(f"Image width: {width} -- Image height: {height}")

####################################################################################################################


if __name__ == "__main__":          # execute application
    app = QApplication(sys.argv)    # 
    window = mainWidget()           # create instance of class mainWidget
    window.show()                   # show on screen
    app.exec_()


    # remove_background()
    # resize_canvas_to_1x1_ratio()
