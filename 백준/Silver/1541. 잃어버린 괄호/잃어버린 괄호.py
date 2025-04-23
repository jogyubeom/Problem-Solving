
import sys
input = sys.stdin.readline

arr = input().split('-')
temp = []
for n in arr:
    num = sum(map(int, n.split('+')))
    temp.append(num)

res = temp[0] - sum(temp[1:])
print(res)
