for _ in range(int(input())):
    nums = list(map(int, input().split()))
    num_sum = 0
    min_num = 1e9
    for n in nums:
        if n % 2 == 0:
            num_sum += n
            min_num = min(n, min_num)
    print(num_sum, min_num)