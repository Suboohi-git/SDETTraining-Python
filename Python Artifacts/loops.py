a = 0

while a < 5:
  print(a)
  if a==3:
      break
  a += 1
print("*****************")
a=0
while a<5:
    a+=1
    if a==3:
        continue
    print(a)
print("**********************")
a = 1
while a < 5:
  print(a)
  a += 1
else:
  print("a is no longer less than 5")
print("**************************")

fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  print(fruit) 
print("**************************")

for x in "banana":
  print(x)

print("***************")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  if fruit == "banana":
    break
  print(fruit) 

print("***************")
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
  if fruit == "banana":
    continue
  print(fruit) 

print("***************")
for x in range(6):
  print(x) 
print("***************")
for x in range(2,6):
  print(x) 
print("***************")
for x in range(6):
  print(x)
else:
  print("Finally finished!") 
print("***************")
adjectives = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for adjective in adjectives:
  for fruit in fruits:
    print(adjective, fruit) 