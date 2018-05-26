import cv2
import numpy as np
img = cv2.imread('images/watch.jpg', cv2.IMREAD_COLOR)

cv2.line(img, (10, 10), (800, 800), (0, 255, 0), 15)
cv2.rectangle(img, (15, 25), (200, 150), (255, 0, 0), 5)
cv2.circle(img, ((200+15)//2, (150+25)//2), (150-25)//2, (0, 0, 255), -1)
pts = np.array([[10, 5], [20, 30], [70, 20], [50, 10]], np.int32)
# OpenCV documentation had this code, which reshapes the array to a 1 x 2. I did not
# find this necessary, but you may:
#pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (0, 0, 255), 3)

font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img, 'opencv', (450, 430), font, 1, (100, 0, 255), 2, cv2.LINE_AA)

cv2.imshow('image', img)

cv2.waitKey()
cv2.destroyAllWindows()
