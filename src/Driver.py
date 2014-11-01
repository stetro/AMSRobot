from Stepper import Stepper
from time import sleep

class Driver():
  def __init__(self, time=0.01):
    self.time=0.01
    #current robot setup
    self.left = Stepper(14, 15, 18, 23, time)
    self.right = Stepper(22, 27, 17, 4, time)
    #setup for lcd
    #self.left = Stepper(19,20,21,26,time=time)
    #self.right = Stepper(5,6,12,13,time=time)

  def forwards(self):
    for i in range(0,8):
      #print("left step: {}, right step: {}".format(i,i))
      self.left.Step(i,True)
      self.right.Step(i,True)
      sleep(self.time)
      self.left.Step(i,False)
      self.right.Step(i,False)
      sleep(self.time)

  def backwards(self):
    for i in range(7,-1,-1):
      #print("left step: {}, right step: {}".format(i,i))
      self.left.Step(i,True)
      self.right.Step(i,True)
      sleep(self.time)
      self.left.Step(i,False)
      self.right.Step(i,False)
      sleep(self.time)

  def rotateRight(self):
    i2=range(7,-1,-1)
    for i in range(0,8):
      #print("left step: {}, right step: {}".format(i,i2[i]))
      self.left.Step(i,True)
      self.right.Step(i2[i],True)
      sleep(self.time)
      self.left.Step(i,False)
      self.right.Step(i2[i],False)
      sleep(self.time)

  def rotateLeft(self):
    i2=range(7,-1,-1)
    for i in range(0,8):
      #print("left step: {}, right step: {}".format(i2[i],i))
      self.left.Step(i2[i],True)
      self.right.Step(i,True)
      sleep(self.time)
      self.left.Step(i2[i],False)
      self.right.Step(i,False)
      sleep(self.time)

if __name__ =="__main__":
  d=Driver();
  for i in range(0,100):
    #d.forwards()
		d.backwards()
		#d.rotateLeft()
