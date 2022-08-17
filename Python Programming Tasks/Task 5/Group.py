# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n=input()
pattern=r"([a-z A-Z 0-9])\1"
result=re.search(pattern,n)
if result:
    print(result.groups()[0])
else:
    print(-1)