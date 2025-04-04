# Creates a new file, but raises an error if it already exists
try:
    with open("new_file.txt", 'x') as file:
        file.write("This is a new file.")
except FileExistsError:
    print("File already exists!")