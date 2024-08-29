
S = input()
N = len(S) // 2 # 첫 N자리
flag = False
while True:
    for i in range(0, len(S) - 2 * N + 1):
        left = S[i:i + N]
        leftSum = 0
        for r in range(N):
            leftSum += int(left[r])
        right = S[i + N:i + 2 * N]
        rightSum = 0
        for c in range(N):
            rightSum += int(right[c])
        if leftSum == rightSum:
            flag = True
            break
    if flag is True:
        print(2 * N)
        break
    N -= 1
    if N == 0:
        print(0)
        break
