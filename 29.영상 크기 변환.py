import sys
import numpy as np
import cv2


src = cv2.imread('rose.bmp') # src.shape=(320, 480)
#원래 이미지 사이즈
if src is None:
    print('Image load failed!')
    sys.exit()

dst1 = cv2.resize(src, (0, 0), fx=4, fy=4, interpolation=cv2.INTER_NEAREST)
#nearest는 제일 안좋다.
#dsize를 0,0주는대신에 fx,fy에다가 4를줌. 결과적으로는 dsize도 1920,1280이 입력된다.
dst2 = cv2.resize(src, (1920, 1280))  # cv2.INTER_LINEAR. 기본 디폴트값
#엣지부분에 뭔가 컴퓨터가 만든느낌이있음.
dst3 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_CUBIC)
#인터 큐빅이 조금더 난데
dst4 = cv2.resize(src, (1920, 1280), interpolation=cv2.INTER_LANCZOS4)
#란초스가 컨트라스트 느낌이 더 높은 느낌이 있긴함.
cv2.imshow('src', src)
cv2.imshow('dst1', dst1[500:900, 400:800])
#너무크니까 x는 500~900까지 y는 400~800까지 보여준다.
cv2.imshow('dst2', dst2[500:900, 400:800])
cv2.imshow('dst3', dst3[500:900, 400:800])
cv2.imshow('dst4', dst4[500:900, 400:800])
cv2.waitKey()
cv2.destroyAllWindows()
