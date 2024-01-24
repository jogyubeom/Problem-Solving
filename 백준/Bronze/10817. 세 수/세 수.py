a, b, c = input().split()
A = int(a)
B = int(b)
C = int(c)
my_list = [A, B, C]
my_list.remove(max(my_list))
my_list.remove(min(my_list))
print(my_list[0])