example_sets={"apple","banana","guava"}
print(example_sets)

for item in example_sets:
    print(item)

example_sets.add("orange")
example_sets.update(["mango","grapes"])

print(example_sets)

print(len(example_sets))

example_sets.remove("banana")
example_sets.discard("cherry")
print(example_sets)

example_sets=set(("apple","banana","cherry"))
print(example_sets)