N, X = map(int, input().split())
prices = list(map(int, input().split()))
temp = 1e9
for i in range(1, N):
    temp = min(temp, prices[i] + prices[i-1])
print(temp * X)