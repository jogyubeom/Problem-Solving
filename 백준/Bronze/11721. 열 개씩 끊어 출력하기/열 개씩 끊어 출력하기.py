words = input()
N = len(words)
ten_cut = N // 10
the_rest = N % 10

for t in range(ten_cut):
    print(words[0 + t * 10 : 10 + t * 10])
if the_rest:
    print(words[-the_rest:])
else:
    pass

