#!/usr/bin/env python3

import cv2
import time
cap=cv2.VideoCapture(0)

while True:
    _,source=cap.read()
    cv2.imshow("source",source)
    gray=cv2.cvtColor(source,cv2.COLOR_RGB2GRAY)
    _,result=cv2.threshold(gray,128,255,cv2.THRESH_BINARY)
    cv2.imshow("result",result)
    time.sleep(0.1)
    cv2.waitKey(1)
