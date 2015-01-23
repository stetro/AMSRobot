import cv2
import cv2.cv as cv
import numpy as np
import io
import picamera


class Detection:
	stream = None
	camera = None
	framecount = 0
	def __init__(self, draw=False, blur=20,width=640,height=480, debug=False):
		if Detection.camera == None:
			Detection.camera=picamera.PiCamera()
			Detection.camera.resolution = (width, height)
			Detection.camera.awb_mode = "tungsten"
		self.debug=debug
		self.running = True
		self.blur=blur
		self.draw = draw
		self.kernel = np.ones((5,5),np.uint8)

	def loop(self):
		raise NotImplementedError()

	def isRunning(self):
		return self.running

	def stop(self):
		self.running = False

	def doDebug(self, frame):
		if self.debug:
			cv2.imwrite("debug%03d.jpg" % Detection.framecount, frame)
			Detection.framecount += 1
	

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

	def __del__(self):
		Detection.camera.close()
