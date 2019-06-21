import cv2
import numpy as np 

#edge detector
cap = cv2.VideoCapture(0)

while True:
	ret,img = cap.read()
	cimg = cv2.Canny(img,100,200)
	cv2.imshow('45',cimg)
	cv2.imshow('45-color',img)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()
"""
#print img and save it with different name
img = cv2.imread('campus.jpg',1)
cv2.imshow('campus',img)
k=cv2.waitKey(0)
if k==27 :
	cv2.destroyAllWindows() 
elif k == ord('s'):
	cv2.imwrite('iitg.png',img)
	cv2.destroyAllWindows() 


# capture frame and print 
cap=cv2.VideoCapture(0)
ret,frame=cap.read()
print (ret)
print (frame)
cv2.imshow('image',frame)
cv2.waitKey(0)
cap.release()

#video color to gray
cap = cv2.VideoCapture(0#for web cam , servo.mp4#for video)
while(True#for cam cap.isOpened()#for recorded video playing):
	ret,frame=cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	cv2.imshow('image',gray)
	
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cap.release()
cv2.destoryAllWindows()
"""
"""
#resize and draw and write text on img
img = cv2.imread('messi1.jpg',1)

#cv2.line(img,(0,0),(150,150),(255,255,0),15)
res = cv2.resize(img,None,fx=0.5, fy=0.5, interpolation = cv2.INTER_CUBIC	)
#height, width = img.shape[:2]
#res = cv2.resize(img,(2*width, 2*height), interpolation = cv2.INTER_CUBIC)

#pts = np.array([[10,105],[201,301],[70,600],[500,10]])
#pts = pts.reshape((4,1,2))
#cv2.polylines(res,[pts],True,(0,255,255))

#cv2.rectangle(res,(10,10),(300,150),(0,255,255),15)
#cv2.circle(res,(100,63), 55, (0,255,0), -1)
#font = cv2.FONT_HERSHEY_COMPLEX
#cv2.putText(res,'OpenCV',(25,100), font, 2,(255,255,255),1,cv2.LINE_AA)
cv2.imshow('messi1',res)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""

"""
#for rotation and translation

img = cv2.imread('messi.jpg',-1)
#rows,cols = img.shape[:2]

#M = np.float32([[1,0,10],[0,1,100]])
#dst1 = cv2.warpAffine(img,M,(cols,rows))


 #For rotation
img = cv2.imread('messi.jpg',-1)
rows,cols = img.shape[:2]

M1 = cv2.getRotationMatrix2D((cols/3,rows/3),180,2)
dst = cv2.warpAffine(img,M1,(cols,rows))
cv2.imshow('img',img)
#cv2.imshow('dst1',dst1)
cv2.imshow('dst',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""

"""
#for image

im = cv2.imread('45.png')
img = cv2.Canny(im,100,200)

#imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
cv2.imshow('gray',img)
ret,thresh = cv2.threshold(img,127,255,0)
cv2.imshow('thr',thresh)
#image, contours, hierarchy = cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cv2.waitKey(0)
"""
