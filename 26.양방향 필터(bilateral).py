import sys
import numpy as np
import cv2

src = cv2.imread('lenna.bmp',cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.bilateralFilter(src, -1, 10, 5)
#d값을 -1로 주면 자동으로 마스크 크기가 설정된다.
#엣지 기준을 10(시그마값)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
