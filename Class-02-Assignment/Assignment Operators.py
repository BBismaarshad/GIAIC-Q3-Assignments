### Assignment Operators ###

# = 
# Assigns the value on the right to the variable on the left
x = 2
print(x)  # Output: 2

# +=
# Adds the right value to the left variable and assigns the result to the left variable
x = 6
x += 3  # Equivalent to x = x + 3
print(x)  # Output: 9

# -=
# Subtracts the right value from the left variable and assigns the result to the left variable
x = 5
x -= 3  # Equivalent to x = x - 3
print(x)  # Output: 2

# *=
# Multiplies the left variable by the right value and assigns the result to the left variable
x = 5
x *= 3  # Equivalent to x = x * 3
print(x)  # Output: 15

# /=
# Divides the left variable by the right value and assigns the result to the left variable
x = 5
x /= 3  # Equivalent to x = x / 3
print(x)  # Output: 1.6667 (approx.)

# %=
# Assigns the remainder of the division of the left variable by the right value to the left variable
x = 5
x %= 3  # Equivalent to x = x % 3
print(x)  # Output: 2

# //=
# Divides the left variable by the right value and assigns the largest integer less than or equal to the result
x = 5
x //= 3  # Equivalent to x = x // 3
print(x)  # Output: 1

# **=
# Raises the left variable to the power of the right value and assigns the result to the left variable
x = 8
x **= 3  # Equivalent to x = x ** 3
print(x)  # Output: 512

# &= 
# Performs a bitwise AND operation on the left variable and the right value, then assigns the result to the left variable
x = 9
x &= 9  # Equivalent to x = x & 9
print(x)  # Output: 9

# |= 
# Performs a bitwise OR operation on the left variable and the right value, then assigns the result to the left variable
x = 10
x |= 3  # Equivalent to x = x | 3
print(x)  # Output: 11

# ^= 
# Performs a bitwise XOR operation on the left variable and the right value, then assigns the result to the left variable
x = 8
x ^= 3  # Equivalent to x = x ^ 3
print(x)  # Output: 11

# >>= 
# Performs a bitwise right shift on the left variable by the number of positions specified by the right value
x = 3
x >>= 4  # Equivalent to x = x >> 4
print(x)  # Output: 0

# <<= 
# Performs a bitwise left shift on the left variable by the number of positions specified by the right value
x = 5
x <<= 3  # Equivalent to x = x << 3
print(x)  # Output: 40
