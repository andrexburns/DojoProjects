class car(object):
  def __init__(self, price, speed,fuel, mileage, tax):
    self.price = price
    self.speed = speed
    self.mileage = mileage
    self.fuel = fuel
    self.tax = tax

  def display_all(self):
    print self.price, self.speed, self.mileage, self.fuel, self.tax


car1 = car(10000,"120mph","kinda full","15mpg",0.15)

car1.display_all()
car2 = car(10000, "130mph","empty" ,"10mph",0.15)

car2.display_all()
car3 = car(10000, "140mph","full" ,"15mph",0.15)

car3.display_all()
car4 = car(10000, "150mph","full","17mph",0.15)

car4.display_all()
car5 = car(10000, "160mph", "empty","15mph",0.15)

car5.display_all()
car6 = car(100000, "170mph","full","10mph",0.15)

car6.display_all()
