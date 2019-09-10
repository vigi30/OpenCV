import cv2
import numpy as np

def nothing(x):
    pass

drawing = False # true if mouse is pressed
mode = True # if True, draw rectangle. Press 'm' to toggle to curve
ix,iy = -1,-1
r=0
b=0
b=0
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global ix,iy,drawing,mode,r,g,b

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        ix,iy = x,y
        

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            if mode == True:
                cv2.rectangle(img1,(ix,iy),(x,y),(b,g,r),-1)
                #print ix,iy,x,y
            else:
                cv2.circle(img1,(x,y),5,(b,g,r),-1)

    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        if mode == True:
            cv2.rectangle(img1,(ix,iy),(x,y),(b,g,r),-1)
        else:
            cv2.circle(img1,(x,y),5,(b,g,r),-1)

# Create a black image, a window
img = np.zeros((512,512,3), np.uint8)
img1 = np.zeros((512,512,3), np.uint8)
cv2.namedWindow('image')

cv2.namedWindow('image1')


# create trackbars for color change
cv2.createTrackbar('R','image',0,255,nothing)
cv2.createTrackbar('G','image',0,255,nothing)
cv2.createTrackbar('B','image',0,255,nothing)

# create switch for ON/OFF functionality
switch = '0 : OFF \n1 : ON'
cv2.createTrackbar(switch, 'image',0,1,nothing)
cv2.setMouseCallback('image1',draw_circle)

while(1):
    cv2.imshow('image',img)
    cv2.imshow('image1',img1)
    
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k==27:
        break

    # get current positions of four trackbars
    r = cv2.getTrackbarPos('R','image')
    
    g = cv2.getTrackbarPos('G','image')
    
    b = cv2.getTrackbarPos('B','image')
    
    s = cv2.getTrackbarPos(switch,'image')
    
    
    if s == 0:
        img[:] = 0
    else:
        img[:] = [b,g,r]
        #cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

cv2.destroyAllWindows()
