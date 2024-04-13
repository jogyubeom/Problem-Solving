
from collections import deque

N = int(input())    # 컴퓨터 수
adjl = [[] for _ in range(N+1)]     # 각 컴퓨터(인덱스)와 연결된 컴퓨터(리스트 내용) 정보
visited = [0] * (N+1)   # 각 컴퓨터 방문 정보
for _ in range(int(input())):
    a, b = map(int, input().split())
    adjl[a].append(b)
    adjl[b].append(a)

count = -1
start = 1
que = deque()
que.append(start)
while que:
    now = que.popleft()
    if visited[now]:
        continue
    visited[now] = 1
    count += 1
    for n in adjl[now]:
        que.append(n)
print(count)
