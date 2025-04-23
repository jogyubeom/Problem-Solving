
import sys
input = sys.stdin.readline

arr = input()
res = []
num = ''
temp = 0

for i in range(len(arr)):
    if arr[i] == '+':
        temp += int(num)
        num = ''
    
    elif arr[i] == '-':
        temp += int(num)
        res.append(-temp)
        temp = 0
        num = ''
    
    elif i == len(arr) - 1:
        temp += int(num)
        res.append(-temp)

    else:
        num += arr[i]

res[0] *= -1
print(sum(res))