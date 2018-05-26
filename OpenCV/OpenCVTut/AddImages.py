import cv2

img1 = cv2.imread('images/add1.png')
img2 = cv2.imread('images/add2.png')
img3 = cv2.imread('images/pylogo.png')
add = img1 + img2
add1 = cv2.add(img1, img2)
weightedadd = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)

cv2.imshow('image1', img1)
cv2.imshow('image2', img2)
cv2.imshow('add', add)
cv2.imshow('add1', add1)
cv2.imshow('wadd', weightedadd)


cv2.waitKey(0)
cv2.destroyAllWindows()
