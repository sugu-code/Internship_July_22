def print_rangoli(size):
    string = ''
    w  = size*4-3
    for i in range(1,size+1):
        for j in range(0,i):
            string += chr(96+size-j)
            if len(string) < w :
                string += '-'
        for k in range(i-1,0,-1):    
            string += chr(97+size-k)
            if len(string) < w :
                string += '-'
        print(string.center(w,'-'))
        string = ''
    for i in range(size-1,0,-1):
        string = ''
        for j in range(0,i):
            string += chr(96+size-j)
            if len(string) < w :
                string += '-'
        for k in range(i-1,0,-1):
            string += chr(97+size-k)
            if len(string) < w :
                string += '-'
        print(string.center(w,'-'))
        

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)