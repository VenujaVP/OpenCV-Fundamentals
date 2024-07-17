import cv2

# Create a VideoCapture object to access the webcam
cap = cv2.VideoCapture(0)  # Open the default camera (index 0)

#VideoWriter_fourcc determines how the video is compressed and stored.
#link for more fourcc codes - https://fourcc.org/codecs.php
fourcc = cv2.VideoWriter_fourcc(*'XVID') 
#fourcc = cv2.VideoWriter_fourcc('X' 'V' 'I' 'D')

#Output video=>  (Name, fouecc, PPF rate, (Heigth, Width))
out = cv2.VideoWriter('output.avi', fourcc, 25.0, (480, 640))  

# Check if the VideoWriter opened successfully
if not out.isOpened():
    print("Error: VideoWriter not opened")
    cap.release()  # Release the camera if VideoWriter failed
    cv2.destroyAllWindows()
    exit()

# Check if the camera is available
print("Camera availability - ", cap.isOpened()) 
print("Camera opened successfully")

while True:
    # Capture frame by frame
    ret, frame = cap.read()  # Read a frame from the camera
    print("frame captured = ",ret)

    # Check if the frame was captured successfully
    if ret:
        # Display the captured frame in a window
        cv2.imshow('frame', frame)  

        # Write the frame to the output video
        out.write(frame)  

        # Check if the 'Esc' key (ASCII 27) is pressed
        if cv2.waitKey(1) & 0xFF == 27:  # Check for ESC key press to exit
            break

# When everything is done, release the capture and close all windows
cap.release()  # Release the VideoCapture object to free the camera
out.release()  # Release the VideoWriter object to save the video file properly
cv2.destroyAllWindows() 
