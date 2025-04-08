N, M = map(int, input().split())
prices = []
for _ in range(M):
    prices.append(int(input()))

prices.sort()
maxProfit = 0
minPrice = 1e9

for i in range(M):
    price = prices[i]
    eggs = M - i
    if eggs > N:
        eggs = N
    profit = eggs * price
    if profit == maxProfit:
        minPrice = min(minPrice, price)
    elif profit > maxProfit:
        maxProfit = profit
        minPrice = price

print(minPrice, maxProfit)
    
