# proof of concept for this ams object detection
import cv2
import cv2.cv as cv
import numpy as np
import time


class Detection:
	cap = None
	def __init__(self, draw=False, blur=55):
		self.blur=blur
		self.draw = draw

		if Detection.cap is None:
			Detection.cap = cv2.VideoCapture(0)
			Detection.cap.set(cv.CV_CAP_PROP_GAIN,0.0)
			Detection.cap.set(cv.CV_CAP_PROP_EXPOSURE, 0.0)
			Detection.cap.set(cv.CV_CAP_PROP_FPS, 1)
		self.kernel = np.ones((5,5),np.uint8)

	def loop(self):
		raise NotImplementedError()

	def isRunning(self):
		if cv2.waitKey(1) & 0xFF == ord('q'):
			return False
		return True

	def imageCapture(self):
		# capture frame from camera
		ret, frame = Detection.cap.read(cv2.CV_LOAD_IMAGE_GRAYSCALE)
		# convert to HSV Map
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		blurred = cv2.medianBlur(hsv, self.blur)
		# create mask 
		mask = cv2.inRange(blurred, self.lower_color, self.upper_color)
		return (frame, mask)

	def drawWindow(self, frame, mask):
		cv2.imshow('VideoWindow', frame)
		cv2.imshow('FrameWindow', mask)


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
		(frame, mask) =circleDetection.imageCapture()
		circles = circleDetection.circleDetection(mask)
		circle = circleDetection.evaluateCircles(circles, frame)
		if(self.draw):
			circleDetection.drawWindow(frame, mask)
		return circle

class SquareDetection(Detection):
	def __init__(self, draw=False, blur=31):
		# green
		self.lower_color = np.array([60,70,70])
		self.upper_color = np.array([90,255,255])
		Detection.__init__(self, draw, blur)

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
			if self.draw:
				cv2.drawContours(frame,result,0,(0,255,0),2)
			return result
		else:
			return None

	def loop(self):
		(frame, mask) =squareDetection.imageCapture()
		squares = squareDetection.squareDetection(mask)
		square = squareDetection.evaluateSquares(squares, frame)
		if(self.draw):
			squareDetection.drawWindow(frame, mask)
		return square


if __name__ == '__main__':
	squareDetection = SquareDetection(draw=True)
	circleDetection = CircleDetection(draw=True)

	while(circleDetection.isRunning()):
		time.sleep(.5)
		circle = circleDetection.loop()

	while(squareDetection.isRunning()):
		time.sleep(.5)
		square = squareDetection.loop()




		

