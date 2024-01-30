mushroom_list = []
for _ in range(10):
    mushroom_list.append(int(input()))
mushroom_sum = 0
for n in range(10):
    compare_sum = mushroom_sum
    mushroom_sum += mushroom_list[n]
    if abs(100-mushroom_sum) > abs(100-compare_sum):
        print(compare_sum)
        break
    elif abs(100-mushroom_sum) == abs(100-compare_sum):
        print(mushroom_sum)
        break
    elif n == 9:
        print(mushroom_sum)
    else:
        pass