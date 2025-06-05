d = 0
p = 0
for _ in range(int(input())):
    temp = input()
    if temp == 'D':
        d += 1
    else:
        p += 1
    if abs(d-p) >= 2:
        break
print(f"{d}:{p}")