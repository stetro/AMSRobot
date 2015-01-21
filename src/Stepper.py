from time import sleep
import RPi.GPIO as GPIO

##
## This class is controlling the single GPIO pins based 
## on the step positon of a single stepper moter.
##
class Stepper:

  def __init__(self,A,B,C,D,time=0.1):

    # use gpio board pin numbers
    GPIO.setmode(GPIO.BOARD)
    self.D=D
    self.C=C
    self.B=B
    self.A=A

    # wait time
    self.time = time

    # Define GPIO pins as output
    GPIO.setup(self.A,GPIO.OUT)
    GPIO.setup(self.B,GPIO.OUT)
    GPIO.setup(self.C,GPIO.OUT)
    GPIO.setup(self.D,GPIO.OUT)
    GPIO.output(self.A, False)
    GPIO.output(self.B, False)
    GPIO.output(self.C, False)
    GPIO.output(self.D, False)

  # Steps from 1 to 8
  # The Step function can be used in full- or halfstep mode:
  # Fullstepp: 0, 2, 4, 6
  # Halfstepp: 0, 1, 2, 3, 4, 5, 6, 7
  def Step(self,nr):
        if nr==0:
          GPIO.output(self.A, False)
          GPIO.output(self.B, False)
          GPIO.output(self.C, False)
          GPIO.output(self.D, True)
        elif nr==1:
          GPIO.output(self.A, False)
          GPIO.output(self.B, False)
          GPIO.output(self.C, True)
          GPIO.output(self.D, True)
        elif nr==2:
          GPIO.output(self.A, False)
          GPIO.output(self.B, False)
          GPIO.output(self.C, True)
          GPIO.output(self.D, False)
        elif nr==3:
          GPIO.output(self.A, False)
          GPIO.output(self.B, True)
          GPIO.output(self.C, True)
          GPIO.output(self.D, False)
        elif nr==4:
          GPIO.output(self.A, False)
          GPIO.output(self.B, True)
          GPIO.output(self.C, False)
          GPIO.output(self.D, False)
        elif nr==5:
          GPIO.output(self.A, True)
          GPIO.output(self.B, True)
          GPIO.output(self.C, False)
          GPIO.output(self.D, False)
        elif nr==6:
          GPIO.output(self.A, True)
          GPIO.output(self.B, False)
          GPIO.output(self.C, False)
          GPIO.output(self.D, False)
        elif nr==7:
          GPIO.output(self.A, True)
          GPIO.output(self.B, False)
          GPIO.output(self.C, False)
          GPIO.output(self.D, True)

  def __del__(self):
    GPIO.cleanup()
