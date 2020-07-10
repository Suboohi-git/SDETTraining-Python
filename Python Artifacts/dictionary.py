example_dict={
    "brand":"ford",
    "model":"Skoda",
    "year":2017
}
print(example_dict)

x= example_dict["model"]
print(x)

x= example_dict.get("model")
print(x)

example_dict["year"]=2019
print(example_dict)

for x in example_dict:
    print(x)
    print(example_dict[x])

for x in example_dict.values():
    print(x)

for x,y in example_dict.items():
    print(x,y)

print(len(example_dict))

example_dict["color"]="red"
print(example_dict)

example_dict.pop("model")
print(example_dict)

example_dict.popitem()
print(example_dict)

my_pets = {
  "timmy": {
    "type": "dog",
    "color": "blonde"
  },
  "chippy": {
    "type": "cat",
    "color": "brown"
  }
}

example_dict = dict(brand="Ford", model="Mustang", year=1964)
print(example_dict)