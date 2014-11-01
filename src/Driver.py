from Stepper import Stepper
from time import sleep

class Driver():
  def __init__(self,time=0.01):
    self.time=0.005
    self.left = Stepper(19,20,21,26,time=time)
    self.right = Stepper(5,6,12,13,time=time)

  def forward(self):
    for i in range(0,7):
      self.left.Step(i,True)
      self.right.Step(i,True)
      sleep(self.time)
      self.left.Step(i,False)
      self.right.Step(i,False)
      sleep(self.time)
      #print i

  def backwards(self):
    for i in range(7,0,-1):
      self.left.Step(i,True)
      self.right.Step(i,True)
      sleep(self.time)
      self.left.Step(i,False)
      self.right.Step(i,False)
      sleep(self.time)

  def rotateRight(self):
    i2=range(7,0,-1)
    for i in range(0,7):
      self.left.Step(i,True)
      self.left.Step(i2[i],True)
      sleep(self.time)
      self.left.Step(i,False)
      self.right.Step(i2[i],False)
      sleep(self.time)

  def rotateRight(self):
    i2=range(7,0,-1)
    for i in range(0,7):
      self.left.Step(i2[i],True)
      self.left.Step(i,True)
      sleep(self.time)
      self.left.Step(i2[i],False)
      self.right.Step(i,False)
      sleep(self.time)

if __name__ =="__main__":
  d=Driver();
  for i in range(0,100):
    d.forward()
