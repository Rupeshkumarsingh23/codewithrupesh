class Emp:
    raise_amount=7.5
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def increase_salary(self):
        self.salary=self.salary+(self.salary*Emp.raise_amount/100)
    def display(self):
        print(self.name,self.age,self.salary)

obj1=Emp("Rupesh",23,80000)
obj2=Emp("Rajeev",23,70000)
print("before increment salary:")
obj1.display()
obj2.display()
print("After increment by ",Emp.raise_amount,"percent:")
obj1.increase_salary()
obj2.increase_salary()
obj1.display()
obj2.display()
