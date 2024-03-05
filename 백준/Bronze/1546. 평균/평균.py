N = int(input())    # 시험 본 과목 수
score_lst = list(map(int, input().split()))
M = max(score_lst)
score_sum = 0
for score in score_lst:
    score_sum += score * 100 / M
print(score_sum / N)