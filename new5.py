class Person:
  def __init__(self,name,age):
  	self.name=name
  	self.age=age
  def fly(self):
  	print(self.name,self.age)	
  	
class Student(Person):
  def __init__(self,name,age):
    super().__init__(name,age)
x=Student("aadil",24)
x.fly()

		