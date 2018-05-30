# Haar Cascade Object Detection Face & Eye

import cv2
import copy
# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml


def getLoc(location):
    face_cascade = cv2.CascadeClassifier(
        'D:\Programming\PythonLearn\OpenCV\OpenCVTut\haarcascade_frontalface_default.xml')
    # smile_cascade = cv2.CascadeClassifier(
    #    'D:\Programming\PythonLearn\OpenCV\OpenCVTut\haarcascade_smile.xml')
    # https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
    # eye_cascade = cv2.CascadeClassifier(
    #    'D:\Programming\PythonLearn\OpenCV\OpenCVTut\haarcascade_eye.xml')

    img = cv2.imread(location)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, minSize=(50,50))
    res_img = copy.deepcopy(img)

    for (x, y, w, h) in faces:
        print((x, y, w, h))
        cv2.rectangle(img, (x, y), (x+w, y+h), (66, 165, 245), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        res_face = res_img[y:y+h, x:x+w]

        '''
        # eye detection


        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in eyes:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), ((205, 220, 57)), 2)
        '''

        '''
        # smile detection
        smile = smile_cascade.detectMultiScale(roi_gray)
        for (ex, ey, ew, eh) in smile:
            cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), ((105, 120, 157)), 2)
            # cv2.putText(roi_color, 'smile', (ex, ey), cv2.FONT_HERSHEY_DUPLEX, 0.7, (100, 0, 255), 2, cv2.LINE_AA)

        '''
    # cv2.imshow('img', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    cv2.imwrite('images/fdout.jpg', img)
    return "images/fdout.jpg"
