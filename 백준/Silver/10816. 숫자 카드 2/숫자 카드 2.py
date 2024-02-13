my_dict = {}
N = int(input())    # 상근이가 가진 숫자 카드 개수
my_list = list(map(int, input().split()))   # 카드에 적힌 숫자들
M = int(input())    # 확인할 정수 개수
checklist = list(map(int, input().split()))     # 확인할 정수들

for n in range(N):
    if my_dict.setdefault(my_list[n], 0) >= 1:
        my_dict[my_list[n]] += 1
        continue
    my_dict[my_list[n]] = 1

for n in checklist:
    result = my_dict.setdefault(n, 0)
    print(f'{result}', end=' ')