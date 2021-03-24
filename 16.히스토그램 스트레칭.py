import sys
import numpy as np
import cv2


src = cv2.imread('Hawkes.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()



def getGrayHistImage(hist): #히스토그램 만드는 함수
    imgHist = np.full((100, 256), 255, dtype=np.uint8)

    histMax = np.max(hist)  # 히스토그램의 MAX값을 계산해서
    for x in range(256):
        pt1 = (x, 100)
        pt2 = (x, 100 - int(hist[x, 0] * 100 / histMax))
        #가장 큰 부분의 높이가 100픽셀이 되도록.
        cv2.line(imgHist, pt1, pt2, 0)

    return imgHist

#오픈시비버전
gmin, gmax, _, _ = cv2.minMaxLoc(src)
dst = cv2.normalize(src, None, 0, 255, cv2.NORM_MINMAX)

#넘파이버전
#gmin=np.min(src)
#gmax=np.max(src)
#dst=np.clip((src-gmin)*255./(gmax-gmin),0,255).astype(np.uint8)
#dst = ((src - gmin) * 255. / (gmax - gmin)).astype(np.uint8)
#src, None(출력영상은 그냥 None으로 주면됨)

hist = cv2.calcHist([src], [0], None, [256], [0, 256])
histImg = getGrayHistImage(hist)

hist2 = cv2.calcHist([dst], [0], None, [256], [0, 256])
histImg2 = getGrayHistImage(hist2)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.imshow('histImg', histImg)#히스토그램 보여주기
cv2.imshow('histImg2', histImg2)#히스토그램 보여주기
cv2.waitKey()

cv2.destroyAllWindows()
