with open('example.txt', 'r+') as file:
    print(file.tell())  # Current position (0 at start)
    content = file.read(5)
    print(content)
    print(file.tell())  # Position after reading 5 chars
    file.seek(0)  # Go back to start
    print(file.read())  # Read entire file