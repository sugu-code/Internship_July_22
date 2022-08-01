# Enter your code here. Read input from STDIN. Print output to STDOUT
import cmath
m=input()
print(*cmath.polar(complex(m)), sep="\n")