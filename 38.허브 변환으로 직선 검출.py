import sys
import numpy as np
import cv2


src = cv2.imread('building.jpg', cv2.IMREAD_GRAYSCALE)

if src is None:
    print('Image load failed!')
    sys.exit()

edges = cv2.Canny(src, 50, 150)
#먼저 케니함수로 엣지영상을 구한다.
lines = cv2.HoughLinesP(edges, 1, np.pi / 180., 160,
                        minLineLength=50, maxLineGap=5)
#1번째 인자 : edges
#2번째 인자 : rho로 1픽셀간격으로 한다. 보통 기본값
#3번째 인자 : 각도는 1도단위. 보통 기본값
#4번째 인자 : threshold는 160정도
#5번째 인자 : 최소길이 50
#6번째 인자 : 5픽셀정도는 떨어져도 이어라
dst = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
#컬러로 바꿔야 빨간색 직선성분을 표현할 수 있다.
if lines is not None:#혹시 라인이 하나도 검출이 안될수 있다.
    for i in range(lines.shape[0]):#shape의 첫번째가 직선성분의 개수
        pt1 = (lines[i][0][0], lines[i][0][1])  # 시작점 좌표 x,y
        pt2 = (lines[i][0][2], lines[i][0][3])  # 끝점 좌표 x,y
        #가운데 인자는 무조건 0이다. 더미개념
        cv2.line(dst, pt1, pt2, (0, 0, 255), 2, cv2.LINE_AA)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
