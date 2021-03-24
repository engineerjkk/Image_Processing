import sys
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

cp = (src.shape[1] / 2, src.shape[0] / 2)
#입력영상의 shape에서 가로 세로를 반으로 나눈것을 cp로 지정. 이점이 중앙센터
rot = cv2.getRotationMatrix2D(cp, 20, 0.5)
#cp가 센터, 20도 반시계방향, 크기는 반으로
dst = cv2.warpAffine(src, rot, (0, 0))
#이 rot를 가져다가 warpAffine함수의 두번째 인자로 지정을 한다.
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
