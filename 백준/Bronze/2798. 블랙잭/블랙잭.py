N, M = map(int, input().split())    # N = 카드 개수, M = 목표 수
cards = list(map(int, input().split()))
sum_v = []
for a in cards:
    for b in cards:
        if a != b:
            for c in cards:
                if a != c and b != c:
                    if a + b + c <= M:
                        sum_v.append(a+b+c)

print(max(sum_v))