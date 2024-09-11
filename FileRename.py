import os
import shutil
from tkinter import Tk
from tkinter import filedialog

# Function to open file explorer and select multiple files
def select_files():
    root = Tk()
    root.withdraw()   
    file_paths = filedialog.askopenfilenames(title="Select Files")
    root.destroy()  
    return file_paths

# Step 1: Open file explorer and select files
file_paths = select_files()

# Step 2: Generate names (or custom ranges)
start_num = int(input("Enter starting number"))
end_num = int(input("Enter ending number")) 
names = [str(num).zfill(5) for num in range(start_num, end_num + 1)]

# Ensure that we have enough names for the selected files
if len(file_paths) > len(names):
    raise ValueError(f"Selected more files ({len(file_paths)}) than available names ({len(names)})!")

# Step 3: Define the main folder where the renamed files will be moved

main_folder = r'C:\Users\Username\Replace with your path name'

# Step 4: Iterate over the files and rename them
for idx, file_path in enumerate(file_paths):
    try:
        # Extract the current file extension
        _, file_extension = os.path.splitext(file_path)  # Get the file extension like '.jpg'

        # Get the corresponding name from the list
        new_filename = f"{names[idx]}{file_extension}"  # e.g., '00001.jpg'

        # Full new file path
        new_file_path = os.path.join(main_folder, new_filename)

        # Step 5: Rename the file and move it to the main folder
        shutil.move(file_path, new_file_path)

        print(f"Renamed '{file_path}' to '{new_file_path}'")

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
