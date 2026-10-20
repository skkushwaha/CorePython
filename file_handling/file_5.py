import os

# Specify the directory path
path = r'D:\pynative\reports'
file_name = 'revenue.txt'

# Creating a file at specified folder
# join directory and file path
with open(os.path.join(path, file_name), 'w') as fp:
    # uncomment below line if you want to create an empty file
    fp.write('This is a new line')