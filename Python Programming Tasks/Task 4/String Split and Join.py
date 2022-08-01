def split_and_join(line):
    c=''
    for i in line.split(' '):
        if c=='':
            c=i
        else:
            c=c+'-'+i
    return c

    
if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)