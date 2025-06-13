import pandas as pd
import sys  # TODO Tie this into the sys args
import headers as h
import save_chunk as sc
from utils import utils as u 

CHUNK_SIZE = 100_000  # Number of rows to read in at a time
HEADERS = []

def main():
    # Tie this into SYS ARGS eventually
    file_path = input("Database Filepath: ")  # Path to the csv file

    change_headers = input("Change headers? (y/n): ")  # Asks if the user wants to change the headers  
    
    df = pd.read_csv(
        file_path, chunksize=CHUNK_SIZE
    )  # Reads the csv file in chunks of 100,000 rows

    if change_headers.lower() == "y": # If the user wants to change the headers
        print("Current Headers:", h.get_column_names(df)) 
        user_input = input("Enter new headers separated by commas: ")  # Get the new headers from the user
        HEADERS = [header.strip() for header in user_input.split(",")]
        if len(HEADERS) != 0:
            print("Headers set to memory!")
    else:
        HEADERS = h.get_column_names(df)
    # print(
    #     "Headers: ", h.get_column_names(df)
    # )  # Get the column names. Passes the first chunk to get_column_names()

    index = u.get_last_index()  # Get the last index from the config.cfg file
    last_row = u.get_last_row()  # Get the last row from the rows.cfg file
    
    print("Last Row indexed:", last_row)
    
    for idx, chunk in enumerate(df):  # Loops through the chunks
        index += 1
        current_row = idx * CHUNK_SIZE # Increments the index by 1

        save_chunk = sc.save_chunk_to_csv(file_path, chunk, index, HEADERS)  # Saves the chunk to a csv file

        chunk_path = save_chunk[0]

        h.set_column_names(chunk_path, HEADERS)  # Sets the new headers for the chunk

        print("Current Row:", current_row)
        
        print(
            f"Saving chunk #{index} to csv..."
        )  # Prints the index of the chunk being saved
        #print(sc.save_chunk_to_csv(file_path, chunk, index)) 
        

    print("Done!")


if __name__ == "__main__":
    main()
