import cv2
import numpy as np

dark_red  = np.uint8([[[12,22,121]]])
dark_red = cv2.cvtColor(dark_red,cv2.COLOR_BGR2HSV)
print(dark_red)
cv2.imshow('d', dark_red)
cv2.waitKey(0)
cv2.destroyAllWindows()
