import numpy
a=numpy.array(input().split(),float)
numpy.set_printoptions(legacy='1.13')
print(numpy.floor(a))
print(numpy.ceil(a))
print(numpy.rint(a))