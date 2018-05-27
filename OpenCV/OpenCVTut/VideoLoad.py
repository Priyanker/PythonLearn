import cv2

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    retval2, thres = cv2.threshold(frame, 12, 255, cv2.THRESH_BINARY)
    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
cv2.imwrite('images/pic.png', frame)

cv2.imwrite('images/gray.png', gray)
