T = int(input())
zero = [1, 0, 1, 1]
one = [0, 1, 1, 2]
for i in range(3, 40):
    zero.append(zero[i-1] + zero[i])
    one.append(one[i-1] + one[i])
for _ in range(T):
    N = int(input())
    print(zero[N], end=' ')
    print(one[N])