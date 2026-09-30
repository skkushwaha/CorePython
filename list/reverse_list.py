# displaying list elements in reverse order
days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',]
print('\nIn reverse order of days:')
i=len(days)-1
while i>=0:
    print(days[i], ",", end='')
    i-=1

# print reverse order second method
print('\nIn reverse order of days:')
i=-1
while i>=-(len(days)):
    print(days[i], ",", end='')
    i-=1