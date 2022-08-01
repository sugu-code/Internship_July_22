# Enter your code here. Read input from STDIN. Print output to STDOUT
def subset(s,b):
    c= b.issubset(s) and not(s.issubset(b))
    return c

if __name__=='__main__':
    s=set(map(int,input().split()))
    n=int(input())
    c=True
    for i in range(n):
        b=set(map(int,input().split()))
        c&=subset(s,b)
    print(c)
