from time import sleep
import RPi.GPIO as GPIO

class Stepper:

  def __init__(self,A,B,C,D,time=0.1):
    #use gpio names
    GPIO.setmode(GPIO.BCM)
    self.D=D
    self.C=C
    self.B=B
    self.A=A
		
    # Verwendete Pins am Rapberry Pi
    #D = 26
    #C = 20
    #B = 19
    #A = 21
    #wait time
    self.time = time

    # Pins aus Ausgaenge definieren
    GPIO.setup(self.A,GPIO.OUT)
    GPIO.setup(self.B,GPIO.OUT)
    GPIO.setup(self.C,GPIO.OUT)
    GPIO.setup(self.D,GPIO.OUT)
    GPIO.output(self.A, False)
    GPIO.output(self.B, False)
    GPIO.output(self.C, False)
    GPIO.output(self.D, False)

  # Schritte 1 - 8 festlegen
  def Step(self,nr,on=True):
      if on==True:
        if nr==0:
          GPIO.output(self.D, True)
        elif nr==1:
          GPIO.output(self.D, True)
          GPIO.output(self.C, True)
        elif nr==2:
          GPIO.output(self.C, True)
        elif nr==3:
          GPIO.output(self.B, True)
          GPIO.output(self.C, True)
        elif nr==4:
          GPIO.output(self.B, True)
        elif nr==5:
          GPIO.output(self.A, True)
          GPIO.output(self.B, True)
        elif nr==6:
          GPIO.output(self.A, True)
        elif nr==7:
          GPIO.output(self.D, True)
          GPIO.output(self.A, True)
      else:
        if nr==0:
          GPIO.output(self.D, False)
        elif nr==1:
          GPIO.output(self.D, False)
          GPIO.output(self.C, False)
        elif nr==2:
          GPIO.output(self.C, False)
        elif nr==3:
          GPIO.output(self.B, False)
          GPIO.output(self.C, False)
        elif nr==4:
          GPIO.output(self.B, False)
        elif nr==5:
          GPIO.output(self.A, False)
          GPIO.output(self.B, False)
        elif nr==6:
          GPIO.output(self.A, False)
        elif nr==7:
          GPIO.output(self.D, False)
          GPIO.output(self.A, False)

  # Volle Umdrehung
  def round(self):
    for i in range(0,7):
      if i>0:
        Step(i-1,False)
        sleep(time)
      Step(i,True)
      #print i

  def __del__(self):
    GPIO.cleanup()
