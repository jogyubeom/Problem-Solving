N, M = map(int,input().split())
basket_order = list(range(1,N+1))
for n in range(M):
    i, j = map(int,input().split())
    turn_list = basket_order[i-1:j]
    turn_list.reverse()
    basket_order[i-1:j] = turn_list
    
for i in basket_order:
    print(i, end=' ')
