for _ in range(int(input())):
    N, A = map(int, input().split())
    documents = list(map(int, input().split()))
    printed = [0] * N
    count = 0
    now = 0
    while True:
       if printed[now] == 1:
            now = (now + 1) % N
            continue
       else:
            document = documents[now]
            for i in range(N):
                if documents[i] > document and printed[i] == 0:
                        now = (now + 1) % N
                        break
            else:
                printed[now] = 1
                count += 1
                if now == A:
                    print(count)
                    break
                now = (now + 1) % N
           
