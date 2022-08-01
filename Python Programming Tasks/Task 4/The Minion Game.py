def minion_game(string):
    l="AEIOU"
    size = len(string)
    t= int(size * (size + 1) / 2)
    k=0
    for i in range(size):
        if string[i] in l:
            k=k+(size-i)   
    s = t - k
    if s > k: 
        print(f"Stuart {s}")
    elif s < k: 
        print(f"Kevin {k}")
    else: 
        print("Draw")
    
if __name__ == '__main__':
    s = input()
    minion_game(s)