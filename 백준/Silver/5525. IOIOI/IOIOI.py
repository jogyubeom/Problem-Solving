
import sys
input = sys.stdin.readline

N = int(input())
M = int(input())
S = input()
count = 0

def check(n):
    for i in range(2 * N + 1):
        if i % 2 == 0:
            if S[n + i] != 'I':
                return False
        else:
            if S[n + i] != 'O':
                return False
    
    return True

for n in range(M - 2 * N):
    if check(n):
        count += 1

print(count)