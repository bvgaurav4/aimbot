import cv2
import pyautogui
import numpy as np  

while True:
    # Capture screenshot
    screenshot = pyautogui.screenshot()
    # Convert the image into numpy array representation
    frame = np.array(screenshot)
    # Convert the BGR image into RGB image
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    # Display the RGB image
    cv2.imshow('Screen Capture', frame)
    # Wait for the user to press 'q' key to stop the program
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()