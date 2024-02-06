N, K = map(int, input().split())    # N = 국가 수, K = 등수 알려는 국가
country = {}   # 국가 별 현황
count = 0   # k국 보다 앞서있는 나라
for _ in range(N):
    a, b, c, d = map(int, input().split())  # [국가, 금, 은, 동메달 수]
    country[a] = [b, c, d]
for c in range(1, N+1):
    if c != K and country[c][0] > country[K][0]:    # 금메달이 k국 보다 많음
        count += 1
    elif c != K and country[c][0] == country[K][0] and \
            country[c][1] > country[K][1]:
        count += 1
    elif c != K and country[c][0] == country[K][0] and \
            country[c][1] == country[K][1] and \
            country[c][2] > country[K][2]:
        count += 1

print(count + 1)