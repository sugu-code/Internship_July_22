# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=int(input())
pattern=r"^([-\+])?\d*\.\d+$"
for i in range(n):
    k=input()
    output=re.search(pattern,k)
    if output:
        print("True")
    else:
        print("False")