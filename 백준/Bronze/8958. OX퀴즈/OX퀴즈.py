T = int(input())
for _ in range(T):
    result = input()
    score = 0
    score_sum = 0
    for n in range(len(result)):
        if result[n] == 'O':
            score += 1
            score_sum += score
        else:
            score = 0
    print(score_sum)