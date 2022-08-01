# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__=='__main__':
    s=set([])
    n=int(input())
    for i in range(n):
        x = input()
        s.add(x)
    print(len(s))