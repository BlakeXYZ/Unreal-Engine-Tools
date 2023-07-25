# rembg i path/to/input.png path/to/output.png
# rembg i C:\Users\blake\Documents\PYTHON_Scripting\2023\07-22-2023__Rembg_Image\input\test_01.jpg C:\Users\blake\Documents\PYTHON_Scripting\2023\07-22-2023__Rembg_Image\output\test_output_01.png

import subprocess, sys


def call_rembg_script_inside_py39env():

    venv_path = r"C:\Users\blake\Documents\PYTHON_Scripting\2023\07-22-2023__Rembg_Image\py39env"
    activate_cmd = rf"{venv_path}\Scripts\activate && py C:\Users\blake\Documents\PYTHON_Scripting\2023\07-22-2023__Rembg_Image\cleanup_image.py"
    result = subprocess.run(activate_cmd, shell=True)

   # Check the result
    if result.returncode == 0:
        print("Virtual environment activated successfully and code complete")
    else:
        print("Failed to activate virtual environment.")


# Call the function to perform the task
if __name__ == "__main__":
    call_rembg_script_inside_py39env()
