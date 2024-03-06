import sys

T = int(input())
for n in range(1, 1+T):
    A, B = map(int, sys.stdin.readline().split())
    print(A+B)