T = int(input())
for tc in range(1, T+1):
    arr = input()
    N = len(arr)

    isPalindrome = 1
    for i in range(N//2):   # 절반으로 쪼개서 다 교환한 후에 비교할 필요 없이
        if arr[i] != arr[N-1-i]:    # 절반으로 나눠서 비교한 것이 다 같으면 회문이라고 판단가능
            isPalindrome = 0    # 중간에 다른거 발견하면 더 비교할 것 없이 반복 빠져나온다
            break                   # 다 뒤집지 않고도 회문을 판별할 수 있다

    print(f'#{tc} {isPalindrome}')