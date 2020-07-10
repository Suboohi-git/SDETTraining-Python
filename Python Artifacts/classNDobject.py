class MyClass:
  'This is an example class'
  x = 5
  
p1 = MyClass()
print(p1.x) 

class Person:
  'This class represents a person'
  
  def __init__(self, name, age):
    self.name = name
    self.age = age

  def myFunc(self):
    print("Hello, my name is " + self.name)

p1 = Person("John", 36)

print(p1.name) 
print(p1.age)  
p1.myFunc