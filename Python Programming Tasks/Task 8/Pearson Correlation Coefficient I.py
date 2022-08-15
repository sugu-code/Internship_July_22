# Enter your code here. Read input from STDIN. Print output to STDOUT
length = int(input())
x = list(map(float,input().strip().split()))
y = list(map(float,input().strip().split()))
s=0
mx = sum(x) / length
for i in x:
    s += (i-mx)**2
sdx=(s/length)**0.5

my = sum(y) / length
s=0
for i in y:
    s += (i-my)**2
sdy=(s/length)**0.5
cov=0
for i in range(length):
    cov +=(x[i]-mx)*(y[i]-my)

cor = cov / (length * sdx * sdy)

print(round(cor,3))