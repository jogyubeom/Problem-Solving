T = int(input())
for _ in range(T):
    note1 = set()
    N = int(input())
    Num = list(map(int, input().split()))
    for n in Num:
        note1.add(n)
    M = N = int(input())
    Mum = list(map(int, input().split()))
    for n in Mum:
        if n in note1:
            print(1)
        else:
            print(0)
