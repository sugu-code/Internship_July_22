# Enter your code here. Read input from STDIN. Print output to STDOUT
import math
ab=int(input())
bc=int(input())
ac=math.sqrt((ab**2)+(bc**2))
cm=ac/2
bca=math.asin(ab/ac)
bm=math.sqrt((bc**2+cm**2)-(2*bc*cm*math.cos(bca)))
teta=math.asin(math.sin(bca)*cm/bm)
print(int(round(math.degrees(teta),0)),'\u00B0',sep='')