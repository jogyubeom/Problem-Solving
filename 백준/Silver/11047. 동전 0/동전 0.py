
N, K = map(int, input().split())
money = []
for _ in range(N):
    money.append(int(input()))
money.sort(reverse=True)
count = 0
for i in range(N):
    if K == 0:
        break
    while money[i] <= K:
        K -= money[i]
        count += 1
print(count)