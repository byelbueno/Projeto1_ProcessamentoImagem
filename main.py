import numpy as np
import cv2

car_cascade = cv2.CascadeClassifier('haarcascade_fullbody.xml')
# upper_body_cascade = cv2.CascadeClassifier('haarcascade_upperbody.xml')
# lower_body_cascade = cv2.CascadeClassifier('haarcascade_lowerbody.xml')

cv2.namedWindow('preview')
cv2.resizeWindow('preview', 850, 620)
# cap = cv2.VideoCapture('https://cdn-004.whatsupcams.com/hls/hr_pula01.m3u8')
# cap = cv2.VideoCapture('https://videos-3.earthcam.com/fecnetwork/hdtimes10.flv/chunklist_w246511400.m3u8?t=vBci5OreTDT5OVZWlrH3hFWPpk6y83Y18ohQ4H190JNbgw3s6eommZ%2Baea9wIU1Rl0wJhOIU2MBD4afEiFs6RQ%3D%3D&td=202411060711')
# cap = cv2.VideoCapture(0)
cap = cv2.VideoCapture('https://videos-3.earthcam.com/fecnetwork/AbbeyRoadHD1.flv/chunklist_w69949949.m3u8')

x = 100
vx = 10

while True:
    _, frame = cap.read()
    frame = cv2.resize(frame, (850, 620))
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cars = car_cascade.detectMultiScale(gray, 1.1, 2)

    for (x,y,w,h) in cars:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,255),2)


    font = cv2.FONT_HERSHEY_SIMPLEX

    # org
    org = (50, 50)

    # fontScale
    fontScale = 1

    # Blue color in BGR
    color = (255, 0, 0)

    # Line thickness of 2 px
    thickness = 2

    # Using cv2.putText() method
    image = cv2.putText(frame, f"Quantidade de pessoas: {len(cars)}", org, font, 
                      fontScale, color, thickness, cv2.LINE_AA)

    cv2.imshow('preview', frame)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        break
