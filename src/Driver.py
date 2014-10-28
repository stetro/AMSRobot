from Stepper import Stepper

class Driver():
  def __init__():
    self.left = Stepper(21,19,20,26)
    self.right = Stepper(21,19,20,26)

  def forward():
    for i in range(0,7):
      self.left.Step(i,True)
      self.right.Step(i,True)
      sleep(time)
      self.left.Step(i,False)
      self.right.Step(i,False)
      sleep(time)
      #print i

  def backwards():
    for i in range(7,0,-1):
      self.left.Step(i,True)
      self.right.Step(i,True)
      sleep(time)
      self.left.Step(i,False)
      self.right.Step(i,False)
      sleep(time)

  def rotateRight():
    i2=range(7,0,-1)
    for i in range(0,7):
      self.left.Step(i,True)
      self.left.Step(i2[i],True)
      sleep(time)
      self.left.Step(i,False)
      self.right.Step(i2[i],False)
      sleep(time)

  def rotateRight():
    i2=range(7,0,-1)
    for i in range(0,7):
      self.left.Step(i2[i],True)
      self.left.Step(i,True)
      sleep(time)
      self.left.Step(i2[i],False)
      self.right.Step(i,False)
      sleep(time)
