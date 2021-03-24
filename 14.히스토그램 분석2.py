import sys
import numpy as np
import matplotlib.pyplot as plt
import cv2


def getGrayHistImage(hist):
    imgHist = np.full((100, 256), 255, dtype=np.uint8)
    #먼저 히스토그램을 그릴 바탕화면을 만들어줍니다.

    histMax = np.max(hist) #히스토그램의 MAX값을 계산해저장합니다.
    for x in range(256):
        pt1 = (x, 100) 
        #x,y 좌표이다. x좌표는 0이고 y가 100이면 가장 아래이다. 
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))
        #가장 큰 부분의 높이가 100픽셀이 되도록.
        cv2.line(imgHist, pt1, pt2, 0)

    return imgHist
#matplot 라이브러리 안쓰고 openCV만으로도 가능하다.

src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

hist = cv2.calcHist([src], [0], None, [256], [0, 256])
histImg = getGrayHistImage(hist)

cv2.imshow('src', src)
cv2.imshow('histImg', histImg)
cv2.waitKey()

cv2.destroyAllWindows()
