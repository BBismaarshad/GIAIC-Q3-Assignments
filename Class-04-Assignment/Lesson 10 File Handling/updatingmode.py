# Opens a file for both reading and writing
with open("example.txt", 'r+') as file:
    content = file.read()
    file.write("\nNew data added.")