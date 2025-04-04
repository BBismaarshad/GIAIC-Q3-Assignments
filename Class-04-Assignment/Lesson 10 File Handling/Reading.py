# Read entire file
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Read line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())  # strip() removes extra newlines

# Read specific number of characters
with open('example.txt', 'r') as file:
    print(file.read(10))  # Reads first 10 characters