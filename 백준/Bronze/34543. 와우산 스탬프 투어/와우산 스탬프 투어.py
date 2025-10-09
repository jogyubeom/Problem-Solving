N = int(input())
W = int(input())
p = 0

p += N * 10
if N >= 3:
    p += 20
if N == 5:
    p += 50
if W > 1000:
    p -= 15

if p < 0:
    print(0)
else:
    print(p)
