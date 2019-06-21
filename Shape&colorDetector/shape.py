import cv2
import numpy as np

def shape_detector(cnt): 
		
	approx = cv2.approxPolyDP(cnt, 0.04*cv2.arcLength(cnt,True), True)  #approx cause there might be more vertices 
																		#in zoom so we want to approximate ,like circle infinite vertices 
		
	if len(approx) == 3:
		shape = "Triangle"

	elif len(approx) == 4:
		(x,y,w,h) = cv2.boundingRect(approx)
		ar = w/float(h)
		shape = "Square" if (ar >= 0.95 and ar <= 1.05) else "Rectangle"

	elif len(approx) == 5:
		shape = "Pentagon"

	elif len(approx) == 6:
		shape = "Hexagon"

	else:
		shape = "Circle"

	return shape 
