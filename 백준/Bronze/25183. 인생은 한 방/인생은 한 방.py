N = int(input())
S = input()
count = 0
for i in range(1, N):
    if abs(ord(S[i-1]) - ord(S[i])) == 1:
        count += 1
    else:
        count = 0
    if count >= 4:
        print('YES')
        break
else:
    print('NO')
