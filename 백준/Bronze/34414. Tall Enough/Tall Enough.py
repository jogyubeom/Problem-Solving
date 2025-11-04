res = True
for _ in range(int(input())):
    if int(input()) < 48:
        res = False
        break
print(res)