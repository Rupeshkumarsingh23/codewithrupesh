import math
class circle:
    def __init__(self,radius):
        self.radius=radius
    def cal__area(self):
        area=math.pi*math.pow(self.radius,2)
        print("area of a circle",area)
    def cal__circumference(self):
        circumference=2*math.pi*self.radius
        print("circumference of a circle",circumference)
radius=int(input("Enter a radius of a circle:"))
obj=circle(radius)
obj.cal__area()
obj.cal__circumference()
