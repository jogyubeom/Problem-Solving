H, M = map(int,input().split())

new_M = M - 45
if new_M >= 0:
    print(H,new_M)
elif new_M < 0:
    H -= 1
    new_M += 60
    if H < 0:
        H = 23
    print(H,new_M)