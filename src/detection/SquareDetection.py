import cv2
import cv2.cv as cv
import numpy as np
from detection.Detection import Detection

class SquareDetection(Detection):
	def __init__(self, draw=False, blur=31, width=640, height=480, debug=False):
		# blue color mask in HSV space (also constrains heu and satuation)
		self.lower_color = np.array([80, 50, 50], dtype=np.uint8)
		self.upper_color = np.array([120,255,255], dtype=np.uint8)
		Detection.__init__(self, draw, blur, width, height, debug)

	def squareDetection(self, mask):
		contours, hier = cv2.findContours(mask,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
		return contours

	def evaluateSquares(self, contours, frame):
		if contours is not None:
			result = []
			for cnt in contours:
			    if cv2.contourArea(cnt) > 5000:  # remove small areas like noise etc
			        hull = cv2.convexHull(cnt)    # find the convex hull of contour
			        hull = cv2.approxPolyDP(hull,0.1*cv2.arcLength(hull,True),True)
			        if len(hull) == 4:
			        	result.append(hull)	
			if self.draw or self.debug:
				cv2.drawContours(frame,result,0,(0,255,0),2)
				self.doDebug(frame)
			return result
		else:
			return None

	def loop(self):
		(frame, mask) =self.imageCapture()
		squares = self.squareDetection(mask)
		square = self.evaluateSquares(squares, frame)
		if(self.draw):
			self.drawWindow(frame, mask)
		return (square, frame)
