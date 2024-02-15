for _ in range(1, 11):
    T = int(input())    # 케이스 번호
    arr = list(map(int, input().split()))  # 데이터 입력 (8개 숫자)
    front = 0
    flag = False
    while flag is False:
        for n in range(5):
            arr[front] -= n + 1
            if arr[front] <= 0:
                arr[front] = 0
                flag = True
                front = (front + 1) % 8
                break
            front = (front + 1) % 8
    result = arr[front:] + arr[:front]

    print(f'#{T}', end=' ')
    print(*result)