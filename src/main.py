
from detection.Detection import Detection
from detection.SquareDetection import SquareDetection
from detection.CircleDetection import CircleDetection
from Stepper import Stepper
from Driver import Driver

import time

if __name__ == '__main__':
	d=Driver(0.003)
	for i in range(0,10):
		d.forwards()

	circleDetection = CircleDetection(draw=False,width=640 ,height= 480, debug=True)

	while(circleDetection.isRunning()):
		time.sleep(.5)
		(circle, frame) = circleDetection.loop()
		print("circle found: "+str(circle))
		if circle==None:
			for i in range(0,30):
				d.rotateRight()
		elif circle[0] > 400:
			print("YAY!!! left direction")
			for i in range(0,5):
				d.rotateRight()
		elif circle[0] < 266:
			print("YAY!!! right direction")
			for i in range(0,5):
				d.rotateLeft()
		else:
			print("YAY!!! straight direction")
			for i in range(0,100):
				d.forwards()
		if circle != None and circle[2] > 130:
			circleDetection.stop()
			for i in range(0,100):
				d.forwards()

	squareDetection = SquareDetection(draw=False)

	while(squareDetection.isRunning()):
		time.sleep(.5)
		(square, frame) = squareDetection.loop()
		print("square found: "+str(square))
		if len(square) == 0:
			for i in range(0,5):
				d.rotateRight()
