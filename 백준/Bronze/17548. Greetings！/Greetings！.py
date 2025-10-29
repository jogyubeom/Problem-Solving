word = input()
cnt = 0
for i in word:
    if i == "e":
        cnt += 1

cnt *= 2
print("h" + "e" * cnt + "y")