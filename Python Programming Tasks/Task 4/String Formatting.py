def print_formatted(number):
    s = len(bin(number)[2:])
    for i in range(1,number+1):
        print(str(i).rjust(s,' '),end=" ")
        print(oct(i)[2:].rjust(s,' '),end=" ")
        print(((hex(i)[2:]).upper()).rjust(s,' '),end=" ")
        print(bin(i)[2:].rjust(s,' '),end=" ")
        print("")
        
        
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)