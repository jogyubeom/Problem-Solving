good = [1, 2, 3, 3, 4, 10]
evil = [1, 2, 2, 2, 3, 5, 10]
for b in range(int(input())):
    gp = 0
    ep = 0
    g = list(map(int, input().split()))
    e = list(map(int, input().split()))
    for i in range(6):
        gp += g[i] * good[i]
    for j in range(7):
        ep += e[j] * evil[j]
        
    if gp > ep:
        print(f"Battle {b + 1}: Good triumphs over Evil")
    elif ep > gp:
        print(f"Battle {b + 1}: Evil eradicates all trace of Good")
    else:
        print(f"Battle {b + 1}: No victor on this battle field")
        
    