my_dict = {}
N = int(input())    # 상근이가 가진 숫자 카드 개수
my_list = list(map(int, input().split()))   # 카드에 적힌 숫자들
M = int(input())    # 확인할 정수 개수
checklist = list(map(int, input().split()))     # 확인할 정수들

for n in range(N):
    my_dict[my_list[n]] = 0

for n in range(M):
    if checklist[n] in my_dict:
        print(1, end=' ')
    else:
        print(0, end=' ')