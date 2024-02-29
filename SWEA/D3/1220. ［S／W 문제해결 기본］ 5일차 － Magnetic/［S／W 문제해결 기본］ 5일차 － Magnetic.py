for tc in range(1, 11):
    N = int(input())    # 테이블 한 변의 길이
    table = [list(map(int, input().split())) for _ in range(N)]   # 테이블 입력, 1=N극, 2=S극
    count = 0   # 교착 상태 개수
    flag = 0    # 만나서 교착 상태가 이루어지는 극
    for j in range(N):
        for i in range(N):
            if table[i][j] == 1:
                flag = 'S'
            elif table[i][j] == 2 and flag == 'S':
                count += 1
                flag = 'N'
        flag = 0
    print(f'#{tc} {count}')