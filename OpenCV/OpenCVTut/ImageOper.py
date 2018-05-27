import cv2
img = cv2.imread('images/watch1.jpg', cv2.IMREAD_COLOR)
watch_face = img[37:111, 107:194]
img[0:74, 0:87] = watch_face

# img[0:115, 0:88] = area
cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

print(img.shape)
print(img.size)
print(img.dtype)
