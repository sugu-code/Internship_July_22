if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    b=[]
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if i+j+k!=n:
                    a=[i,j,k]
                    b.append(a)
    print(b)