### Logical Operators ###

# and
# Returns True if both conditions are true
x = 6
print(x > 4 and x < 10)  # Output: True (6 is greater than 4 and less than 10)

# or
# Returns True if at least one of the conditions is true
x = 5
print(x > 5 or x < 6)  # Output: True (5 is not greater than 5, but it is less than 6)

# not
# Reverses the result of the condition, returning True if the condition is False
x = 5
print(not(x > 3 and x < 10))  # Output: False (5 is between 3 and 10, so the "not" makes it False)
