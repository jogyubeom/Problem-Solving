
import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    n = int(input())
    cloth_name = dict()
    for __ in range(n):
        name, kind = input().split()

        if cloth_name.get(kind):
            cloth_name[kind] += 1
        
        else:
            cloth_name[kind] = 1

    res = 1
    for i in cloth_name:
        res *= cloth_name[i] + 1
    print(res - 1)