#4.basic drawing functions
import cv2
import numpy as np

# Create a blank image
image = np.zeros((400, 400, 3), dtype=np.uint8)

# Draw a line
#cv2.line(image, top_left_x_y, bottom_right_x_y, color, thickness)
cv2.line(image, (50, 50), (350, 350), (255, 0, 0), 5)  # Blue line

# Draw a rectangle
#cv2.rectangle(image, top_left_corner_x_y, bottom_right_corner_x_y, color, thickness)
cv2.rectangle(image, (50, 50), (350, 350), (0, 255, 0), 3)  # Green rectangle

# Draw a circle
#cv2.circle(image, center_x_y, radius, color, thickness)
cv2.circle(image, (200, 200), 100, (0, 0, 255), -1)  # Red filled circle

# Draw text
#cv2.putText(image, text, bottom_left_corner_x_y, font_face, font_scale, color, thickness, line_type)
cv2.putText(image, 'Hello World!', (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

# Draw an ellipse
#cv2.ellipse(image, center_x_y, axes_length, angle, start_angle, end_angle, color, thickness)
cv2.ellipse(image, (200, 200), (100, 50), 0, 0, 180, (255, 255, 0), 2)  # Yellow ellipse

# Display the image
cv2.imshow('Shapes', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
