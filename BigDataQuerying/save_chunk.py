import os
import headers as h

def save_chunk_to_csv(database, chunk, index, headers):
    database = os.path.basename(
        os.path.realpath(database)
    )  # Gets the name of the database file. 

    save_path = f"{database}_#{index}.csv"  # Path to the folder where the split files will be saved

    chunk.columns = headers

    chunk.to_csv(rf"{save_path}", index=False)

    open("Config/config.cfg", "w").write(
        str(index)
    )  # Writes the index to the config file

    # Returns the index of the last file saved
    return save_path, index