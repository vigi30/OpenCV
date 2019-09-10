#!/usr/bin/python

# Standard imports
import cv2
import numpy as np;

# Read image
im = cv2.imread("pd.jpg")
im1=im.copy()
im=cv2.medianBlur(im, 5)
im=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
# ret,val=cv2.threshold(im,160,255,cv2.THRESH_BINARY)
# #val=cv2.adaptiveThreshold(im,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,11,2)

# Setup SimpleBlobDetector parameters.
params = cv2.SimpleBlobDetector_Params()

# # Change thresholds
params.minThreshold = 100
params.maxThreshold = 255

# params.filterByColor=1
# params.blobColor = 0


# Filter by Area.
#params.filterByArea = True
params.minArea = 30

# Filter by Circularity
params.filterByCircularity = True
params.minCircularity = 0.396

# # Filter by Convexity
params.filterByConvexity = True
params.minConvexity = 0.750
    
# # Filter by Inertia
params.filterByInertia = True
params.minInertiaRatio = 0.220

# Create a detector with the parameters
ver = (cv2.__version__).split('.')
if int(ver[0]) < 3 :
	detector = cv2.SimpleBlobDetector(params)
else : 
	detector = cv2.SimpleBlobDetector_create(params)


# Detect blobs.
keypoints = detector.detect(im)
print len(keypoints)
for i in range(len(k)):
    x = k[i].pt[0]
    y = k[i].pt[1]
    print "angle of ",i,"is ",k[i].angle
    print "response of ",i,"is ",k[i].response
    print "size of ",i,"is ",k[i].size
    center=(int(x),int(y))
    r=int(k[i].size/2.0)
    
    cv2.circle(im1,center,r,(0,255,0),2)

# Draw detected blobs as red circles.
# cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures
# the size of the circle corresponds to the size of blob

im_with_keypoints = cv2.drawKeypoints(im1, keypoints, np.array([]), (0,0,255),  cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show blobs
cv2.imshow("Keypoints", im_with_keypoints)
cv2.waitKey(0)



