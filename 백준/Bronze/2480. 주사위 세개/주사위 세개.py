arr = list(map(int, input().split()))
dice = [0] * 7
for i in arr:
    dice[i] += 1

case = max(dice)
if case == 3:
    print(10000 + arr[0] * 1000)
    
elif case == 2:
    n = dice.index(2)
    print(1000 + n * 100)
    
else:
    print(max(arr) * 100)