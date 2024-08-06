
N, K = map(int, input().split())
array = list(range(1, N + 1))
josefus_lst = []
person = len(array) 
index = 0
while person != 0:
    index += K-1
    if index >= person:
        index %= person
    choose = array.pop(index)
    josefus_lst.append(choose)
    person -= 1
print('<', end='')
print(*josefus_lst, sep=', ' ,end='')
print('>')
