import numpy as np
import cv2


def on_level_change(pos):
    #pos는 정수값을 받는 인자.
    value = pos * 
    16#그레이 스케일레벨을 16씩 증가하도록 한다. 
    #if value >= 255:
     #   value = 255

    
    #fill 함수를 사용해도 됨.
    value=np.clip(value,0,255)
    #레벨 최소를 0으로 최대를 255으로 세팅하는 클립함수입니다.
    #0보다 작은건 무조건 0, 255보다 큰건 무조건 255로 세팅해줍니다.
    img[:] = value  
    # img 영상 모든값에 세팅을 합니다.
    cv2.imshow('image', img)



img = np.zeros((480, 640), np.uint8)
cv2.namedWindow('image')
cv2.createTrackbar('level', 'image', 0, 16, on_level_change)
#트랙바는 반드시 창이 생성된 이후인 namedWindow 이후에 써야한다.
#namedWindow를 안쓸거면아니면 적어도 imshow뒤엔써야한다.
#level 이름의 image 창에 만들고, 초기치는 0, 트랙바최댓값 16,콜백함수이름->
#변경됐을때 onlevel_change함수를 호출해줘라
cv2.imshow('image', img)
cv2.waitKey()
cv2.destroyAllWindows()
