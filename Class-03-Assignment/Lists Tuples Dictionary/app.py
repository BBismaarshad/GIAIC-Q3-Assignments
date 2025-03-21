# Ordered

my_list = [10, 20, 30, 40]
print(my_list)  # Output: [10, 20, 30, 40]

# Indexed
my_list = [10, 20, 30, 40]
print(my_list[2])  # Output: 30 (3rd element, 0-based indexing)

# Mutable
my_list = [10, 20, 30, 40]
my_list[1] = 25  # 2nd element ko modify karna
print(my_list)  # Output: [10, 25, 30, 40]

# Dynamic Size
my_list = [10, 20, 30]
my_list.append(40)  # List mein ek element add karna
print(my_list)  # Output: [10, 20, 30, 40]

my_list.remove(20)  # List se ek element remove karna
print(my_list)  # Output: [10, 30, 40]

# Heterogeneous
my_list = [10, "Hello", 3.14, True]
print(my_list)  # Output: [10, "Hello", 3.14, True]


#Common List Methods


#append()
my_list = [1, 2, 3]
my_list.append(4)
print(my_list)  # Output: [1, 2, 3, 4]


#extend()
my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)  # Output: [1, 2, 3, 4, 5]


#insert()
my_list = [1, 2, 3]
my_list.insert(1, 1.5)
print(my_list)  # Output: [1, 1.5, 2, 3]


#remove()
my_list = [1, 2, 3, 2]
my_list.remove(2)
print(my_list)  # Output: [1, 3, 2]


#pop()
my_list = [1, 2, 3]
popped_element = my_list.pop(1)
print(my_list)  # Output: [1, 3]
print(popped_element)  # Output: 2



#clear()
my_list = [1, 2, 3]
my_list.clear()
print(my_list)  # Output: []


# index()
my_list = [1, 2, 3, 2]
index = my_list.index(2)
print(index)  # Output: 1


#count()
my_list = [1, 2, 3, 2]
count = my_list.count(2)
print(count)  # Output: 2



#sort()
my_list = [3, 1, 4, 1, 5, 9]
my_list.sort()
print(my_list)  # Output: [1, 1, 3, 4, 5, 9]



#reverse()
my_list = [1, 2, 3]
my_list.reverse()
print(my_list)  # Output: [3, 2, 1]


#copy()
my_list = [1, 2, 3]
new_list = my_list.copy()
print(new_list)  # Output: [1, 2, 3]


#len()
my_list = [1, 2, 3]
length = len(my_list)
print(length)  # Output: 3


#Dictionary

# Creating a dictionary
fruits = {
    "apple": "red",
    "banana": "yellow",
    "grape": "purple",
    "orange": "orange"
}

# Accessing values using keys
print("Color of apple:", fruits["apple"])
print("Color of banana:", fruits["banana"])

# Adding a new fruit and its color
fruits["watermelon"] = "green"
print("Updated dictionary:", fruits)

# Changing the color of a fruit
fruits["grape"] = "green"  # Correcting the key to "grape"
print("Updated color of grape:", fruits["grape"])

# Removing a fruit
del fruits["banana"]
print("Dictionary after removing banana:", fruits)

# Checking if a fruit exists
if "orange" in fruits:
    print("Orange is in the dictionary!")