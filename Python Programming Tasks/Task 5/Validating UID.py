# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern1=r'[A-Z]{2}'
pattern2=r'\d\d\d'
n=int(input())
for i in range(n):
    m=''.join(sorted(input()))
    if m.isalnum() and len(set(m))==10:
        if re.search(pattern1,m) and re.search(pattern2,m):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
            