#Blurring techniques
"""
Blurring is an image processing technique used to smooth out edges and reduce noise, 
creating a softened version of the original image. OpenCV provides several methods for blurring an image
"""
import cv2
import numpy as np

# Read the image
img = cv2.imread('Image1.jpg')

# Apply Averaging
average_blur = cv2.blur(img, (5, 5))
"""
Function: cv2.blur(image, (width, height))
cv2.blur(): This function calculates the average of all the pixels under the kernel area and replaces the central element with this average.
This operation is also known as "box filtering".
"""

# Apply Gaussian Blurring
gaussian_blur = cv2.GaussianBlur(img, (5, 5), 0)
"""
Function: cv2.GaussianBlur(image, (width, height), standard_deviation)
cv2.GaussianBlur(): This function uses a Gaussian kernel,
which gives a weighted average of the surrounding pixels to produce a more natural blurring effect
"""

# Apply Median Blurring
median_blur = cv2.medianBlur(img, 5)
"""
Function: cv2.medianBlur(image, kernel_size)
cv2.medianBlur(): This function replaces each pixel's value with the median value of all the pixels in the kernel area.
This method is particularly effective in reducing "salt and pepper" noise.
"""

# Apply Bilateral Filtering
bilateral_blur = cv2.bilateralFilter(img, 9, 75, 75)
"""
Function: cv2.bilateralFilter(image, diameter, color_sigma, space_sigma)
cv2.bilateralFilter(): This function applies a bilateral filter to the image, which smooths the image while preserving edges.
It is useful for denoising while maintaining sharp edges.
"""

# Display the results
# Press ESC to show newt Image
cv2.imshow('Original', img)
K = cv2.waitKey(0) & 0xFF

#Press ESC to show newt Image
if K == 27:
    cv2.imshow('Averaging', average_blur)
    K = cv2.waitKey(0) & 0xFF

#Press ESC to show newt Image
if K == 27:
    cv2.imshow('Gaussian Blurring', gaussian_blur)
    K = cv2.waitKey(0) & 0xFF

#Press ESC to show newt Image
if K == 27:
    cv2.imshow('Median Blurring', median_blur)
    K = cv2.waitKey(0) & 0xFF

#Press ESC to show newt Image
if K == 27:
    cv2.imshow('Bilateral Filtering', bilateral_blur)
    K = cv2.waitKey(0) & 0xFF

if K == 27:
    cv2.destroyAllWindows()
