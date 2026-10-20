import os

# list files a directory
print(os.listdir(r'D:\pynative\reports'))
# output ['sample.txt', 'sales.txt', 'sales_2.txt' 'profit.txt']

# verify file exist
print(os.path.isfile(r'D:\pynative\reports\profit.txt'))
# output True