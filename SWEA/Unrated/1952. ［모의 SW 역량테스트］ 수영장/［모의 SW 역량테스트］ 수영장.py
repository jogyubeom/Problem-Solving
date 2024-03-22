T = int(input())
for tc in range(1,1+T):
    cost = list(map(int, input().split()))
    # 인덱스가 1월부터 들어갔으면 좋겠다! 그럼 0 리스트 하나 더해주면 된다.
    days = [0] + list(map(int, input().split()))
    # DP 배열
    plans = [0] * 13

    # 1~12월까지 반복
    for i in range(1, 13):
        # 현재 달의 최소 비용 계산
        # 이전 달 + 1일권 구입 / 이전 달 + 1달권 구입 / 3달 전 + 3달권 구입 중에서 최소값!
        plans[i] = min(plans[i-1] + days[i] * cost[0], plans[i-1] + cost[1])

        if i >= 3:
            plans[i] = min(plans[i], plans[i-3] + cost[2])

    # 12월까지의 계산 결과와 1년권 가격을 비교
    min_cost = min(plans[12], cost[3])
    print(f'#{tc} {min_cost}')