
import heapq
import sys
input = sys.stdin.readline

q = []
N = int(input())
for _ in range(N):
    x = int(input())
    if x:
        heapq.heappush(q, -x)
    else:
        if len(q) == 0:
            print(0)
        else:
            num = heapq.heappop(q)
            print(-num)
