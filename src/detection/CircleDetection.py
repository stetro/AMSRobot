import cv2
import cv2.cv as cv
import numpy as np
from detection.Detection import Detection

class CircleDetection(Detection):
	def __init__(self, draw=False, blur=55, width=640, height=480, debug=False):
		# orange color mask in HSV space (also constrains heu and satuation)
		self.lower_color = np.array([15,70,90])
		self.upper_color = np.array([35,200,200])
		Detection.__init__(self, draw, blur, width, height, debug)

	def circleDetection(self, mask):
		# find circles
		circles = cv2.HoughCircles(mask, cv.CV_HOUGH_GRADIENT, 4, 500, np.array([]), 500, 100, 20, 300)
		return circles

	def evaluateCircles(self, circles, frame):
		if circles is not None:
			circles = np.round(circles[0, :]).astype("int")
			for (x, y, r) in circles:		
				cv2.circle(frame, (x,y), r ,(0, 255, 0), 4)
				cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
				self.doDebug(frame)
				return (x, y, r)
		else:
			self.doDebug(frame)
			return None

	def loop(self):
		(frame, mask) =self.imageCapture()
		circles = self.circleDetection(mask)
		circle = self.evaluateCircles(circles, frame)
		if(self.draw):
			self.drawWindow(frame, mask)
		return (circle, frame)
