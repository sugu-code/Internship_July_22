if __name__ == '__main__':
    records=[]
    low1=100
    low2=100
    m=[]
    for i in range(int(input())):
        name = input()
        score = float(input())
        l=[name,score]
        records.append(l)
    for name, score in records:
        if low1>=score:
            low1=score
    for name, score in records:
        if score !=low1:
            if low2>=score:
                low2=score
    for name, score in records:
        if score ==low2:  
              m.append(name)   
    m.sort()
    for f in m:
        print(f)