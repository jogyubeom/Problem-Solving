L = int(input())    # 집합의 크기
S = list(map(int, input().split()))
n = int(input())

S.sort()
count = 0
start = 1
end = 0
flag = False
for i in range(L):
    if S[i] == n:
        flag = True
        break
    elif S[i] > n:
        end = S[i]
        if i != 0 and S[i-1] < n:
            start = S[i-1] + 1
        break


if flag == True:
    print(0)
else:
    good = list(range(start, end))
    # print(f'start = {start}, end = {end}, good = {good}')
    num = len(good)
    if num < 2:
        print(0)
    else:
        for i in range(num - 1):
            if good[i] > n:
                continue
            for j in range(i + 1, num):
                if good[j] < n:
                    continue
                count += 1
        print(count)


