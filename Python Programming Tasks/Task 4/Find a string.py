def count_substring(string, sub_string):
    c=0
    for i in range(len(sub_string)):
        if i+len(sub_string)<=len(string):
            for j in range(len(string)):
                if sub_string[i]==string[j]:
                    h=0
                    for k in range(len(sub_string)):
                        if j+k<=len(string):
                            if sub_string[k]==string[j+k]:
                                h+=1
                            if h==len(sub_string):
                                c=c+1              
    return c

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)