def select(v):
    global count
    end = v
    for w in work_list:
        if w[0] >= end:
            count += 1
            end = w[1]


T = int(input())  # 테스트 케이스
for tc in range(1, 1 + T):
    N = int(input())  # 신청서 개수
    work_list = []      # 작업들
    for _ in range(N):
        s, e = map(int, input().split())    # 각 작업의 시작 시간과 종료 시간 튜플 입력
        work_list.append((s, e))
    work_list.sort(key=lambda x: x[1])
    count = 0
    select(0)
    print(f'#{tc} {count}')
