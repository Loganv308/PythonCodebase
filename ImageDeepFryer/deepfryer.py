import cv2
import numpy as np
import random

image = cv2.imread("20211015_131435.jpg")

height, width, channels = image.shape

def createNoise():

    counter = 1

    saturation_level = random.randint(0, 256)

    # Convert the image to the HSV color space
    image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Increase the saturation of the image
    image_hsv[:,:,1] = cv2.add(image_hsv[:,:,1], saturation_level)

    # Clip the saturation to the maximum value (255)
    image_hsv[:,:,1] = np.clip(image_hsv[:,:,1], 0, 255)

    # Convert the image back to the BGR color space
    image_deep_fried = cv2.cvtColor(image_hsv, cv2.COLOR_HSV2BGR)

    # Setting the size of the window
    kernel_size = (3, 3) 

    if kernel_size[0] > width or kernel_size[1] > height:
        kernel_size = (min(kernel_size[0], width), min(kernel_size[1], height))

    # Apply a Gaussian blur to the image
    image_deep_fried = cv2.GaussianBlur(image_deep_fried, kernel_size, 0)

    # Choose a random amount of contrast
    contrast_level = random.uniform(1.0, 2.0)

    # Increase the contrast of the image
    image_deep_fried = cv2.addWeighted(image_deep_fried, contrast_level, np.zeros(image.shape, dtype=image.dtype), 0, 0)

    # Save the deep fried image
    cv2.imwrite(f'20211015_131435_deepfriedV{int(counter)}.jpg', image_deep_fried)

    counter =+counter
   
if __name__ == '__main__':
    counter = 5
    for i in range(counter):
        createNoise()