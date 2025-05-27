
import sys
from collections import deque
input = sys.stdin.readline

for _ in range(int(input())):
    A, B = map(int, input().split())

    check = [0] * 10000
    q = deque()
    q.append((A, ''))

    while q:
        now, result = q.popleft()
        if now == B:
            print(result)
            break

        da = now * 2
        if da > 9999:
            da = da % 10000
        if check[da] == 0:
            check[da] = 1
            q.append((da , result + 'D'))

        if now == 0:
            sa = 9999
        else:
            sa = now - 1
        if check[sa] == 0:
            check[sa] = 1
            q.append((sa , result + 'S'))

        la = now // 1000 + (now % 1000) * 10
        if check[la] == 0:
            check[la] = 1
            q.append((la , result + 'L'))

        ra = now // 10 + (now % 10) * 1000
        if check[ra] == 0:
            check[ra] = 1
            q.append((ra , result + 'R'))
