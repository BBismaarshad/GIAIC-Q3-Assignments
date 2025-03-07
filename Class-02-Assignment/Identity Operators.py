### Identity Operators ###

# is
# Returns True if both variables point to the same object in memory (i.e., they are identical)
x = ["apple", "Cherry"]
y = ["apple", "Cherry"]
z = x
print(x is z)  # Output: True (x and z point to the same object in memory)
print(x is y)  # Output: False (x and y point to different objects, even though they have the same content)
print(x == y)  # Output: True (x and y have the same content, but are different objects)

# is not
# Returns True if both variables do not point to the same object in memory
x = ["apple", "Cherry"]
y = ["apple","Cherry"]
z = x
print(x is not z)  # Output: False (x and z point to the same object, so "is not" is False)
print(x is not y)  # Output: True (x and y are different objects in memory, so "is not" is True)

print(x != y)  # Output: False (x and y are not the same object but have the same content, so "!=" is False)
