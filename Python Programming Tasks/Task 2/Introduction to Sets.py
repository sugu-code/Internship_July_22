from __future__ import division

def average(array):
    array=set(array)
    avg=0
    for i in array:
        avg+=i
    return avg/len(array)

if __name__ == '__main__':
    n = int(raw_input())
    arr = map(int, raw_input().split())
    result = average(arr)
    print result