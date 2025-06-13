import base64
import os


def base64_decode(data):
    try:
        # Ensure that the length of the data is a multiple of 4 by padding if needed

        decoded_data = base64.b64decode(data).decode('utf-8')
        return decoded_data
    except Exception as e:
        print(f"Error during base64 decoding: {e}")
        return None

def get_File_Extension(file_name):
    file_extension = os.path.splitext(file_name)[1]
    return file_extension

def traverse_directory(directory):
    filePaths = []
    folderPaths = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    # Process the file content if needed
                    # Example: content = f.read()
                    pass
            except UnicodeDecodeError:
                print(f"Unable to decode file: {file_path}")
            filePaths.append(file_path)
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            folderPaths.append(dir_path)
    return filePaths, folderPaths

def getFileStructure():
    file_path = input("Enter the file path: ")
    file_paths, folder_paths = traverse_directory(file_path)
    return file_paths, folder_paths


def main():
    file_paths, folder_paths = getFileStructure()

    for x in file_paths:
        print("File Path:", x)
        with open(x, "rb+") as f:
            file_ext = get_File_Extension(x)
            for line in f:
                decoded_data = base64_decode(line)
                
                if decoded_data is None:
                # Write the decoded data to a new file
                    output_file_path = x + f"_Failed_decode{file_ext}"
                    try:
                        with open(output_file_path, "w") as output_file:
                            output_file.write(decoded_data)
                            print(f"Decoded data written to: {output_file_path}")
                    except Exception as e:
                        print(f"Error during writing decoded data: {e}")

        print("\n\n")


if __name__ == "__main__":
    main()
