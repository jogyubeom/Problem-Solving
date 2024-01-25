C = int(input())
test_case = {}
for n in range(C):
    test_case[n] = list(map(int,input().split()))

for n in range(C):
    case = test_case[n]
    N = case[0]
    score = []
    for n in range(1, N + 1):
        score.append(case[n])
    average = sum(score)/N
    above_average = 0
    for S in score:
        if S > average:
            above_average += 1
    above_ratio = round((above_average / N) * 100, 3)
    print(above_ratio,'%',sep='')