import os
import glob
import sys

# Check for correct number of arguments
if len(sys.argv) != 4:
    print("Usage: python script.py <folder_path> <file_type> <slice_index>")
    sys.exit(1)

folder_path = sys.argv[1]  # Folder path passed as argument
file_type = sys.argv[2]    # File type passed as argument
slice_index = int(sys.argv[3])  # Slice index passed as argument

# Change to the provided folder path
os.chdir(folder_path)

# Loop through all files of the given file type
for file in glob.glob(f"*.{file_type}"):
    file_name = os.path.splitext(file)[0]
    extension = os.path.splitext(file)[1]
    
    # Apply slicing based on provided index
    new_file_name = f"{file_name[:-slice_index]}{extension}"
    
    try:
        os.rename(file, new_file_name)
    except OSError as e:
        print(f"Error renaming {file}: {e}")
    else:
        print(f"Renamed {file} to {new_file_name}")
