# import cv2 as cv
# img = cv.imread('/Users/baozi/summer_training/day2/opencv/test.jpg')
# # print(img.shape) #(H W C)
# # img = cv.imread('/Users/baozi/summer_training/day2/opencv/test.jpg', 0) #变黑白，
# # 0 Gray 1 RGb -1 RGBA

# cv.imshow("img", img)
# cv.waitKey(0)
# cv.destroyAllWindows()

w = 200
h = 200
import numpy as np
img = np.zeros(shape=(h, w, 3))
print(img)