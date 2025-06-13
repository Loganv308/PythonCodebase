# Icon Creator
# Written by: @Loganv308
# Version: 1.0
# Date: 11/8/2022

import requests
from PIL import Image

def make_square(im, min_size=256, fill_color=(0, 0, 0, 0)):
    x, y = im.size
    size = max(min_size, x, y)
    new_im = Image.new('RGBA', (size, size), fill_color)
    new_im.paste(im, (int((size - x) / 2), int((size - y) / 2)))
    return new_im

def main():
    try:
        image_url = input("Enter the image url: ")
        fileName = input("Enter the name of the file: ")

        img_data = requests.get(image_url).content
        with open(f'{fileName}.png', 'wb') as handler:
            handler.write(img_data)

        img = Image.open(f'{fileName}.png')

        icon_sizes = [(16, 16), (24, 24), (32, 32), (48, 48), (64, 64), (128, 128), (255, 255)]

        img.save(f'{fileName}.ico', sizes=icon_sizes, optimize=True)
        
        test_image = Image.open(f'{fileName}.png')
        
        test_image.show()
    except KeyboardInterrupt:
        print("Exiting...")
        exit()
    except:
        print("An error occured. Exiting...")
        exit()

if __name__ == "__main__":
    main()

# new_image = make_square(test_image)