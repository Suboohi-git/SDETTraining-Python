def myFunction():
    print("Hello")

myFunction()

def my_function(name):
  print("Hello " + name)
  
my_function("Suboohi") 

def my_function1(fname, lname):
  print(fname + " " + lname)

my_function1("SS", "AH") 

def my_function2(*pets):
  print("The youngest pet is " + pets[1])

my_function2("Timmy", "Chippy") 

def my_function3(country = "India"):
  print("I am from " + country)

my_function3("Sweden")
my_function3("Japan")
my_function3()

def my_function4(x):
  return 5 * x

print(my_function4(3))
print(my_function4(5))
print(my_function4(9)) 