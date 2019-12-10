import math
sum = 0
def getFuel(fuel):
    needFuel = math.floor(fuel/3)-2
    if needFuel>0:
        global sum
        sum += needFuel
        getFuel(needFuel)
with open('./test.txt', 'r', encoding = 'utf-8') as f:
    for line in f:
        num = int(line)
        getFuel(num)
print(sum)