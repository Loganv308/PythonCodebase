import os

"""
Author: Logan V
Date: 2023-09-05 (yyyy-mm-dd)
"""
"""
Description:
    The purpose of this file is to have re-occurring functions 
    that are used in multiple files and databases. 
"""


"""
    This is used to get the last row from the rows.cfg file.
    The file is generated from where the script left off reading through the database. 
"""
def get_last_row():  # This is getting the ROW value from the rows.cfg file. 
    try:
        if os.path.exists("Config/rows.cfg"):
            with open("Config/rows.cfg", "r") as f:
                line = f.readline().strip()
                value = line.split('=')[1].strip()
                return int(value)
        else:
            with open("Config/rows.cfg", "w") as f:
                f.write("0")
            return 0
    except Exception as e:
        print(f"Error while reading the file: {e}")


"""
    This is getting the INDEX value from the config.cfg file.
    It's used to determine where to start the next query.
"""
def get_last_index(): 
    
    file_path = "Config/config.cfg"  # Path to the config file

    lst = os.listdir(
        "Split_Data"
    )  # List of files in the Split_Data folder. Provides a way to check in the next line the amount of files split.

    num_split_files = len(
        lst
    )  # Number of split files in the Split_Data folder. Used to check if the file is empty or not.

    print(
        "Number of current split files:", num_split_files
    )  # Prints the number of split files. Used for debugging.

    # The code below is used to create the config file if it doesn't exist, and to read the last index from the file.
    # ---------------------------------------------- #
    try:  # Try to create the config file if it doesn't exist
        if (not os.path.exists(file_path)):  # If the file doesn't exist, creates the file and writes "0" to it
            with open(file_path, "w") as f:  # Open the file in write mode
                f.write("0")  # Write "0" to the file
            return 0  # Return 0 to indicate that the file was empty
        
        if(os.path.getsize(file_path) == 0 and num_split_files != 0):  # If the file is empty
            with open(file_path, "w") as f:  # Open the file in write mode
                f.write(num_split_files)  # Write the number of split files to the file
            return num_split_files 

    except Exception as e:  # If there's an error, print it
        print(f"Error while checking or creating the file: {e}")  # Print the error
        return None  # Return None to indicate an error

    try:
        # If the file exists and is not empty, read the last line
        with open(file_path, "r") as f:
            lines = f.readlines()
            if (
                num_split_files != 0
            ):  # This was the biggest pain in the cock to figure out. Fuck this loop in particular.
                return int(lines[-1].strip())
            else:
                # This block might be redundant since we already checked if the file is empty
                # However, keeping it to handle any unexpected scenarios
                with open(file_path, "w") as f:
                    f.write("0")
                return 0
    except Exception as e:
        print(f"Error while reading the file: {e}")
        return None
    # ---------------------------------------------- #