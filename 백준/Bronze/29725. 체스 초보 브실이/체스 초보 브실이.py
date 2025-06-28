w = ['P', 'N', 'B', 'R', 'Q']
b = ['p', 'n', 'b', 'r', 'q']
p = [1, 3, 3, 5, 9]
wp = 0
bp = 0
for _ in range(8):
    line = input()
    for i in line:
        for j in range(5):
            if w[j] == i:
                wp += p[j]
            elif b[j] == i:
                bp += p[j]
print(wp - bp)