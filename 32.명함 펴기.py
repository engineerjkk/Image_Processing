import sys
import numpy as np
import cv2


src = cv2.imread('namecard.jpg')

if src is None:
    print('Image load failed!')
    sys.exit()

w, h = 720, 400#출력영상의 크기를 9:5정도로 만들어줬다.
srcQuad = np.array([[325, 307], [760, 369], [718, 611], [231, 515]], np.float32)
#입력영상의 좌표를 만들어준다. 죄측상단, 오른쪽 상단, 오른쪽하단, 좌측하단의 좌표이다.
dstQuad = np.array([[0, 0], [w-1, 0], [w-1, h-1], [0, h-1]], np.float32)
#출력영상의 좌상단,우상단,우하든,좌하든

pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
#두개의 인자도 지정한다. 
dst = cv2.warpPerspective(src, pers, (w, h))
#두번째 인자와 출력영상의 크기.
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
