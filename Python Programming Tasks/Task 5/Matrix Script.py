import math
import os
import random
import re
import sys

n,m= input().rstrip().split()
matrix = []

for i in range(int(n)):
    m_item = input()
    matrix.append(m_item)
encoded_s = "".join([matrix[j][i] for i in range(int(m)) for j in range(int(n))])
pat = r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])'
print(re.sub(pat,' ',encoded_s))