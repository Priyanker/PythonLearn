# Haar Cascade Object Detection Face & Eye

import cv2
import copy
file_paths = []
# multiple cascades:
#    https: // github.com/Itseez/opencv/tree/master/data/haarcascades

# https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml


def getLocs(location):
    global file_paths
    file_paths.clear()
    face_cascade = cv2.CascadeClassifier('D:\Programming\PythonLearn\OpenCV\OpenCVTut\haarcascade_frontalface_default.xml')
    # smile_cascade = cv2.CascadeClassifier(
    #    'D:\Programming\PythonLearn\OpenCV\OpenCVTut\haarcascade_smile.xml')

    # https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_eye.xml
    # eye_cascade = cv2.CascadeClassifier(
    #    'D:\Programming\PythonLearn\OpenCV\OpenCVTut\haarcascade_eye.xml')

    img = cv2.imread(location)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, minSize=(50, 50))
    # res_img = copy.deepcopy(img)

    img = cv2.imread(location)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray)

    resface = copy.deepcopy(img)  # img.copy() does same thing
    count = 1
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x+w, y+h), (66, 165, 245), 2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
        roi_color1 = resface[y:y+h, x:x+w]
        s1 = 'face'+str(count)
        # cv2.imshow(s1, roi_color1)
        loc = "images/JL/"
        loc = loc + s1 + ".png"
        file_paths.append(loc)
        cv2.imwrite(loc, roi_color1)
        count = count + 1

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

    cv2.imwrite('images/JL/mainout.jpg', img)
    file_paths.append('images/JL/mainout.jpg')
    # print(len(file_paths))
    return file_paths
