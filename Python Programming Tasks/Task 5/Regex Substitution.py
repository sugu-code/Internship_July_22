# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
n = int(input())
for i in range(n):
   h = input()
   h = re.sub(r"\ \&\&\ "," and ",h)
   h = re.sub(r"\ \|\|\ "," or ",h)
   h = re.sub(r"\ \&\&\ "," and ",h)
   h = re.sub(r"\ \|\|\ "," or ",h)
   print(h)