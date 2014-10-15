import cv2
import cv2.cv as cv
import numpy as np
from detection.Detection import Detection

class CircleDetection(Detection):
	def __init__(self, draw=False, blur=55):
		# red
		self.lower_color = np.array([0,70,70])
		self.upper_color = np.array([20,255,255])
		Detection.__init__(self, draw, blur)

	def circleDetection(self, mask):
		# find circles
		circles = cv2.HoughCircles(mask, cv.CV_HOUGH_GRADIENT, 4, 500, np.array([]), 500, 100, 20, 300)
		return circles

	def evaluateCircles(self, circles, frame):
		if circles is not None:
			circles = np.round(circles[0, :]).astype("int")
			for (x, y, r) in circles:		
				if(self.draw):
					cv2.circle(frame, (x,y), r ,(0, 255, 0), 4)
					cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
				return (x, y, r)
		else:
			return None

	def loop(self):
		(frame, mask) =self.imageCapture()
		circles = self.circleDetection(mask)
		circle = self.evaluateCircles(circles, frame)
		if(self.draw):
			self.drawWindow(frame, mask)
		return circle