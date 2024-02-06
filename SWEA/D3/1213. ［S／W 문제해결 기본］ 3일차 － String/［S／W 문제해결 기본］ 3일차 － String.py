for t in range(1, 11):
    tc = input()
    A = input()  # A = 찾을 문자열 , B = 전체 문자열
    B = input()
    n = 0
    count = 0
    while n <= len(B)-len(A):
        for i in range(len(A)):
            if B[n + i] != A[i]:
                break
        else:
            count += 1
            n += len(A)
            continue
        n += 1

    print(f'#{tc} {count}')