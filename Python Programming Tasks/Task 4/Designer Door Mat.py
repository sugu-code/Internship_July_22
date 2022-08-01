# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m=input().split(' ')
for i in range(1,int(n),2): 
    print((i * ".|.").center(int(m), "-"))
print("WELCOME".center(int(m),"-"))
for i in range(int(n)-2,-1,-2): 
    print((i * ".|.").center(int(m), "-"))