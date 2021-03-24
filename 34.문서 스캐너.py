import sys
import numpy as np
import cv2


def drawROI(img, corners):
    cpy = img.copy() #일단 복사본을 하나 만든다. 그리고 그 위에만들거다.

    c1 = (192, 192, 255)#옅은 빨강
    c2 = (128, 128, 255)#좀더 어두운 빨강

    for pt in corners:
        cv2.circle(cpy, tuple(pt), 25, c1, -1, cv2.LINE_AA)
        #-1을 통해 원의 내부를 채운다.

    cv2.line(cpy, tuple(corners[0]), tuple(corners[1]), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[1]), tuple(corners[2]), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[2]), tuple(corners[3]), c2, 2, cv2.LINE_AA)
    cv2.line(cpy, tuple(corners[3]), tuple(corners[0]), c2, 2, cv2.LINE_AA)
    #네개의 모서리 점을 잇는 직선이다.
    #점들의 좌표는 튜플로 묶어둔다.코너 0,1,2,3이 ndarray라서 그냥넘기면 에러가난다.
    disp = cv2.addWeighted(img, 0.3, cpy, 0.7, 0)
    #입력영상에다가 만든 cpy를 addWeighted로 합성을 한다.
    #그래서 핑크색 부분이 배경도 살짝 보이게 된다. 
    return disp


def onMouse(event, x, y, flags, param):
    #오픈시비에서 제공하는 콜백함수이므로 5개의 파라메타를 따라야한다.
    #flags는 상태
    
    global srcQuad, dragSrc, ptOld, src

    if event == cv2.EVENT_LBUTTONDOWN: #클릭했을때
        for i in range(4):
            if cv2.norm(srcQuad[i] - (x, y)) < 25:
                #이미 저장된 네개 모서리점의 좌표 네개와 지금 클릭한 좌표의 거리가 25보다 작은지 체크한다. 동그라미 안에 들어왔는지.
                dragSrc[i] = True
                #몇번째냐 드레그를 true로 설정
                ptOld = (x, y)
                #마우스를 조금씩 이동할때마다 변위를 알아야한다.
                break

    if event == cv2.EVENT_LBUTTONUP:#드레그를 떼면
        for i in range(4):
            dragSrc[i] = False #초기화

    if event == cv2.EVENT_MOUSEMOVE: #마우스 왼쪽이 눌려있는 상태에서만 체크
        for i in range(4):
            if dragSrc[i]: #dragsrc가 트루일 경우에만
                dx = x - ptOld[0] #현재점의 x좌표와 이전점의 x좌표로 변위 계산
                dy = y - ptOld[1]

                srcQuad[i] += (dx, dy) #그것만큼 모서리 좌표로 이동을 해준다.ㅈ

                cpy = drawROI(src, srcQuad) #이동한 결과를 drawROI로 호출을 한다.
                cv2.imshow('img', cpy)
                ptOld = (x, y)
                break


# 입력 이미지 불러오기
src = cv2.imread('scanned.jpg')

if src is None:
    print('Image open failed!')
    sys.exit()
src = cv2.pyrDown(src)

# 입력 영상 크기 및 출력 영상 크기
h, w = src.shape[:2]
#입력영상의 세로와 가로 크기를 받는다.

dw = 500
#똑바로 폈을때 A4가로크기를 500으로 가정
dh = round(dw * 297 / 210)  # A4 용지 크기: 210x297cm
#A4용지의 비율을 이용해서 세로크기 지정

# 모서리 점들의 좌표, 드래그 상태 여부
srcQuad = np.array([[30, 30], [30, h-30], [w-30, h-30], [w-30, 30]], np.float32)
#내가 선택하려고 하는 모서리 네개의 ndarray 
#일단 초기점의 좌표이다. 이건 마우스이벤트 처리하면서 변경한다. 반시계방향으로
dstQuad = np.array([[0, 0], [0, dh-1], [dw-1, dh-1], [dw-1, 0]], np.float32)
#출력영상의 모서리 위치이다.
dragSrc = [False, False, False, False]

# 모서리점, 사각형 그리기
disp = drawROI(src, srcQuad)
#입력영상과 내가 선택한 쿼드를 drawROI 함수를 통해 disp에 전송한다.

cv2.imshow('img', disp)
cv2.setMouseCallback('img', onMouse)

while True:
    key = cv2.waitKey()
    if key == 13:  # ENTER 키
        break#엔터키를 누르면 빠져나와서 투시변환과 결과영상 진행
    elif key == 27:  # ESC 키
        cv2.destroyWindow('img')#ESC를 누르면 전체 시스템을 종료한다.
        sys.exit()

# 투시 변환
pers = cv2.getPerspectiveTransform(srcQuad, dstQuad)
#3x3 투시변환 행렬이 리턴이 된다.
dst = cv2.warpPerspective(src, pers, (dw, dh), flags=cv2.INTER_CUBIC)

# 결과 영상 출력
#cv2.namedWindow('dst', cv2.WINDOW_NORMAL)
#노말이 안된다.
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()
