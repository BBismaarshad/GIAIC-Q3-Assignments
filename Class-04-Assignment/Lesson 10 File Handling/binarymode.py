# Opens a file in binary mode (used for non-text files like images)
with open("image.jpg", 'rb') as file:
    binary_data = file.read()