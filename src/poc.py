# proof of concept for this ams object detection
import cv2
import cv2.cv as cv
import numpy as np
import Queue

cap = cv2.VideoCapture(0)
cap.set(cv.CV_CAP_PROP_GAIN,0.0)
cap.set(cv.CV_CAP_PROP_EXPOSURE, 0.0)
cap.set(cv.CV_CAP_PROP_FPS, 5)

lower_red = np.array([0,70,70])
upper_red = np.array([30,255,255])
kernel = np.ones((5,5),np.uint8)

radians = np.array([0 for x in range(5)])
positions = np.array([[0,0] for x in range(5)])
mean_position = 0


while(True):
	# capture frame from camera
	ret, frame = cap.read(cv2.CV_LOAD_IMAGE_GRAYSCALE)
	# convert to HSV Map
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
	blurred = cv2.medianBlur(hsv, 55)
	# create mask 
	mask = cv2.inRange(blurred, lower_red, upper_red)

	# find circles
	circles = cv2.HoughCircles(mask, cv.CV_HOUGH_GRADIENT, 4, 500, np.array([]), 500, 100, 20, 300)
	if circles is not None:
		circles = np.round(circles[0, :]).astype("int")
		for (x, y, r) in circles:
			radians[mean_position] = r
			positions[mean_position] = [x, y]
			mean_position = (mean_position +1) % 5
			mean = positions.mean(axis = 0)
			x = int(mean[0])
			y = int(mean[1])
			cv2.circle(frame, (x,y), int(radians.mean()), (0, 255, 0), 4)
			cv2.rectangle(frame, (x - 5, y - 5), (x + 5, y + 5), (0, 128, 255), -1)

	cv2.imshow('VideoWindow', frame)
	cv2.imshow('FrameWindow', mask)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break

cap.release()
cv2.destroyAllWindows()

