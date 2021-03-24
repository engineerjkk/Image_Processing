import sys
import numpy as np
import cv2


src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

#dx와 dy는 입력영상의 미분값을 저장한 행렬
dx = cv2.Sobel(src, cv2.CV_32F, 1, 0)
dy = cv2.Sobel(src, cv2.CV_32F, 0, 1)

#크기계산
mag = cv2.magnitude(dx, dy)
mag = np.clip(mag, 0, 255).astype(np.uint8)

#입력영상과 같은 크기의 출력 창 생성
edge = np.zeros(src.shape[:2], np.uint8)

#magnitude 픽셀에서 120보다 픽셀은 edge에서 255로 전부 세팅해줍니다.
edge[mag > 120] = 255
#_, dst = cv2.threshold(mag, 120, 255, cv2.THRESH_BINARY)


cv2.imshow('src', src)
cv2.imshow('mag', mag)
cv2.imshow('edge', edge)
cv2.waitKey()

cv2.destroyAllWindows()
