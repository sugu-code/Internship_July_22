# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
a=set(map(int,input().split()))
N=int(input())
for i in range(N):
    x=input().split()
    if x[0]=="intersection_update":
        b=set(map(int,input().split())) 
        a=a.intersection(b)
    if x[0]=="update":
        d=set(map(int,input().split())) 
        a=a.union(d)
    if x[0]=="symmetric_difference_update":
        e=set(map(int,input().split())) 
        a=a.symmetric_difference(e)
    if x[0]=="difference_update":
        f=set(map(int,input().split())) 
        a=a.difference(f)
count=0
for i in a:
    count+=i
print(count)
    