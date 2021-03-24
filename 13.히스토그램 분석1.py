import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2


# 그레이스케일 영상의 히스토그램
src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

#histSize는 256이며 range는 0~255이므로 256이 맞습니다(-1까지)
hist = cv2.calcHist([src], [0], None, [256], [0, 256])

cv2.imshow('src', src)
#cv2.waitKey(1)

plt.plot(hist)
plt.show()

# 컬러 영상의 히스토그램
src = cv2.imread('lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

colors = ['b', 'g', 'r']
bgr_planes = cv2.split(src)

for (p, c) in zip(bgr_planes, colors):
    hist = cv2.calcHist([p], [0], None, [256], [0, 256])
    plt.plot(hist, color=c)
#p는 반드시 리스트 형태로 넣습니다. color type은 b g r 로 표현됩니다.
cv2.imshow('src', src)
cv2.waitKey(1)

plt.show()

cv2.destroyAllWindows()
