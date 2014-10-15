# proof of concept for this ams object detection
import cv2
import cv2.cv as cv
import numpy as np
import time



class Detection:
	def __init__(self, draw=False):
		raise NotImplementedError()

	def loop(self):
		raise NotImplementedError()

	def isRunning(self):
		if cv2.waitKey(1) & 0xFF == ord('q'):
			return False
		return True


class CircleDetection(Detection):
	def __init__(self, draw=False):
		self.draw = draw
		self.cap = cv2.VideoCapture(0)
		self.cap.set(cv.CV_CAP_PROP_GAIN,0.0)
		self.cap.set(cv.CV_CAP_PROP_EXPOSURE, 0.0)
		self.cap.set(cv.CV_CAP_PROP_FPS, 1)

		self.lower_red = np.array([0,70,70])
		self.upper_red = np.array([20,255,255])
		self.kernel = np.ones((5,5),np.uint8)
		
		# MEAN VALUES
		#self.radians = np.array([0 for x in range(5)])
		#self.positions = np.array([[0,0] for x in range(5)])
		#self.mean_position = 0

	def imageCapture(self):
		# capture frame from camera
		ret, frame = self.cap.read(cv2.CV_LOAD_IMAGE_GRAYSCALE)
		# convert to HSV Map
		hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
		blurred = cv2.medianBlur(hsv, 55)
		# create mask 
		mask = cv2.inRange(blurred, self.lower_red, self.upper_red)
		return (frame, mask)

	def circleDetection(self, mask):
		# find circles
		circles = cv2.HoughCircles(mask, cv.CV_HOUGH_GRADIENT, 4, 500, np.array([]), 500, 100, 20, 300)
		return circles

	def evaluateCircles(self, circles, frame):
		if circles is not None:
			circles = np.round(circles[0, :]).astype("int")
			for (x, y, r) in circles:
				
				# MEAN VALUES
				#self.radians[self.mean_position] = r
				#self.positions[self.mean_position] = [x, y]
				#self.mean_position = (self.mean_position +1) % 5
				#mean = self.positions.mean(axis = 0)
				#x = int(mean[0])
				#y = int(mean[1])
				#r = int(self.radians.mean())

				if(self.draw):
					cv2.circle(frame, (x,y), r ,(0, 255, 0), 4)
					cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)
				return (x, y, r)
		else:
			return None

	def drawWindow(self, frame, mask):
		cv2.imshow('VideoWindow', frame)
		cv2.imshow('FrameWindow', mask)

	def loop(self):
		(frame, mask) =circleDetection.imageCapture()
		circles = circleDetection.circleDetection(mask)
		circle = circleDetection.evaluateCircles(circles, frame)
		if(self.draw):
			circleDetection.drawWindow(frame, mask)
		return circle

	def __del__(self):
		self.cap.release()
		cv2.destroyAllWindows()


if __name__ == '__main__':
	circleDetection = CircleDetection(draw=True)
	while(circleDetection.isRunning()):
		time.sleep(.5)
		circle = circleDetection.loop()
		print circle


		

