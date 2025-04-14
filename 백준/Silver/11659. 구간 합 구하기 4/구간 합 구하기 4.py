import sys
input = sys.stdin.readline
    
N, M = map(int, input().split())
numbers = [0] + list(map(int, input().split()))
count = 0
for n in range(N + 1):
    count += numbers[n]
    numbers[n] = count

for _ in range(M):
    i, j = map(int, input().split())
    res = numbers[j] - numbers[i - 1]
    print(res)