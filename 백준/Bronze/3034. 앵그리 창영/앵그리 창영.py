a, b, c = map(int, input().split())
d = (b**2 + c**2)**0.5
for i in range(a):
    temp = int(input())
    if temp <= d:
        print("DA")
    else:
        print("NE")