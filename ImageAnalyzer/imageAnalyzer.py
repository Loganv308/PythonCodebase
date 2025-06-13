import os

from PIL import Image

def analyzeImage(imagePath):
    image = Image.open(imagePath)
    width, height = image.size
    return width, height

def main():
    imagePath = os.path.join(os.path.dirname(__file__), 'image.png')
    width, height = analyzeImage(imagePath)
    print('Width: %s, Height: %s' % (width, height))

if __name__ == '__main__':
    main()