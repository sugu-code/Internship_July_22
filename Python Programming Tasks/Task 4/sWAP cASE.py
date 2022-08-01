def swap_case(s):
    c=''
    for i in range(len(s)):
        if s[i].islower()==True:
            c=c+s[i].upper()
        elif s[i].islower()==False:
            c=c+s[i].lower()
        else:
            c=c+i
    return c

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)