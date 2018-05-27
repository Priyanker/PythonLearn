from matplotlib import pyplot as plt
import numpy as np
import cv2

img1 = cv2.imread('images/watch.jpg', cv2.IMREAD_GRAYSCALE)  # =0
# IMREAD_COLOR =1
# IMREAD_UNCHANGED = -1


cv2.imshow('imge', img1)
cv2.waitKey(0)
cv2.destroyAllWindows()

'''
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([200, 300, 400], [100, 200, 300], 'c', linewidth=5)
plt.show()
'''

'''
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.plot([50, 100], [80, 120], 'c', linewidth=5, color='#990999')
plt.show()

'''
cv2.imwrite('images/watchg.png', img1)
