import sys
import numpy as np
import cv2


src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()
'''
kernel=np.array([[-1, 0, 1],
                 [-2, 0, 2],
                 [-1, 0, 1]],
        dtype=np.float32)
dx= cv2.filter2D(src,-1,kernel,delta=128)
'''
#이렇게는 하지 않는다 사실 오픈시비에서 제공하는 소벨을 쓰자

dx = cv2.Sobel(src, cv2.CV_32F, 1, 0,delta=128)
#4byte 형태의 float 형태
dy = cv2.Sobel(src, cv2.CV_32F, 0, 1,delta=128)

mag= cv2.magnitude(dx,dy)
mag=np.clip(mag,0,255).astype(np.uint8)
#magnitude는 x방향과 y방향을 같이 조합해서 쓰기 떄문에 기둥부분을 검출할 수 있다.

edge=np.zeros(mag.shape[:2],np.uint8)
edge[mag>80]=255
#threshold 값을 120정도 줌.

cv2.imshow('src', src)
cv2.imshow('mag', mag)
cv2.imshow('edge', edge) 
#cv2.imshow('dx', dx)
#cv2.imshow('dy', dy)
#어차피 dx,dy가 float타입이어도 내부에서 255를 곱해서 처리해준다.
cv2.waitKey()

cv2. destroyAllWindows()
