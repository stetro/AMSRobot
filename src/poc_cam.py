import io
import picamera
import cv2

#saving the picture to an in-program stream rather than a file
stream = io.BytesIO()

#to speed things up, lower the resolution of the camera
CAMERA_WIDTH = 320
CAMERA_HEIGHT = 240

with picamera.PiCamera() as camera:
    camera.resolution = (CAMERA_WIDTH, CAMERA_HEIGHT)
    #capture into stream
    camera.capture(stream, format='jpeg')
#convert image into numpy array
data = np.fromstring(stream.getvalue(), dtype=np.uint8)
#turn the array into a cv2 image
image = cv2.imdecode(data, 1)
camera.close()

