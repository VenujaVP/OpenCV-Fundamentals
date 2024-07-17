import cv2  # Import the OpenCV library

# Open the default camera (index 0)
cap = cv2.VideoCapture(0)

#If camara avalable print "True" and not Print "False"
print("camara avalablity - ",cap.isOpened()) 


print( "For exit enter ESC Key") 
first_iteration = True
while True:  # Start an infinite loop to capture video frames

    # Read a frame from the camera
    ret, frame = cap.read()  

    if first_iteration:  # Check if it's the first iteration
        #print Frame Heigth
        print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)) 
        #print Frame Width
        print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        # Set the flag to False after the first iteration
        first_iteration = False  

    """
    #For convert Frame Screen to Gray (comment 25th line and uncomment this block
    Gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    cv2.imshow("Capture_FRAME", Gray)  # Display the captured frame in a window
    cv2.imshow("Capture_FRAME", Gray)
    """
    #FOR FLIP THE SIDE, REMOVE COMMENT IN LINE 32 AND 39, CREATE 38 LINE AS COMMENT
    #flipped_frame = cv2.flip(frame, 1)   # Flip the frame horizontally
        #0 means flipping around the x-axis (vertical flip).
        #1 means flipping around the y-axis (horizontal flip).
        #-1 means flipping around both axes (both horizontal and vertical flip).

    #Display the captured frame in a window
    cv2.imshow("Capture_FRAME", frame)
    #cv2.imshow("Capture_FRAME", flipped_frame)   #Display the flipped frame in a window


    # Check if the 'Esc' key (ASCII 27) is pressed
    if cv2.waitKey(1) & 0xFF == 27:
        cv2.destroyAllWindows()  # Close any OpenCV windows
        break  # Exit the loop
    

cap.release()  # Release the camera for use by other applications
cv2.destroyAllWindows()  # Close any OpenCV windows
