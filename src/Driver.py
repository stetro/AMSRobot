from Stepper import Stepper
from time import sleep

class Driver():
  def __init__(self, time=0.01):
    self.time=0.01
    #current robot setup
    self.left = Stepper(7, 11, 13, 15, time)
    self.right = Stepper(16, 12,10, 8, time)
    #setup for lcd
    #self.left = Stepper(19,20,21,26,time=time)
    #self.right = Stepper(5,6,12,13,time=time)

  def forwards(self):
    for i in range(0,4):
      #print("left step: {}, right step: {}".format(i,i))
      self.left.Step(i * 2 + 1)
      self.right.Step(i * 2 + 1)
      sleep(self.time)

  def backwards(self):
    for i in range(3,-1,-1):
      #print("left step: {}, right step: {}".format(i,i))
      self.left.Step(i * 2 + 1)
      self.right.Step(i * 2 + 1)
      sleep(self.time)

  def rotateRight(self):
    i2=range(3,-1,-1)
    for i in range(0,4):
      #print("left step: {}, right step: {}".format(i,i2[i]))
      self.right.Step(i * 2 + 1)
      self.left.Step(i2[i] * 2 + 1)
      sleep(self.time)

  def rotateLeft(self):
    i2=range(3,-1,-1)
    for i in range(0,4):
      #print("left step: {}, right step: {}".format(i2[i],i))
      self.right.Step(i2[i] * 2 + 1)
      self.left.Step(i * 2 + 1)
      sleep(self.time)

if __name__ =="__main__":
  d=Driver();
  for i in range(0,100):
    d.forwards()
		#d.backwards()
		#d.rotateLeft()
