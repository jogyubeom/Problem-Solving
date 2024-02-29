import sys
# sys.stdin = open('input.txt')

N = int(input())    # 수의 개수
arr = [0] * 10001
for _ in range(N):
    arr[int(sys.stdin.readline())] += 1
for n in range(len(arr)):
    if arr[n] != 0:
        for _ in range(arr[n]):
            print(n)