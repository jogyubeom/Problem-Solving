import sys
from collections import deque

input = sys.stdin.readline

    
N, M = map(int, input().split())
ladder_start = []
ladder_end = []
snake_start = []
snake_end = []
for _ in range(N):
    x, y = map(int, input().split())
    ladder_start.append(x)
    ladder_end.append(y)

for _ in range(M):
    x, y = map(int, input().split())
    snake_start.append(x)
    snake_end.append(y)

visited = [1e9] * 101

que = deque()
que.append((1, 0))

while que:
    now = que.popleft()
    num = now[0]
    count = now[1]
    for t in range(1, 7):
        next = num + t
        if next in ladder_start:
            next = ladder_end[ladder_start.index(next)]
        elif next in snake_start:
            next = snake_end[snake_start.index(next)]
        
        if next > 100:
            continue
        
        if visited[next] <= count + 1:
            continue
        visited[next] = count + 1
        if next != 100:
            que.append((next, count + 1))

print(visited[100])