#Resizing and Masking
import cv2
import numpy as np

# Load an image
image = cv2.imread('Document.jpg')

# Resize the image
resized_image = cv2.resize(image, (500, 500), interpolation=cv2.INTER_LINEAR)

"""
#cv2.resize(input_image, output_size, interpolation_method)
Helps in standardizing input sizes for models,
reducing processing time, and fitting images into a specific format.
"""

# Create a mask
mask = np.zeros(resized_image.shape[:2], dtype=np.uint8)
mask[100:200, 100:200] = 255  # Example mask
masked_image = cv2.bitwise_and(resized_image, resized_image, mask=mask)

"""
A binary mask image that determines which parts of the input image to keep.
"""
print("Use'ESC' Key to go foward/show other output ")
# Display results
cv2.imshow('Resized', resized_image)
k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.imshow('Masked', masked_image)
    k = cv2.waitKey(0) & 0xFF

if k == 27:
    cv2.destroyAllWindows()
