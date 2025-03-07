

### Bitwise Operators ###

# & 
# Performs a bitwise AND operation. It returns 1 if both bits are 1, otherwise 0.
print(6 & 3)  # Output: 2 (6 in binary: 110, 3 in binary: 011, AND result: 010 which is 2)

# | 
# Performs a bitwise OR operation. It returns 1 if at least one bit is 1.
print(8 | 3)  # Output: 11 (8 in binary: 1000, 3 in binary: 0011, OR result: 1011 which is 11)

# ^ 
# Performs a bitwise XOR (exclusive OR) operation. It returns 1 if the bits are different, otherwise 0.
print(4 ^ 3)  # Output: 7 (4 in binary: 0100, 3 in binary: 0011, XOR result: 0111 which is 7)

# ~ 
# Performs a bitwise NOT operation. It inverts all the bits (flips 0s to 1s and 1s to 0s).
print(~3)  # Output: -4 (~3 flips the bits of 3, resulting in -4 in two's complement representation)

# << 
# Performs a bitwise left shift. Shifts the bits of the number to the left by the specified number of positions.
print(3 << 2)  # Output: 12 (3 in binary: 0011, shifted left by 2: 1100 which is 12)

# >> 
# Performs a bitwise right shift. Shifts the bits of the number to the right by the specified number of positions.
print(8 >> 2)  # Output: 2 (8 in binary: 1000, shifted right by 2: 0010 which is 2)

##example
print(8 >> 2)
