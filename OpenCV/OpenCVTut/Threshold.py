import cv2

img = cv2.imread('images/bookpage.jpg')
#gimg = cv2.imread('images/bookpage.jpg', cv2.IMREAD_GRAYSCALE)

gimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval, t1 = cv2.threshold(img, 12, 255, cv2.THRESH_BINARY)
retval2, t2 = cv2.threshold(gimg, 12, 255, cv2.THRESH_BINARY)
gaus = cv2.adaptiveThreshold(gimg, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
retval3, ot = cv2.threshold(gimg, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow('orig', img)
cv2.imshow('t', t1)
cv2.imshow('t2', t2)
cv2.imshow('t3', gaus)
cv2.imshow('t4', ot)
cv2.waitKey(0)
cv2.destroyAllWindows()
