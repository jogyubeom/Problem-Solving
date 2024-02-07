the_rest = set()
for _ in range(10):
    n = int(input())
    the_rest.add(n % 42)
print(len(the_rest))