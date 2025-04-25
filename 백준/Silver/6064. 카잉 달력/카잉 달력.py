
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    M, N, x, y = map(int, input().split())
    count = x
    if y == N:
        y = 0
    
    while True:

        if count % N == y:
            print(count)
            break

        count += M

        if count > M*N:
            print(-1)
            break

