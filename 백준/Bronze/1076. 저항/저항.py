
resistance = {
  'black': 0,
  'brown': 1,
  'red': 2,
  'orange': 3,
  'yellow': 4,
  'green': 5,
  'blue': 6,
  'violet': 7,
  'grey': 8,
  'white': 9
}

x = input()
y = input()
z = input()

num = str(resistance[x]) + str(resistance[y])
print(int(num) * 10**resistance[z])
