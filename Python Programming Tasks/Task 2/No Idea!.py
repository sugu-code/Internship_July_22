# Enter your code here. Read input from STDIN. Print output to STDOUT
if __name__ == "__main__":
    h = 0
    n, m = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    
    g = set(map(int, input().strip().split(' ')))
    b = set(map(int, input().strip().split(' ')))
    
    for i in arr:
        if i in g:
            h += 1
        elif i in b:
            h -= 1
    print(h)