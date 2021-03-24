import sys
import numpy as np
import cv2

src = cv2.imread('noise.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.medianBlur(src, 3)
dst2=cv2.medianBlur(dst,3)
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('dst2',dst2)#미디언 필터를 한번 더 반복해 줍니다.
cv2.waitKey()

cv2.destroyAllWindows()

#랜덤하게 0 또는 255로 10%정도를 추가했다.