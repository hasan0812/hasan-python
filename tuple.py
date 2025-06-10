fruits = ("apple", "banana", "cherry", "pineapple")

print("fruits tuple:", fruits)


print("first fruit:", fruits[0])
print("second fruit:", fruits[1])


print("Last fruit:", fruits[-1])


print("first two fruits:", fruits[0:2])


for i in fruits:
    print(i)


print("apple count:", fruits.count("apple"))

print("Index of banana:", fruits.index("apple"))

numbers = {1, 2, 3, 4, 5, 1, 2}
print("Number set:", numbers)
numbers.add(6)
print("after adding 6:", numbers)
numbers.remove(3)
print("after removing 3:", numbers)


set1 = {1, 2, 3}
set2 = {3, 4, 5}


# Union(combine all remove duplicates)

print("Union:", set1.union(set2)) # 12345

# Intersection(common)

print("Intersection:", set1.intersection(set2)) # 3

# Difference

print("Difference (set1 - set2):", set1.difference(set2)) # 1 2