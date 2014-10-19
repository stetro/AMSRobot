import cv2
import cv2.cv as cv
import numpy as np

class Detection:
	cap = None
	def __init__(self, draw=False, blur=55):
		self.blur=blur
		self.draw = draw
		if Detection.cap is None:
			Detection.cap = cv2.VideoCapture(0)
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
