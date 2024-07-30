X = int(input())
stick = 2**6
count = 0
while X != 0:
    if X < stick:
        stick /= 2
    else:
        X -= stick
        count += 1
print(count)