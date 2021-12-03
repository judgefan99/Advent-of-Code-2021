lines = []
with open('day2.txt') as f:
    lines = f.readlines()

cleanlines = []
depth = 0
forwards = 0
aim = 0

for element in lines:
    cleanlines.append(element.strip())

lines = cleanlines

for element in lines:
    if len(element) == 9:
        forwards = forwards + int(element[-1])
        depth = depth + (int(aim)) * (int(element[-1]))
    if len(element) == 6:
        aim = aim + int(element[-1])
    if len(element) == 4:
        aim = aim - int(element[-1])

print(int(forwards * depth))
