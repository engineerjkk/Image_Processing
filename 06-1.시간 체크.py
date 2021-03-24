import sys
import time
import numpy as np
import cv2


img = cv2.imread('hongkong.jpg')

tm = cv2.TickMeter()
#TickMeter를 통해 tm이라는 객체를 생성한다.

tm.reset() 
tm.start()
t1 = time.time()

edge = cv2.Canny(img, 50, 150)

tm.stop()

ms=tm.getTimeMilli()
print('time:', (time.time() - t1) * 1000)
print('Elapsed time: {}ms.'.format(ms))


#tm.start와 tm.stop으로 시간측정하는 방법과
#t1=time.time()과 t2=time.time()를 선언해놓고 둘의 차이를 빼는 방법도 있다.
# 하지만 이건 마이크로sec임을 유의! 
#but import time을 선언해야한다.
#그리고 시간연산은 한번만하지말고 for loop를 돌려서 20번정도해서 평균내는게 안정하다.