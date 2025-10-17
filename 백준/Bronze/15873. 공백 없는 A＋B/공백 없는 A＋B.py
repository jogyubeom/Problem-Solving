nums = input()
temp = len(nums)
if temp == 2:
    print(int(nums[0]) + int(nums[1]))
elif temp == 4:
    print(20)
else:
    a = int(nums[0])
    b = int(nums[1])
    if int(nums[1]) == 0:
        a = 10
        b = int(nums[2])
    elif int(nums[2]) == 0:
        b = 10
    print(a + b)