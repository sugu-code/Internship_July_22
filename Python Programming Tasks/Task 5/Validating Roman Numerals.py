d='(IX|IV|V?I{0,3})'
t='(XC|XL|L?X{0,3})'
h='(CM|CD|D?C{0,3})'
th='M{0,3}'
regex_pattern = r"%s%s%s%s$" %(th,h,t,d)	# Do not delete 'r'.

import re
print(str(bool(re.match(regex_pattern, input()))))