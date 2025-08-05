for _ in range(int(input())):
    price = float(input())
    res = f"{round(price * 0.8, 2):.2f}"
    print("$" + str(res))