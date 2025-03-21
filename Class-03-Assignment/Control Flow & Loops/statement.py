#In python, there are four forms of the if ...else statement.


#1.if Statement

# Ask the user to enter their age and convert the input to an integer
age = int(input("Enter your age: "))

# Check if the age is greater than or equal to 18
if age >= 18:
    # If the condition is True, print this message
    print("You are eligible to vote.")




# 2. If ... else statement
# Take number input from the user
number = int(input("Enter Number: "))

# Check if the number is positive or negative
if number > 0:
    print("Number is positive")  # If the number is greater than 0
else:
    print("Number is negative")  # If the number is less than 0






# 3. if ...elif ... else statement

# Step 1: Define the marks
marks = 85

# Step 2: Check if marks are greater than or equal to 90
if marks >= 90:
    print("Grade: A")  # If marks are 90 or above, print "Grade: A"

# Step 3: If the first condition is false, check if marks are 80 or above
elif marks >= 80:
    print("Grade: B")  # If marks are 80 or above, print "Grade: B"

# Step 4: If both conditions are false, execute the else block
else:
    print("Grade: C")  # If marks are less than 80, print "Grade: C"





# 4. Nested if Statement

# Student ke marks input
marks = float(input("Enter your marks: "))

# Outer if statement
if marks >= 0 and marks <= 100:  # Check if marks are valid
    # Nested if statement
    if marks >= 90:
        print("Grade: A+")
    elif marks >= 80:
        print("Grade: A")
    elif marks >= 70:
        print("Grade: B")
    elif marks >= 60:
        print("Grade: C")
    elif marks >= 50:
        print("Grade: D")
    else:
        print("Grade: F (Fail)")
else:
    print("Invalid marks! Marks should be between 0 and 100.")