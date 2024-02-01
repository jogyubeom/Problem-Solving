def binary_search(P,A):
    start = 1
    end = P
    c = 0
    count = 0
    while c != A:
        c = int((start + end)/2)
        count += 1
        if A > c:
            start = c
        elif A < c:
            end = c
    return count

T = int(input())
for tc in range(1, T+1):
    P, A, B = map(int, input().split())
    if binary_search(P,A) < binary_search(P,B):
        print(f'#{tc} A')
    elif binary_search(P,A) > binary_search(P,B):
        print(f'#{tc} B')
    else:
        print(f'#{tc} 0')