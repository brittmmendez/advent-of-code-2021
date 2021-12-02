lines = []
horizontal = 0
depth = 0

with open('/Users/brittanymorris/Desktop/advent-of-code-2021/02/input.txt') as f:
    lines = f.readlines()

for line in lines:
    x = line.split()
    position = x[0]
    amount = int(x[1])

    if position == 'forward':
        horizontal += amount
    elif position == 'down':
        depth += amount
    elif position == 'up':
        depth -= amount

print (horizontal*depth)
