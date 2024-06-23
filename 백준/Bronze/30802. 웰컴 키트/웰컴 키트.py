N = int(input())     # 전체 참가자 수
sizes = list(map(int, input().split()))     # 사이즈별 신청자 수
T, P = map(int, input().split())  # 티셔츠와 펜 묶음 수
result1 = 0
for x in sizes:
    if x % T != 0:
        result1 += (x // T) + 1
    else:
        result1 += (x // T)
print(result1)

result2 = N // P
result3 = N % P
print(result2, result3)
