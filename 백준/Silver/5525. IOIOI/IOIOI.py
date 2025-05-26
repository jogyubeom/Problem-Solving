
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()
temp = 'I' + 'OI' * N
count = 0
n = 0

while n < M - 2 * N:
    if S[n] != 'I':
        n += 1
    elif S[n:n + 2 * N + 1] == temp:
        count += 1
        while True:
            if S[n + 2 * N + 1:n + 2 * N + 3] == 'OI':
                count += 1
                n += 2
            else:
                break
        n += 2 * N + 1
    else:
        n += 1

print(count)