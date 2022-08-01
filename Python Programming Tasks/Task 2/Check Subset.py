# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
for i in range(n):
    m=int(input())
    a=set(map(int,input().split()))
    p=int(input())
    b=set(map(int,input().split()))
    if a.intersection(b)==a:
        c=True
    else:
        c=False
    print(c)