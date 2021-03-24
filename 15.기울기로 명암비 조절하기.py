import sys
import numpy as np
import cv2


src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

alpha = 1.0 #기울기 1 
dst = np.clip((1+alpha)*src - 128*alpha, 0, 255).astype(np.uint8)
#128을 지나면서 기울기는 1, 실수형태이기에 astype(np.uint8)로 한다.

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()

