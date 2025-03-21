# for loop 
# example 
# Using a for loop to print numbers from 1 to 10
for i in range(1, 11):  # range(1, 11) generates numbers from 1 to 10 (11 is not included)
    print(i)  # Print the current value of 'i' in each iteration



# while Loop
# Initialize a variable
i = 10

# Use a while loop to print numbers from 10 to 100
while i <= 100:  # Loop runs as long as 'i' is less than or equal to 100
    print(i)    # Print the current value of 'i'
    i += 10      # Increment 'i' by 10 in each iteration Controlling Loops



# Controlling Loops

# Break example
list1 = range(10)  # Create a range from 0 to 9
for X in list1:    # Loop through each value in the range
    if X == 4:     # Check if the current value of X is 4
        break      # If X is 4, exit the loop completely
    print(X)       # Print the current value of X

# Continue example
list1 = range(10)  # Create a range from 0 to 9
for X in list1:    # Loop through each value in the range
    if X == 4:     # Check if the current value of X is 4
        continue   # If X is 4, skip this iteration and move to the next one
    print(X)       # Print the current value of X


#Nested Loops
# Outer loop for rows
for i in range(1, 6):  # 1 se 5 tak rows ke liye
    # Inner loop for columns
    for j in range(1, i + 1):  # Har row mein columns ki number uski row number ke equal hoga
        print("*", end=" ")  # '*' print karo aur space add karo
    print()  # New line ke liye