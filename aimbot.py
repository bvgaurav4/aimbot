from mss import mss
import cv2
import numpy as np

sct = mss()

while True:
    screenshot = sct.grab(sct.monitors[1])
    # Only take the RGB channels for each pixel
    img = np.array(screenshot)[:, :, :3]
    cv2.imshow('Screen Capture', img)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()