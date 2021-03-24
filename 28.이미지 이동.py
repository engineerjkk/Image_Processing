import sys
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

aff = np.array([[1, 0, 200],
                [0, 1, 100]], dtype=np.float32)
#2행3열이므로 가로로 이동할 크기, 세로로 이동할 크기를 지정한다.
#float형으로 만들어야하기떄문에 dtype을 지정해줘야한다. 
dst = cv2.warpAffine(src, aff, (0, 0))
#입력영상과 똑같은 크기의 dst를 받을 수 있다. 
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
