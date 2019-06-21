import cv2
import numpy as np
import imutils
import time

def nothing(x):
	pass


img = cv2.imread('test.png')
#cap = cv2.VideoCapture(0)
cv2.namedWindow('Trackbar')

cv2.createTrackbar('low_h',   'Trackbar', 0,   255, nothing)
cv2.createTrackbar('low_s',   'Trackbar', 0,   255, nothing)
cv2.createTrackbar('low_v',   'Trackbar', 0,   255, nothing)
cv2.createTrackbar('high_h',  'Trackbar', 255, 255, nothing)
cv2.createTrackbar('high_s',  'Trackbar', 255, 255, nothing)
cv2.createTrackbar('high_v',  'Trackbar', 255, 255, nothing)
cv2.createTrackbar('erode',   'Trackbar', 0,   255, nothing)
cv2.createTrackbar('dilation','Trackbar', 0,   255, nothing)
cv2.createTrackbar('kernel',  'Trackbar', 0,   255, nothing)





while True:
	
	#_,img = cap.read()

	hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


	low_h  = cv2.getTrackbarPos('low_h', 'Trackbar')
	low_s  = cv2.getTrackbarPos('low_s', 'Trackbar')
	low_v  = cv2.getTrackbarPos('low_v', 'Trackbar')


	high_h = cv2.getTrackbarPos('high_h','Trackbar')
	high_s = cv2.getTrackbarPos('high_s','Trackbar')
	high_v = cv2.getTrackbarPos('high_v','Trackbar')


	low_limit = np.array([low_h,low_s,low_v])
	high_limit = np.array([high_h,high_s,high_v])	    
	mask = cv2.inRange(hsv,low_limit,high_limit)

	blurred = cv2.GaussianBlur(mask, (5,5), 2)
	bit = cv2.bitwise_and(img, img, mask = mask)  

	kernel = np.ones((cv2.getTrackbarPos('kernel','Trackbar'),cv2.getTrackbarPos('kernel','Trackbar')),np.uint8)
	edged = cv2.erode(mask.copy(), kernel, iterations = cv2.getTrackbarPos('erode','Trackbar'))
	edged = cv2.dilate(edged, kernel, iterations = cv2.getTrackbarPos('dilation','Trackbar'))
	edged = cv2.Canny(edged, 45,100)

	#time.sleep(1)

	cnts,hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)

	#cnt = imutils.grab_contours(cnt)
	#time.sleep(1)

	frame = img.copy()
	cv2.drawContours(frame,cnts,-1,(255,0,0),1)
	cv2.imshow('ans',frame)

	if cv2.waitKey(1) & 0xFF == ord('q'):
		break


#cap.release()
cv2.destroyAllWindows()












         
































