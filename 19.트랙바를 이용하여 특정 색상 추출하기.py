import sys
import numpy as np
import cv2


src = cv2.imread('candies.png')

if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
#hsv로 변환

def on_trackbar(pos): #지금 여기서는 쓰지 않는 함수
    hmin = cv2.getTrackbarPos('H_min', 'dst')
    hmax = cv2.getTrackbarPos('H_max', 'dst')
#getTrackbarPos : dst창에있는 H_min의 위치를 받는다. 
    dst = cv2.inRange(src_hsv, (hmin, 150, 0), (hmax, 255, 255))
    #hmin을 20 hmax를 40 하면 노란색을 골라낼수있다. 
    #100~120 정도로 하면 파란색을 골라낼 수 있다.
    #빨간색은 Hue값이 0이나 180에 가깝다. 빨간색은 경계선에있기때문에 따로따로 검출해서 or연산으로 붙여주어야한다.
    cv2.imshow('dst', dst)


cv2.imshow('src', src)
cv2.namedWindow('dst')

cv2.createTrackbar('H_min', 'dst', 50, 179, on_trackbar)
cv2.createTrackbar('H_max', 'dst', 80, 179, on_trackbar)
#Hue값에 하나는 Maximum값, 하나는 Minimum값
on_trackbar(0)

cv2.waitKey()

cv2.destroyAllWindows()
