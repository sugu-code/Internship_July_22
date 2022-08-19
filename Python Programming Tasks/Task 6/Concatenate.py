import numpy
n,m,p=map(int,input().split())
arr1= numpy.array([input().strip().split() for i in range(n)],int)
arr2=numpy.array([input().strip().split() for i in range(m)],int)
print(numpy.concatenate((arr1,arr2),))