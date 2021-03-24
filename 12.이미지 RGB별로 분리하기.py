import sys
import numpy as np
import cv2


# 컬러 영상 불러오기
src = cv2.imread('candies.png', cv2.IMREAD_COLOR)

if src is None:
    print('Image load failed!')
    sys.exit()

# 컬러 영상 속성 확인
print('src.shape:', src.shape)  # src.shape: (480, 640, 3)
print('src.dtype:', src.dtype)  # src.dtype: uint8

#컬러이미지 BGR을 HSV 형태로 변환하여 줍니다.
src_hsv=cv2.cvtColor(src,cv2.COLOR_BGR2HSV)

b_plane = src_hsv[:, :, 0]
g_plane = src_hsv[:, :, 1]
r_plane = src_hsv[:, :, 2]

cv2.imshow('src', src)
cv2.imshow('B_plane', b_plane)
cv2.imshow('G_plane', g_plane)
cv2.imshow('R_plane', r_plane)
cv2.waitKey()

cv2.destroyAllWindows()
