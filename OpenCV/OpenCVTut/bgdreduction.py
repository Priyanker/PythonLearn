# MOG Background Reduction

import cv2
'''
cap = cv2.VideoCapture('images/car1.mp4')
cap = cv2.VideoCapture('images/tech.mp4')
cap = cv2.VideoCapture('images/ink.mp4')
cap = cv2.VideoCapture('images/scienceexpl1.mp4')
'''
cap = cv2.VideoCapture('images/people-walking.mp4')
cap = cv2.VideoCapture('images/scienceexpl2.mp4')

# for video cam
# cap = cv2.VideoCapture(0)


fgbg = cv2.createBackgroundSubtractorMOG2()

while(1):
    ret, frame = cap.read()

    fgmask = fgbg.apply(frame)

    cv2.imshow('fgmask', frame)
    cv2.imshow('frame', fgmask)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()
