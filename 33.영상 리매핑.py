import sys
import numpy as np
import cv2


src = cv2.imread('tekapo.bmp')

if src is None:
    print('Image load failed!')
    sys.exit()

h, w = src.shape[:2]

map2, map1 = np.indices((h, w), dtype=np.float32)
#map2는 y좌표 인덱스, map1은 x좌표 인덱스
#indice는 그냥 hw의 행렬 인덱스로 변환해주는 함수이다.

map2 = map2 + 10 * np.cos(map1/32 )
#사인함수처럼 출렁이게끔 만든 코드
#Y좌표에다가 sin함수를 넣는데 10픽셀만큼 꿀렁거릴수있게 magnitude를 줬고
#32는 적당한값줘서 여러번 파도가 치게 만들었다.
#32로 안나누면 엄청 촘촘, 큰숫자로 나누면 완만해진다.
print(map2[0:10,0:10])
#왼쪽은 행 오른쪽은 열
dst = cv2.remap(src, map1, map2, cv2.INTER_CUBIC, borderMode=cv2.BORDER_DEFAULT)
#퀄리티를 좋게하기위해 inter_cubic을 줬다.
#보더모드는 디폴트로한다. 영상 바깥쪽에 가상의 픽셀이 있다고 가정하는 것이다. 바깥쪽에 픽셀에 대칭적으로 나타나는 것이다.
cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()

cv2.destroyAllWindows()
