try:
    file = open("example.txt", "r")
except FileNotFoundError:
    print("File not found!")
else:
    # Executes only if no exception occurred
    content = file.read()
    print(content)
    file.close()