import sys
import numpy as np
import cv2


# 녹색 배경 동영상
cap1 = cv2.VideoCapture('woman.mp4')

if not cap1.isOpened():
    print('video open failed!')
    sys.exit()

# 비오는 배경 동영상
cap2 = cv2.VideoCapture('raining.mp4')

if not cap2.isOpened():
    print('video open failed!')
    sys.exit()

# 두 동영상의 크기, FPS는 같다고 가정
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
print('frame_cnt1:', frame_cnt1)
print('frame_cnt2:', frame_cnt2)

fps = cap1.get(cv2.CAP_PROP_FPS)
delay = int(1000 / fps)
#두개 프레임사이의 간격 알기
# 합성 여부 플래그
do_composit = False
#True면 합성을 하고 거짓이면 합성을 하지 않는다.
# 전체 동영상 재생
while True:
    ret1, frame1 = cap1.read()
    #한장한장의 프레임을 frame1으로 받는다.
    if not ret1:
        break
    
    # do_composit 플래그가 True일 때에만 합성 아래에서 스페이스바를 통해 합성을 왔다갔다 하기 위해서임.
    if do_composit: #do_composit이 트루면,
        ret2, frame2 = cap2.read()

        if not ret2:
            break

        #frame2=cv2.resize(frame2,(w,h)) ->만약 웹캠으로 할경우 마스크와 내 웹캠의 사이즈를 맞추어야 하므로 리사이즈 해주어야합니다.  

        # HSV 색 공간에서 녹색 영역을 검출하여 합성
        hsv = cv2.cvtColor(frame1, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (50, 150, 0), (70, 255, 255))
        #마스크영상 제작
        cv2.copyTo(frame2, mask, frame1)
        #마스크가 흰색으로 되어있는 부분만 frame1(여자)으로 복사를 해라.
        #frame2 비오는 동영상
   
    cv2.imshow('frame', frame1)
    key = cv2.waitKey(delay)

    # 스페이스바를 누르면 do_composit 플래그를 변경
    # 스페이스를 눌러서 true와 false를 왔다갔다 한다.
    if key == ord(' '):
        do_composit = not do_composit
    elif key == 27:
        break
    #아무것도 누르지 않으면 true문에서 계속돌아 다음영상을 받는다.

cap1.release()
cap2.release()
cv2.destroyAllWindows()
