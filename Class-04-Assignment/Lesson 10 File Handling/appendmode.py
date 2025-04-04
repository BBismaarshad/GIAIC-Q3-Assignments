# Opens a file for appending (adds to the end without deleting existing content)
with open("example.txt", 'a') as file:
    file.write("\nThis is a new line.")