# -*- coding: utf-8 -*-
import numpy as np
import cv2

def nothing(x):
    pass

img = np.ones((600,800,3), dtype=np.uint8)*255
# img.fill(255) ile de beyaz yapılabilir.
# img = np.zeros((400,800,3), np.uint8)
cv2.namedWindow('image')

# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)
cv2.createTrackbar('Radius','image',0,20,nothing)
switch = '0: OFF \n1: ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)

drawing = False # true if mouse is pressed
ix,iy = -1,-1
radius = 0

# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,r,g,b,radius

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.circle(img,(x,y),radius,(b,g,r),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.circle(img,(x,y),radius,(b,g,r),-1)

while 1:
    cv2.imshow('image',img)
    k = cv2.waitKey(1) & 0xFF
    if k == 27:
        break

    r = cv2.getTrackbarPos('R','image')
    g = cv2.getTrackbarPos('G','image')
    b = cv2.getTrackbarPos('B','image')
    radius = cv2.getTrackbarPos('Radius','image')
    s = cv2.getTrackbarPos(switch,'image')
    cv2.setMouseCallback('image',draw_circle)

    # if s == 0:
    #     img[:] = 0

cv2.destroyAllWindows()