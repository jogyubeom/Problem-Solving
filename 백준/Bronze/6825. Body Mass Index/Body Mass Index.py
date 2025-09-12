w = float(input())
h = float(input())

BMI = w / (h * h)

if BMI > 25:
    print("Overweight")
elif 18.5 < BMI:
    print("Normal weight")
else:
    print("Underweight")