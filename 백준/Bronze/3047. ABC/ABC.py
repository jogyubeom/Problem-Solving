nums = list(map(int, input().split()))
nums.sort()
go = {'A':nums[0], "B":nums[1], "C":nums[2]}
order = input()
for i in order:
    print(go[i], end=" ")


