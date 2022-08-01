def merge_the_tools(string, k):
    output=[]
    for i in range(0,len(string),k):
        output.append(string[i:i+k])
    for s in output:
        result=''
        for j in range(k):
            if (s[j] not in result):
                result+=s[j]
        print(result)

    
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)