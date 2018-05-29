# Haar Cascade Object Detection Face & Eye

import cv2
import copy
# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
smile_cascade = cv2.CascadeClassifier('haarcascade_smile.xml')
# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

img = cv2.imread('images/JL/JL.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray)

resface = copy.deepcopy(img)  # img.copy() does same thing
count = 0
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x+w, y+h), (66, 165, 245), 2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    roi_color1 = resface[y:y+h, x:x+w]
    s1 = 's'+str(count)
    cv2.imshow(s1, roi_color1)
    loc = "images/JL/"
    cv2.imwrite(loc+s1+".png", roi_color1)
    count = count + 1


cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('images/JL/fdout.jpg', img)
