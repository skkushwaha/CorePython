try:
    fp = open('demo_notes.txt', 'r')
    print(fp.read())
    fp.close()
except FileNotFoundError:
    print('Please check the file path')
