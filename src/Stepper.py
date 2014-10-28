from time import sleep
import RPi.GPIO as GPIO

class Stepper:

  def __init__(self,A,B,C,D,time=0.1):
    #use gpio names
    GPIO.setmode(GPIO.BCM)
    # Verwendete Pins am Rapberry Pi
    #D = 26
    #C = 20
    #B = 19
    #A = 21
    #wait time
    self.time = time

    # Pins aus Ausgaenge definieren
    GPIO.setup(A,GPIO.OUT)
    GPIO.setup(B,GPIO.OUT)
    GPIO.setup(C,GPIO.OUT)
    GPIO.setup(D,GPIO.OUT)
    GPIO.output(A, False)
    GPIO.output(B, False)
    GPIO.output(C, False)
    GPIO.output(D, False)

  # Schritte 1 - 8 festlegen
  def Step(nr,on=True):
      if on==True:
        if nr==0:
          GPIO.output(D, True)
        elif nr==1:
          GPIO.output(D, True)
          GPIO.output(C, True)
        elif nr==2:
          GPIO.output(C, True)
        elif nr==3:
          GPIO.output(B, True)
          GPIO.output(C, True)
        elif nr==4:
          GPIO.output(B, True)
        elif nr==5:
          GPIO.output(A, True)
          GPIO.output(B, True)
        elif nr==6:
          GPIO.output(A, True)
        elif nr==7:
          GPIO.output(D, True)
          GPIO.output(A, True)
      else:
        if nr==0:
          GPIO.output(D, False)
        elif nr==1:
          GPIO.output(D, False)
          GPIO.output(C, False)
        elif nr==2:
          GPIO.output(C, False)
        elif nr==3:
          GPIO.output(B, False)
          GPIO.output(C, False)
        elif nr==4:
          GPIO.output(B, False)
        elif nr==5:
          GPIO.output(A, False)
          GPIO.output(B, False)
        elif nr==6:
          GPIO.output(A, False)
        elif nr==7:
          GPIO.output(D, False)
          GPIO.output(A, False)

  # Volle Umdrehung
  def round():
    for i range(0,7):
      if i>0:
        Step(i-1,False)
        sleep(time)
      Step(i,True)
      #print i

  def __del__():
    GPIO.cleanup()
