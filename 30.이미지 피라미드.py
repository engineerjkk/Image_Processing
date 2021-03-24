import sys
import numpy as np
import cv2


src = cv2.imread('cat.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()


rc = (250, 120, 200, 200)  # rectangle tuple
#250,150 좌표부터 시작해서 가로 세로크기. (x,y,w,h)의 튜플
# 원본 영상에 그리기
cpy = src.copy()
#입력영상의 복사본
cv2.rectangle(cpy, rc, (0, 0, 255), 1)
#rectangle함수는 이미지에 사각형을 그리는 함수이다.
#rectanglr 함수 두번째 인자에 rc를 줄수있다.
#빨간색으로 두께가 2픽셀
cv2.imshow('src', cpy)
cv2.waitKey()

# 피라미드 영상에 그리기
for i in range(1, 4):
    src = cv2.pyrDown(src) #나머지 파라미터를 주지않으면 절반씩 작아지는 함수이다.
    cpy = src.copy()
    cv2.rectangle(cpy, rc, (0, 0, 255), 1, shift=i)
    #보통 shift는 디폴트로 0을 놓지만 사각형이 사진에 맞게 바뀔때에는 shift를 쓴다.
    #입력영상은 줄어드는데 rc를 그대로 넣는다?
    #대신에 shift연산을 사용한다. 그림을 그리기위한 좌표를 얼마나 줄일거냐이다.
    cv2.imshow('src', cpy)
    cv2.waitKey()
    cv2.destroyWindow('src')

cv2.destroyAllWindows()
