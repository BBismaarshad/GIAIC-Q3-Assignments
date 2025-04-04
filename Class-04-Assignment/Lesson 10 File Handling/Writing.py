# Write to a file (overwrites existing content)
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new line.")

# Append to a file
with open('example.txt', 'a') as file:
    file.write("\nThis is appended text.")