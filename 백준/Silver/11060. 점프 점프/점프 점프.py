from collections import deque

N = int(input())    # 미로 크기
maze = list(map(int, input().split()))
record = []
for i in range(N):
    record.append(i+maze[i])
start = 0
count = 1
result = -1
que = deque()
que.append(record[0])
while que:
    current = que.popleft()
    if current >= N-1:
        result = count
        break
    next = max(record[start:current+1])
    if next <= current:
        break
    que.append(next)
    count += 1
    start = current
if N == 1:
    result = 0

print(result)
