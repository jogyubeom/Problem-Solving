import sys
input = sys.stdin.readline


N = int(input())
take_money = dict()
for i in range(N):
    a, b, c = map(int, input().split())
    if take_money.get(b-a):
        take_money[b-a] += c
    else:
        take_money[b-a] = c
result = max(take_money.values())
print(result)