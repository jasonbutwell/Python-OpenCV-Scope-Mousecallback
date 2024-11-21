#!/bin/python3
import cv2

mouseX = -1
mouseY = -1
mouseC = False

def mousey(event, x, y,flags, param):
        global mouseX, mouseY, mouseC
        if event == cv2.EVENT_LBUTTONDOWN:
                mouseX, mouseY, mouseC = x,y, True

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT,1080)

while cap.isOpened():
        ret,frame = cap.read()
        cv2.namedWindow("Microscope", cv2.WINDOW_NORMAL)
        cv2.setWindowProperty("Microscope", cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
        cv2.imshow('Microscope',frame)
        cv2.setMouseCallback('Microscope',mousey)

        if mouseC == True:
                break

        if cv2.waitKey(1) & 0xFF == ord('q'):
                break

cap.release()
cv2.destroyAllWindows()

cursor.show()