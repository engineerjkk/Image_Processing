import sys
import numpy as np
import cv2


# 입력 영상에서 ROI를 지정하고, 히스토그램 계산

src = cv2.imread('cropland.png')

if src is None:
    print('Image load failed!')
    sys.exit()

x, y, w, h = cv2.selectROI(src)
#마우스를 이용해서 드레그할수있다. 사각형정보형태로 리턴이 된다. 
#비슷한 모든 컬러를 보여줄 수 있다.
#-------------------------------------------------히스토그램 계산코드
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
#YCrCb로 변환한다.
crop = src_ycrcb[y:y+h, x:x+w]#사용자가 선택한 사각형 영역의 부분영상만 추출을 합니다.

channels = [1, 2] #Y성분인 0번채널은 쓰지 않는다. 그레이값이기때문, 조명을 무시하기 위함
cr_bins = 128 #256해도 무방
cb_bins = 128
histSize = [cr_bins, cb_bins]
cr_range = [0, 256] #256까지 써야 256제외한 255까지 인식을 한다.
cb_range = [0, 256]
ranges = cr_range + cb_range #0 256 0 256

hist = cv2.calcHist([crop], channels, None, histSize, ranges)
#----------------------------------------------------히스토그램 계산코드
hist_norm = cv2.normalize(cv2.log(hist+1), None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)

# 입력 영상 전체에 대해 히스토그램 역투영

backproj = cv2.calcBackProject([src_ycrcb], channels, hist, ranges, 1)
#calcBackProject로 내가 원하는 들판영역사진을 골라낸다.
dst = cv2.copyTo(src, backproj)

cv2.imshow('backproj', backproj)
cv2.imshow('hist_norm', hist_norm)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

#HSV는 색상을 휴값을 이용해 숫자로 색상을 표현하기 좋을때 사용
#YCbCr 임의의 컬러를 가져올때