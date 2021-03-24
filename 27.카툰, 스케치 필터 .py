# 카툰 필터 카메라

import sys
import numpy as np
import cv2


def cartoon_filter(img):
    h, w = img.shape[:2]
    img2 = cv2.resize(img, (w//2, h//2))
    #img자체를 리사이즈 해준다. 가로세로가 반으로 줄어든다. 
    #그러면 처리속도가 더 빨라진다. 단순화는 더 커지고, 
    blr = cv2.bilateralFilter(img, -1, 20, 7)
    #일단 블러영상을 준다.좀과도하게 하기위해 20과 7을 준다.
    edge = 255 - cv2.Canny(img, 50, 120)
    #엣지영상은 캐니를 준다. 입력영상 그대로 줘도 내부에서 그레이스케일로변환해서 케니엣지검출을 해준다.
    #파라미터는 80~120정도 준다.
    #이 값들을 255에서 빼도록하자
    
    edge = cv2.cvtColor(edge, cv2.COLOR_GRAY2BGR)
    #다시 컬러영상으로 변환을 해준다.

    dst = cv2.bitwise_and(blr, edge)
    #and 연산
    dst = cv2.resize(dst, (w, h), interpolation=cv2.INTER_NEAREST)
    #위에서 리사이즈를 한걸 다시 원래대로 돌아온다.
    #interpolation으로 옵션을 주면 더 급격한느낌이있다. 좀더 단순화된형태이다. 이걸안쓰면 블러가 된다. 
    return dst

#어두운쪽 엣지를 어둡게 하고 밝은쪽은 흰색으로 하면 스케치 느낌이 있다.
#그레이스케일 영상과 가우시안 영상을 나누어준다.
def pencil_sketch(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    blr = cv2.GaussianBlur(gray, ( 0, 0), 3)
    #마스크는 디폴트, 표준편차는 3정도로 준다. 
    dst = cv2.divide(gray, blr, scale=255)
    #그레이를 블러로 나눈다. 
    dst=cv2.cvtColor(dst,cv2.COLOR_GRAY2BGR)
    return dst


cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print('video open failed!')
    sys.exit()

cam_mode = 0

while True:
    ret, frame = cap.read()

    if not ret:
        break

    if cam_mode == 1:
        frame = cartoon_filter(frame)
    elif cam_mode == 2:
        frame = pencil_sketch(frame)
        frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    cv2.imshow('frame', frame)
    key = cv2.waitKey(1)

    if key == 27:
        break
    elif key == ord(' '):
        cam_mode += 1
        if cam_mode == 3:
            cam_mode = 0
#모드가 3보다 커지면 다시 0번 모드로

cap.release()
cv2.destroyAllWindows()
