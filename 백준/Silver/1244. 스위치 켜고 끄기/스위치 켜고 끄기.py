def switch(v):
    if arr[v] == 0:
        arr[v] = 1
    else:
        arr[v] = 0


N = int(input())    # 스위치 개수
arr = list(map(int, input().split()))   # 스위치 상태
for i in range(int(input())):
    G, num = map(int, input().split())  # 성별, 숫자 입력
    if G == 1:  # 남자일 때
        for n in range(N):
            if (n+1) % num == 0:
                switch(n)
    else:   # 여자일 때
        switch(num-1)
        c = 1
        while 0 <= num-1-c and num+c <= N:
            if arr[num-1-c] == arr[num-1+c]:
                switch(num-1-c)
                switch(num-1+c)
            else:
                break
            c += 1
for i in range(0, len(arr), 20):
    print(*arr[i:i+20])