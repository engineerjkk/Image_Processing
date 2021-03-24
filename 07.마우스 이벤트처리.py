import sys
import numpy as np
import cv2


oldx = oldy = -1

def on_mouse(event, x, y, flags, param):
    #다섯개의 파라미터, param은 안쓸수있지만 안쓰더라도 적어두자. 
    global oldx, oldy

    if event == cv2.EVENT_LBUTTONDOWN:
        oldx, oldy = x,y  #왼쪽버튼이 눌렸을때 old 좌표를 x,y로 세팅을 한다.
        print('EVENT_LBUTTONDOWN: %d, %d' % (x, y))

    elif event == cv2.EVENT_LBUTTONUP:
        print('EVENT_LBUTTONUP: %d, %d' % (x, y))

    elif event == cv2.EVENT_MOUSEMOVE:
        #마우스가 움직일때 키보드가 눌려있는지를 처리한다. 
        if flags & cv2.EVENT_FLAG_LBUTTON:
            #flags라는 인자값이  FLAG_LBUTTON으로 설정돼있는지 확인한다.
            #==을 쓰면 컨트롤키누르면서 움직이면 인식을 못하므로 and 처리한다
            #cv2.EVENT_FLAG_LBUTTON 는 1인데 1과 and가 되면~
            cv2.line(img, (oldx, oldy), (x, y), (0, 0, 255), 4, cv2.LINE_AA)
            #라인타입으로 해야 이전 좌표와 현재좌표를 이어주기때문에 끊김이 없다.
            cv2.imshow('image', img)

            oldx, oldy = x, y


img = np.ones((480, 640, 3), dtype=np.uint8) * 255
#흰색으로 되어있는 컬러 영상

cv2.namedWindow('image')
cv2.setMouseCallback('image', on_mouse, img)
#setMouseCallback은 namedWindow혹은 imshow 이후에 호출해야 한다.
#두번째 인자가 onMouse
cv2.imshow('image', img)
cv2.waitKey()

cv2.destroyAllWindows()

#cv2.circle(img,(x,y),5,(0,0,255)-1)
#이렇게 하면 빨리 마우스를 움직였을때 빈공간이 생기므로 oldX를 쓰자.