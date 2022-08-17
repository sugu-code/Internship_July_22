import re
n = input()
m = input()
pattern = re.compile(m)
x = pattern.search(n)
if not x: 
    print("(-1, -1)")
while x:
    print("({0}, {1})".format(x.start(), x.end() - 1))
    x = pattern.search(n,x.start() + 1)