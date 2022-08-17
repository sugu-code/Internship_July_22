# Enter your code here. Read input from STDIN. Print output to STDOUT
import re
pattern=r"^[456]+(\d{3}-\d{4}-\d{4}-\d{4})|^[456]+\d{15}"
pattern1=r'(\d)\1\1\1\1'
for i in range(int(input())):
    m=input()
    if re.search(pattern,m):
        if not re.search(pattern1,m):
            print("Valid")
        else:
            print("Invalid")
    else:
        print("Invalid")
            