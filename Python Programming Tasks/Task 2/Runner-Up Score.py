if __name__ == '__main__':
    n = int(input())
    a=[]
    b=[]
    arr = map(int, input().split())
    for i in arr:
        a.append(i)
    c= max(a)
    for j in a:
        if j!=c:
            b.append(j)
    print(max(b))