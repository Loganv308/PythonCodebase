import pandas as pd

def set_column_names(file_path, new_headers):
    # Read the CSV file into a pandas DataFrame.
    df = pd.read_csv(file_path)
    
    # Set the new headers.
    df.columns = new_headers 

    df.to_csv(file_path, index=False) # Save the DataFrame to a CSV file.

    return 
    
def get_column_names(file_path):
    # Get only the first chunk
    first_chunk = next(file_path)
    
    # Returns a list of the column names
    return first_chunk.columns.tolist()