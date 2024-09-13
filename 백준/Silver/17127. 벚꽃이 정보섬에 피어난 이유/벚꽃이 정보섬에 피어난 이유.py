
N = int(input())
flowers_count = list(map(int, input().split()))
max_result = 0
for i in range(N-3):
    for j in range(i+1, N-2):
        for r in range(j+1, N-1):
            for c in range(r+1, N):
                lists = [flowers_count[i:j], flowers_count[j:r], flowers_count[r:c], flowers_count[c:N]]
                results = []
                for lst in lists:
                    result = 1
                    for p in lst:
                        result *= p
                    results.append(result)
                rr = sum(results)
                max_result = max(max_result, rr)
print(max_result)
