class bike(object):
  def __init__(self, price, max_speed, miles):
    self.price = price
    self.max_speed = max_speed
    self.miles = miles

  def displayinfo(self):
    print self.price , self.max_speed, self.miles

  def ride(self):

    self.miles += 10
    return self

  def reverse(self):
    self.miles -= 5
    return self
bike1 = bike(200, "50mph", 100)
bike1.ride().ride().ride().reverse().displayinfo()

bike2 = bike(300, "70mph", 150)
bike2.ride().ride().reverse().reverse().displayinfo()

bike3 = bike(500, "180mph", 150)
bike3.reverse().reverse().reverse().displayinfo()
