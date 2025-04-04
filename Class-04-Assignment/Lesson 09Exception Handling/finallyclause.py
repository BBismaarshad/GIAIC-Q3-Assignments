try:
    file = open("data.txt", "w")
    file.write("Hello World")
except IOError:
    print("Error writing to file")
finally:
    # Always executes, whether an exception occurred or not
    if 'file' in locals():
        file.close()
    print("File operation completed")