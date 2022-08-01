# Enter your code here. Read input from STDIN. Print output to STDOUT
m=int(input())
a=set(map(int,input().split()))
n=int(input())
b=set(map(int,input().split()))
output=list(a^b)
output.sort()
for i in range(len(output)):
    print(output[i])