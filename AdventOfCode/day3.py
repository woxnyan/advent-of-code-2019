import sys
pathPoint = [[] for i in range(2)]
count = 0
with open('./day3.txt', 'r', encoding='utf-8') as f:
    for line in f:
        word = line.split(',')
        pathPoint[count] = word
        count += 1
# pathData = [[] for i in range(2)]  List 循环效率太低，切换成set所以代码有点乱，用set可以过滤重复得点，而且效率很快，快了将近 5500 倍
pathDataA = set()
currentPoint = [0, 0]
totalStep = 0
stepMapA = {}
for point in pathPoint[0]:
    direct = point[0]
    step = point[1:]
    currentX = currentPoint[0]
    currentY = currentPoint[1]
    if direct == 'R':
        for xStep in range(int(step)):
            currentX += 1
            pathDataA.add((currentX, currentY))
            totalStep+=1
            key = str(currentX)+str(currentY)
            if key in stepMapA:
                mapValue = stepMapA[key]
                if mapValue>totalStep:
                    stepMapA[str(currentX)+str(currentY)] = totalStep
            else:
                stepMapA[str(currentX)+str(currentY)] = totalStep
        currentPoint[0] = currentX
    elif direct == 'L':
        for xStep in range(int(step)):
            currentX -= 1
            pathDataA.add((currentX, currentY))
            totalStep+=1
            key = str(currentX)+str(currentY)
            if key in stepMapA:
                mapValue = stepMapA[key]
                if mapValue>totalStep:
                    stepMapA[str(currentX)+str(currentY)] = totalStep
            else:
                stepMapA[str(currentX)+str(currentY)] = totalStep
        currentPoint[0] = currentX
    elif direct == 'U':
        for xStep in range(int(step)):
            currentY += 1
            pathDataA.add((currentX, currentY))
            totalStep+=1
            key = str(currentX)+str(currentY)
            if key in stepMapA:
                mapValue = stepMapA[key]
                if mapValue>totalStep:
                    stepMapA[str(currentX)+str(currentY)] = totalStep
            else:
                stepMapA[str(currentX)+str(currentY)] = totalStep
        currentPoint[1] = currentY
    elif direct == 'D':
        for xStep in range(int(step)):
            currentY -= 1
            pathDataA.add((currentX, currentY))
            totalStep+=1
            key = str(currentX)+str(currentY)
            if key in stepMapA:
                mapValue = stepMapA[key]
                if mapValue>totalStep:
                    stepMapA[str(currentX)+str(currentY)] = totalStep
            else:
                stepMapA[str(currentX)+str(currentY)] = totalStep
        currentPoint[1] = currentY
pathDataB = set()
currentPoint = [0, 0]
totalStep = 0
stepMapB = {}
for point in pathPoint[1]:
    direct = point[0]
    step = point[1:]
    currentX = currentPoint[0]
    currentY = currentPoint[1]
    if direct == 'R':
        for xStep in range(int(step)):
            currentX += 1
            pathDataB.add((currentX, currentY))
            totalStep+=1
            key = str(currentX)+str(currentY)
            if key in stepMapB:
                mapValue = stepMapB[key]
                if mapValue>totalStep:
                    stepMapB[str(currentX)+str(currentY)] = totalStep
            else:
                stepMapB[str(currentX)+str(currentY)] = totalStep
        currentPoint[0] = currentX
        
    elif direct == 'L':
        for xStep in range(int(step)):
            currentX -= 1
            pathDataB.add((currentX, currentY))
            totalStep+=1
            key = str(currentX)+str(currentY)
            if key in stepMapB:
                mapValue = stepMapB[key]
                if mapValue>totalStep:
                    stepMapB[str(currentX)+str(currentY)] = totalStep
            else:
                stepMapB[str(currentX)+str(currentY)] = totalStep
        currentPoint[0] = currentX
        
    elif direct == 'U':
        for xStep in range(int(step)):
            currentY += 1
            pathDataB.add((currentX, currentY))
            totalStep+=1
            key = str(currentX)+str(currentY)
            if key in stepMapB:
                mapValue = stepMapB[key]
                if mapValue>totalStep:
                    stepMapB[str(currentX)+str(currentY)] = totalStep
            else:
                stepMapB[str(currentX)+str(currentY)] = totalStep
        currentPoint[1] = currentY
        
    elif direct == 'D':
        for xStep in range(int(step)):
            currentY -= 1
            pathDataB.add((currentX, currentY))
            totalStep+=1
            key = str(currentX)+str(currentY)
            if key in stepMapB:
                mapValue = stepMapB[key]
                if mapValue>totalStep:
                    stepMapB[str(currentX)+str(currentY)] = totalStep
            else:
                stepMapB[str(currentX)+str(currentY)] = totalStep
        currentPoint[1] = currentY
        
crossPoint = []
for a in pathDataA:
    if a in pathDataB:
        crossPoint.append(a)
minPoint = sys.maxsize
for cross in crossPoint:
    currentSum = abs(cross[0])+abs(cross[1])
    if currentSum < minPoint:
        minPoint = currentSum
print(minPoint)

minStep = sys.maxsize
for cross in crossPoint:
    stepCount = stepMapA[str(cross[0])+str(cross[1])] + stepMapB[str(cross[0])+str(cross[1])]
    if stepCount < minStep:
        minStep = stepCount
print(minStep)
