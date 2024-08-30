N = int(input())
five = N // 5
while True:
    remain = N - (five * 5)
    if remain % 3 == 0:
        three = remain // 3
        break
    five -= 1
    if five < 0:
        print(-1)
        exit()
print(five + three)
