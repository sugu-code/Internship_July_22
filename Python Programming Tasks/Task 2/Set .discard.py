if __name__=='__main__':    
    n = int(input())
    s = set(map(int, input().split()))
    N= int(input())
    a=[]
    for i in range(N):
        x = list(input().split())
        a.append(x)
    for x in a:
        if x[0]=="pop":
            s.pop()
        elif x[0]=="discard":
            s.discard(int(x[1]))
        elif x[0]=="remove":
            s.remove(int(x[1]))
    count=0
    for j in s:
        count+=j
    print(count)