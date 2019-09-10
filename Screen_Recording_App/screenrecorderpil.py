import numpy as np
import cv2
from PIL import ImageGrab
import ctypes
from mss.windows import MSS as mss
sct = mss()


user32 = ctypes.windll.user32
user32.SetProcessDPIAware()
[sysw, sysh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)]


drawing = False # true if mouse is pressed

cix,ciy = -1,-1

sysx=0
sysy=0
cw=0
ch=0
# mouse callback function
def draw_circle(event,x,y,flags,param):
    global cix,ciy,drawing,cw,ch

    if event == cv2.EVENT_LBUTTONDOWN:
        drawing = True
        cix,ciy = x,y
        

    elif event == cv2.EVENT_MOUSEMOVE:
        if drawing == True:
            cv2.rectangle(crop_img_np,(cix,ciy),(x,y),(0,255,0),1)
            #cv2.imshow("new img",crop_img_np)


    elif event == cv2.EVENT_LBUTTONUP:
        drawing = False
        cv2.rectangle(crop_img_np,(cix,ciy),(x,y),(0,255,0),1)
        cw=x-cix + 1 
        ch=y-ciy + 1
        cv2.imshow("new img",crop_img_np)
        
        
        
        
cv2.namedWindow('image1')
cv2.setMouseCallback('image1',draw_circle)


#print cw,ch,cix,ciy       


# while(True):
    # crop_img = ImageGrab.grab(bbox=(sysx,sysy , sysw, sysh))
    # crop_img_np = np.array(crop_img)
    # cv2.imshow('image1', crop_img_np)
    # vid.write(crop_img_np)
    # print cw,ch,cix,ciy
    # key = cv2.waitKey(1)
    # if key == 27:
        # break
flag=1    
while(True):

    monitor = {'top': sysx, 'left': sysy, 'width': sysw, 'height': sysh}
    crop_img_np = np.array(sct.grab(monitor))
    
    if flag == 1:
        cv2.imshow('image1', crop_img_np)
        flag = 0
        
    #print cw,ch,cix,ciy
 
    key = cv2.waitKey(1)
    if key == 27:
         break  

fourcc = cv2.VideoWriter_fourcc('X','V','I','D') #you can use other codecs as well.
vid = cv2.VideoWriter('recorrrd.wmv', fourcc, 8, (cw-cix,ch-ciy))    
while(True):
    img = ImageGrab.grab(bbox=(cix, ciy, cw, ch)) #x, y, w, h
    img_np = np.array(img)
    frame = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    vid.write(frame)
    cv2.imshow("cropped_image", frame)
    k= cv2.waitKey(1) & 0xFF
    if k == 27:
        break    
        
vid.release()
        

cv2.destroyAllWindows()
