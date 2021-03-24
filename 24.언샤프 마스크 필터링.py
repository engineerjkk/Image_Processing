import sys
import numpy as np
import cv2

src = cv2.imread('rose.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()
#1.BGR을 YCrCb 컬러보델로 변환을 해줍니다.
src_ycrcb = cv2.cvtColor(src, cv2.COLOR_BGR2YCrCb)
#2.YCrCb모델의 0번채널, 즉 밝기값만 사용합니다.
src_f = src_ycrcb[:, :, 0].astype(np.float32)
#3.가우시안블러의 내부 파라미터를 채워줍니다. ksize는 기본값으로 sigmax는 2,0을 해줍니다.
blr = cv2.GaussianBlur(src_f, (0, 0), 2.0)
#4.기본 이미지에서 부드러운 이미지를 빼줍니다.
src_ycrcb[:, :, 0] = np.clip(2.0*src_f - blr, 0, 255).astype(np.uint8)
#5.그리고 다시 이미지를 BGR형태로 변환하여 줍니다. 
#입력영상을 두배로 곱한뒤에 빼줍니다. 그렇지 않으면 출력화면이 매우 어둡습니다.
dst = cv2.cvtColor(src_ycrcb, cv2.COLOR_YCrCb2BGR)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
