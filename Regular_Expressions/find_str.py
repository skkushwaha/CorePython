import re
prog = re.compile(r'm\w\w')
str = 'cat mat bat rat'
result = prog.search(str)
print(result.group())

