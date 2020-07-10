a="Hello, World"
print(a)
print(a[1]) # It takes string as array
print(a[2:5])   # It takes string as array with lenths
print(len(a))   # Lenth of string
print(a.replace("H","J"))   # Replace character
print(a.split(","))  # Split a

txt = "The rain in Spain stays mainly in the plain"
x = "ain" in txt
y = "ain" not in txt
print(x) # True
print(y) # False

b= "Hello"
c="World"
d= b+c
print(c)
print(c.lower())
print(c.upper())

age = 36
txt = "My name is John, and I am {}"
print(txt.format(age))
# Output: My name is John, and I am 36

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))
# Output: I want 3 pieces of item 567 for 49.95 dollars.

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))
# Output: I want to pay 49.95 dollars for 3 pieces of item 567.

age = 36
txt = "My name is John, I am " + age
print(txt)

a="Hello"
print(a.upper) # upper case
print(a.lower)  # Lower case
#print( lower(a)) 
#print( upper(a)) 
a=""" This is string assignment 
multiple line."""
print(a)