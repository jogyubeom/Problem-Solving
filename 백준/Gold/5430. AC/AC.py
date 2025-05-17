
from collections import deque
import sys
input = sys.stdin.readline

for _ in range(int(input())):
    order = input()
    N = int(input())
    temp = input()
    if N == 0:
        arr = []
    elif N == 1:
        arr = deque()
        arr.append(temp[1:-2])
    else:
        temp = temp[1:-2]
        arr = deque(temp.split(','))

    check = 1
    for f in order:
        if f == 'R':
            check *= -1
        elif f == 'D':
            if len(arr) == 0:
                print('error')
                break
            else:
                if check > 0:
                    arr.popleft()
                else:
                    arr.pop()
    
    else:
        n = len(arr)
        if n == 0:
            result = '[]'
        
        else:
            result = '['
            if check > 0:
                for i in range(n):
                    result += arr[i]
                    if i != n - 1:
                        result += ','
                    else:
                        result += ']'
            else:
                for i in range(n - 1, -1, -1):
                    result += arr[i]
                    if i != 0:
                        result += ','
                    else:
                        result += ']'
        
        print(result)
