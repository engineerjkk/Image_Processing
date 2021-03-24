import sys
import numpy as np
import cv2


#src = cv2.imread('candies.png')
src = cv2.imread('candies2.png')

if src is None:
    print('Image load failed!')
    sys.exit()

src_hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)

dst1 = cv2.inRange(src, (0, 128, 0), (100, 255, 100))
#B는 0~100, G는 128~ 255, R은 0~100까지 값을 다 골라서 dst1으로 리턴한다.
dst2 = cv2.inRange(src_hsv, (50, 150, 0), (80, 255, 255))
#H값이 50~80, S는 150~255, V는 0~255이다.

cv2.imshow('src', src)
cv2.imshow('dst1', dst1)
cv2.imshow('dst2', dst2)
cv2.waitKey()

cv2.destroyAllWindows()

#조건을 그대로 줬는데 RGB에서 밝은건 잘되는데 어두운건 안된다.
#그런데 HSV는 그런거 상관없이 잘 된다.