import textwrap

def wrap(string, max_width):
    h=len(string)%max_width
    for i in range(0,len(string)-1,max_width):
        c=string[i]
        if i+h!=len(string):
            for j in range(1,max_width):
                c=c+string[i+j]
            print(c)
        else:
            for k in range(i+1,len(string)):
                c=c+string[k]    
    return str(c)    
    

if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)