import os

print(os.getcwd())          # Current working directory
os.listdir('.')             # List files in current directory
os.mkdir('new_dir')         # Create new directory
os.rename('old', 'new')     # Rename file/directory
os.path.exists('file.txt')  # Check if path exists
os.path.getsize('file.txt') # Get file size in bytes
os.path.join('dir', 'file') # Platform-independent path joining