import numpy
p=numpy.array(input().split(),float)
x=int(input())
print(numpy.polyval(p,x))