# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
pattern=r'#[a-fA-F0-9]{3,6}'
for i in range(n):
    s=input()
    x=s.split()
    if len(x)>1  and  '{' not in x:
        x=re.findall(pattern,s)
        for i in x:
            print(i)