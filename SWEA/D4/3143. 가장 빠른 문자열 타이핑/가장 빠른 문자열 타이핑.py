T = int(input())
for tc in range(1, T+1):
    A, B = input().split()  # A = 전체 문자 , B = 저장된 문자열
    A = list(A)
    B = list(B)
    a = len(A)
    b = len(B)
    count = 0
    i = 0
    while i < a-b+1:
        for j in range(b):
            if A[i+j] != B[j]:
                break
        else:
            count += 1
            i += b
            continue
        i += 1

    result = a - (b-1) * count
    print(f'#{tc} {result}')