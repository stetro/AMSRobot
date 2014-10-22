import string,cgi,time
from os import curdir, sep
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from SocketServer import ThreadingMixIn
from detection.Detection import Detection
from detection.SquareDetection import SquareDetection
from detection.CircleDetection import CircleDetection
import cv
import re
import time

circleDetection = CircleDetection(draw=False)
(circle, img) = circleDetection.loop()
cameraQuality=75
class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global cameraQuality
        try:
            self.path=re.sub('[^.a-zA-Z0-9]', "",str(self.path))
	    print self.path
            if self.path=="" or self.path==None or self.path[:1]==".":
                return
            if self.path.endswith(".mjpeg"):
		print ".mjpeg"
                self.send_response(200)
                self.wfile.write("Content-Type: multipart/x-mixed-replace; boundary=--aaboundary")
                self.wfile.write("\r\n\r\n")
                while 1:
                    #time.sleep(.5)
                    (circle, img) = circleDetection.loop()
                    img = cv.fromarray(img)
                    cv2mat=cv.EncodeImage(".jpeg",img,(cv.CV_IMWRITE_JPEG_QUALITY,cameraQuality))
                    JpegData=cv2mat.tostring()
                    self.wfile.write("--aaboundary\r\n")
                    self.wfile.write("Content-Type: image/jpeg\r\n")
                    self.wfile.write("Content-length: "+str(len(JpegData))+"\r\n\r\n" )
                    self.wfile.write(JpegData)
                    self.wfile.write("\r\n\r\n\r\n")
                    #time.sleep(0.05)
                return
            return
        except IOError:
            self.send_error(404,'File Not Found: %s' % self.path)
        except :
            pass

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
#class ThreadedHTTPServer(HTTPServer):
    """Handle requests in a separate thread."""

def main():
    try:
        server = ThreadedHTTPServer(('0.0.0.0', 8080), MyHandler)
        print 'started httpserver...'
        server.serve_forever()
    except KeyboardInterrupt:
        print '^C received, shutting down server'
        server.socket.close()

if __name__ == '__main__':
    main()
