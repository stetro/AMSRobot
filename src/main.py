
from detection.Detection import Detection
from detection.SquareDetection import SquareDetection
from detection.CircleDetection import CircleDetection

import time

if __name__ == '__main__':
	squareDetection = SquareDetection(draw=True)
	circleDetection = CircleDetection(draw=True)

	while(circleDetection.isRunning()):
		time.sleep(.5)
		circle = circleDetection.loop()

	while(squareDetection.isRunning()):
		time.sleep(.5)
		square = squareDetection.loop()
