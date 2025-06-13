import os # Import the os module
from PIL import Image # pip install pillow

directory_files = os.listdir() # Get all files in the directory

multiple_images = [file for file in directory_files if file.endswith(('.jpg', '.png'))] # List of all images in the directory

for image in multiple_images: # Loop through all images in the directory
    img = Image.open(image) # Open the image
    img.thumbnail(size=(300,300)) # Resize the image
    print(img) # Print the image
    img.save('resized-image_'+image, optimize=True, quality=30) # Save the image

print(multiple_images) # Print the list of images