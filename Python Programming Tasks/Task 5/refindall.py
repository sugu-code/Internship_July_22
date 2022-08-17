# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
v="aeiou"
c="bcdfghjklmnpqrstvwxy"
matches=re.findall(r"(?<=[%s])([%s]{2,})[%s]"%(c,v,c),input(),flags=re.IGNORECASE)
print(matches)
    print(-1)
else:
    for i in matches:
        print(i)