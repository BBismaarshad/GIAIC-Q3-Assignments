# Copy an image file
with open('source.jpg', 'rb') as source:
    with open('destination.jpg', 'wb') as destination:
        destination.write(source.read())