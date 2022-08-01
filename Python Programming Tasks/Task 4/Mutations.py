def mutate_string(string, position, character):
    c=''
    for i in range(len(string)):
        if i==position:
            c=c+character
        else:
            c=c+string[i]
    return c

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)