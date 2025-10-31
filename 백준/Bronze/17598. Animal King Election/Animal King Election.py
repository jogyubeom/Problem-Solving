T = 0
L = 0
for _ in range(9):
    v = input()
    if v == "Tiger":
        T += 1
    else:
        L += 1

if T > L:
    print("Tiger")
else:
    print("Lion")