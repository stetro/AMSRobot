
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
#	squareDetection = SquareDetection(draw=False)
	circleDetection = CircleDetection(draw=False,width=640 ,height= 480)



	while(circleDetection.isRunning()):
		time.sleep(.5)
		(circle, frame) = circleDetection.loop()
		if circle==None:
			for i in range(0,30):
				d.rotateRight()
		elif circle[1] > 300:
			for i in range(0,5):
				d.rotateLeft()
		elif circle[1] < 200:
			for i in range(0,5):
				d.rotateRight()
		else:
			print("Found!!! YAY")
			for i in range(0,100):
				d.forwards()

		print(str(circle))

#	while(squareDetection.isRunning()):
#		time.sleep(.5)
#		(square, frame) = squareDetection.loop()
