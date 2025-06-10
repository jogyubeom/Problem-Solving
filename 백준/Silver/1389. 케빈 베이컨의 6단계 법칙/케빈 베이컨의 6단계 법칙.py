from collections import deque
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
check = dict()

for _ in range(M):
    a, b = map(int, input().split())
    temp = check.get(a, set())
    temp.add(b)
    check[a] = temp

    temp = check.get(b, set())
    temp.add(a)
    check[b] = temp

def bfs(x, y):
    que = deque()
    que.append((x, 0))
    visited = [1e9] * (N + 1)
    while que:
        temp = que.popleft()
        now = temp[0]
        count = temp[1]
        if now == y:
            return count
        for i in check[now]:
            if visited[i] > count + 1:
                que.append((i, count + 1))
                visited[i] = count + 1

min_count = 1e9
kevin = 1e9

for x in range(1, N+1):
    res = 0
    for y in range(1, N+1):
        if x == y:
            continue
        res += bfs(x, y)
    
    if res == min_count:
        kevin = min(kevin, x)
    elif res < min_count:
        min_count = res
        kevin = x

print(kevin)