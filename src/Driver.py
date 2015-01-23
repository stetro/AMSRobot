from Stepper import Stepper
from time import sleep

##
## This class is controlling both stepper motors and
## is giving a unified interface for single move actions
## for the robot
##
class Driver():
  def __init__(self, time=0.01):
    self.time=0.01
    # used pin selection, given in the project circuite
    self.left = Stepper(7, 11, 13, 15, time)
    self.right = Stepper(16, 12,10, 8, time)

  def forwards(self):
    for i in range(0,4):
      self.left.Step(i * 2 + 1)
      self.right.Step(i * 2 + 1)
      sleep(self.time)

  def backwards(self):
    for i in range(3,-1,-1):
      self.left.Step(i * 2 + 1)
      self.right.Step(i * 2 + 1)
      sleep(self.time)

  def rotateRight(self):
    i2=range(3,-1,-1)
    for i in range(0,4):
      self.right.Step(i * 2 + 1)
      self.left.Step(i2[i] * 2 + 1)
      sleep(self.time)

  def rotateLeft(self):
    i2=range(3,-1,-1)
    for i in range(0,4):
      self.right.Step(i2[i] * 2 + 1)
      self.left.Step(i * 2 + 1)
      sleep(self.time)
