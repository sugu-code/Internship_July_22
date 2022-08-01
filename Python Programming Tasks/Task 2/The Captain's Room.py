N = int(input())

a = map(int, input().split())
a = sorted(a)

for i in range(len(a)):
    if(i != len(a)-1):
        if(a[i]!=a[i-1] and a[i]!=a[i+1]):
            print(a[i])
            break;
    else:
        print(a[i])
    