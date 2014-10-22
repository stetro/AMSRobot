import cv2
import cv2.cv as cv
import numpy as np
import io
import picamera


class Detection:
	stream = None
	camera = None
	def __init__(self, draw=False, blur=55,width=320,height=240):
		Detection.camera=picamera.PiCamera()
		Detection.camera.resolution = (width, height)
		self.blur=blur
		self.draw = draw
		self.kernel = np.ones((5,5),np.uint8)

	def loop(self):
		raise NotImplementedError()

	def isRunning(self):
		if cv2.waitKey(1) & 0xFF == ord('q'):
			return False
		return True

	def imageCapture(self):
		# capture frame from camera
		Detection.stream = io.BytesIO()
		Detection.camera.capture(Detection.stream, format='jpeg')	
		#convert image into numpy array
		data = np.fromstring(Detection.stream.getvalue(), dtype=np.uint8)
		#turn the array into a cv2 image
		frame = cv2.imdecode(data, 1)
		# convert to HSV Map
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		blurred = cv2.medianBlur(hsv, self.blur)
		# create mask 
		mask = cv2.inRange(blurred, self.lower_color, self.upper_color)
		return (frame, mask)

	def drawWindow(self, frame, mask):
		cv2.imshow('VideoWindow', frame)
		cv2.imshow('FrameWindow', mask)

	def __del__(self):
		Detection.camera.close()
