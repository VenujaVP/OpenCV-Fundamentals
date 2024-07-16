#how to use k = cv2.waitKey(0) wait for a key press
import cv2

# Read the image
img1 = cv2.imread("Image1.jpg", -1)

# Display the image in a window named 'image_1'
cv2.imshow("Press ESE Close, Press 's' to imwrite", img1)

### Wait for a key press indefinitely
k = cv2.waitKey(0) & 0xFF

### Check if the pressed key is 'Esc' (key code 27)
if k == 27:
    print("Esc key pressed. Closing all windows.")
    cv2.destroyAllWindows()  # Close all OpenCV windows
elif k == ord("s"):  # 'k == ord("s")' to check for 's' key
    print("'s' key pressed. Saving the image as 'image_new1.jpg'.")
    cv2.imwrite("image_new1.jpg", img1)  # Save the image as 'image_new1.jpg'
    cv2.destroyAllWindows()  # Close all OpenCV windows
else:
    print("Another key pressed. Closing all windows.")
    cv2.destroyAllWindows()  # Close all OpenCV windows
