import cv2
import numpy as np 
import imutils


img = cv2.imread('test.png')
hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
img1 = img.copy()
img2=cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)


#low_limit = np.array([0,109,69])

low_limit = np.array([10,108,108])
high_limit = np.array([255,255,255])	    
mask = cv2.inRange(hsv,low_limit,high_limit)

blurred = cv2.GaussianBlur(mask, (5,5), 2)
bit = cv2.bitwise_and(img, img, mask = mask)  

kernel = np.ones((0,0),np.uint8)
edged = cv2.erode(mask.copy(), kernel, iterations = 12)
edged = cv2.dilate(edged, kernel, iterations = 12)
edged = cv2.Canny(edged, 45,100)

#time.sleep(1)

cnts,hierarchy = cv2.findContours(edged, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)

#cnt = imutils.grab_contours(cnt)
#time.sleep(1)

frame = img.copy()
cv2.drawContours(frame,cnts,-1,(255,0,0),1)
cv2.imshow('ans',frame)

cv2.waitKey(0)

#hsv1 = cv2.cvtColor(bit,cv2.COLOR_BGR2HSV

#lowercolor = np.array([12,70,0])
#uppercolor = np.array([19,171,250])


lowercolor = np.array([0,87,88])
uppercolor = np.array([60,165,193])
#mask_base = cv2.inRange(hsv1, lowercolor, uppercolor)
#res_base = cv2.bitwise_and(img, img, mask = mask_base)

#edged1 = cv2.Canny(mask_base,45,100)



at = 0

for c in cnts:
	#output = 'N'

	at = cv2.contourArea(c)
	pe = cv2.arcLength(c,True)
	#print(at)
	if(int(at)>25):

		x, y, w, h = cv2.boundingRect(c)

		cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),1)


		mask = np.zeros(img2.shape,np.uint8)      #Mask to seperate one Chips at a time
		cv2.drawContours(mask,[c],0,255,-1)      
		
		ans=cv2.bitwise_and(img1, img1, mask=mask)
		ans1=ans.copy()
		hsv1=cv2.cvtColor(ans,cv2.COLOR_BGR2HSV)
		#hsv2=cv2.cvtColor(ans,cv2.COLOR_BGR2HSV)
		msk1=cv2.inRange(hsv1,lowercolor,uppercolor)
 

		cnts1,hierarchy = cv2.findContours(msk1, cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)

		a1 = 0 
		
		for cnt in cnts1 :                                                                      

			#p = cv2.arcLength(cnt,True)     
			a = cv2.contourArea(cnt)
			a1 += a
			#print(a1)

		output = 'N'

		if (float((at - a1)/at)>0.68):
			#print(((at - a1)/at))
			output = ' Y '
		elif (float((at - a1)/at)<=0.68):
			output = ' N '


		cv2.putText(img, output, (x, y), cv2.FONT_ITALIC,1, (255, 0, 0), 1)

#bit1 = cv2.bitwise_and(img, img, mask = msk1) 
#cv2.imshow('ok',bit1)
cv2.imshow('final',img)
cv2.waitKey(0)




