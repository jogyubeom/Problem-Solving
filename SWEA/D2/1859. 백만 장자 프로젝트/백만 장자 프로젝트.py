T = int(input())
for tc in range(1, 1 + T):
    N = int(input())   # 날짜 수
    arr = list(map(int, input().split()))   # 매매가 리스트
    profit = 0
    max_price = arr.pop()
    for n in range(N-1):
        price = arr.pop()
        if max_price < price:
            max_price = price
        else:
            profit += max_price - price
    print(f'#{tc} {profit}')
