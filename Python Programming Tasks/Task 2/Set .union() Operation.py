# Enter your code here. Read input from STDIN. Print output to STDOUT
n=input()
a=set(map(int,input().split()))
m=input()
b=set(map(int,input().split()))
c=a.union(b)
print(len(c))