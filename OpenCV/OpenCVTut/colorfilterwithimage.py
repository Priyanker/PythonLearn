import cv2
import numpy as np


frame = cv2.imread('images/watch.jpg')
hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

lower_red = np.array([10, 100, 90])
upper_red = np.array([20, 255, 200])

mask = cv2.inRange(hsv, lower_red, upper_red)
result = cv2.bitwise_and(frame, frame, mask=mask)

kernel = np.ones((15, 15), np.float32)/225
smoothed = cv2.filter2D(result, -1, kernel)

blur = cv2.GaussianBlur(result, (15, 15), 0)

median = cv2.medianBlur(result, 15)
#cv2.imshow('frame', frame)
#cv2.imshow('mask', mask)
cv2.imshow('smoothed', smoothed)
cv2.imshow('blur', blur)
cv2.imshow('median', median)
cv2.imshow('res', result)


cv2.waitKey(0)
cv2.destroyAllWindows()
