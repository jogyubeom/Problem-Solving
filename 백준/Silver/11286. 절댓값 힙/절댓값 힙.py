
import heapq
import sys
input = sys.stdin.readline

minus = []
plus = []

for _ in range(int(input())):
    x = int(input())
    if x:
        if x < 0:
            heapq.heappush(minus, -x)
        else:
            heapq.heappush(plus, x)
    
    else:
        if len(minus) == 0 and len(plus) == 0:
            print(0)
        else:
            if len(minus) == 0:
                print(heapq.heappop(plus))
            elif len(plus) == 0:
                print(-heapq.heappop(minus))
            else:
                if minus[0] > plus[0]:
                    print(heapq.heappop(plus))
                else:
                    print(-heapq.heappop(minus))
