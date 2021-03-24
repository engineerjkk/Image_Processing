import sys
import numpy as np
import cv2


# 그레이스케일 영상 불러오기
src = cv2.imread('lenna.bmp', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

#dst = cv2.add(src, 100) 
#입력이미지에 밝기값 전체 100추가
#add함수로 100을 더한다는건 사실내부에서 (100,0,0,0) 으로바뀐다. 그레이스케일에서는 똑같다. 그래서 컬러에서 하면 BGR인 블루만 100이 더해진다.
dst = np.clip(src + 100., 0, 255).astype(np.uint8)
#결과가 0보다 작으면 0으로, 255보다 크면 255로
#정수단위가 아닌, src+100.으로 점을 찍으면 실수단위로 연산이 된다.
#astype으로 컨버젼을 해줘야한다.
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

# 컬러 영상 불러오기
src = cv2.imread('lenna.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

dst = cv2.add(src, (100, 100, 100, 0))
#컬러는 마지막 알파체널 제외하고 BGR전부 고르게 100씩 더해줘야한다.
#dst = np.clip(src + 100., 0, 255).astype(np.uint8)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
