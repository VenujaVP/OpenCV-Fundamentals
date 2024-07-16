#cv2.imread(),cv2.imshow, cv2.waitKey, cv2.destroyAllWindows()
import cv2

# Image Read - cv2.imread()
img1 = cv2.imread("Image1.jpg", 1)  # image in color (BGR format)
img2 = cv2.imread("Image1.jpg", 0)  # image in a single channel, where each pixel represents the intensity of light (black and white)
img3 = cv2.imread("Image1.jpg", -1)  # image has an alpha channel (transparency), it will be included. If not, it behaves like mode 1 (color)

# Print the image as array
print("print img1_################################################")
print(img1)
print("print img2_################################################")
print(img2)
print("print img3_################################################")
print(img3)

# cv2.imshow() - Display the image in a window named 'image_X'
# (See the difference between these 3)
cv2.imshow("image_1", img1)
cv2.waitKey(2000)  # This function waits 2S (2000ms)
cv2.destroyAllWindows() # Close all OpenCV windows

cv2.imshow("image_0", img2)
cv2.waitKey(3000)  # This function waits 3S (3000ms)
cv2.destroyAllWindows() 

cv2.imshow("image_-1", img3)
cv2.waitKey(1000)  # This function waits 1S (1000ms)
cv2.destroyAllWindows()

