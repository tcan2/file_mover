import os
import shutil

# This is our function to move files from source directory to destination directory based on a keyword
def move_files(source_directory, dest_directory, keyword):
    # This will iterate over files in whatever source directory is given
    for item in os.listdir(source_directory):
        # This gets the path to the item so the program can continue whether its a pdf, subfolder, or anything else
        item_path = os.path.join(source_directory, item)
        
        # This checks if the item is a file
        if os.path.isfile(item_path):
            # If it is a file, this checks if the keyword is in the filename
            if keyword in item:
                # Move/Copy the file to the destination directory. You can change what you want it to do
                shutil.copy(item_path, dest_directory)
                # Print if a file was moved/copied
                print(f"Copied {item} to {dest_directory}")
        
        # If it is not a file, check if it is a subfolder/directory
        elif os.path.isdir(item_path):
            # Then run the function again to recursively search the subfolder
            move_files(item_path, dest_directory, keyword)

# Function to get inputs and run file movement
def main():
    # Get source directory path from user input
    source_directory = input("Enter the source directory path: ")
    # Get destination directory path from user input
    dest_directory = input("Enter the destination directory path: ")
    # Get keyword from user input
    keyword = input("Enter the keyword to search for: ")
    # Running the code!
    move_files(source_directory, dest_directory, keyword)

# Running the main function
main()
