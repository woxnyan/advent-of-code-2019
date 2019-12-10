import math
import copy
inputArr = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
currentPoint = 0
while True:
    currentStr = str(inputArr[currentPoint])
    fullStr = currentStr.zfill(5)
    opCode = fullStr[3:]
    if opCode == '03':
        inputNum = input('Enter your num')
        inputArr[inputArr[currentPoint+1]] = int(inputNum)
        currentPoint += 2
    if opCode == '01' or opCode == '02':
        num1 = inputArr[currentPoint+1]
        num2 = inputArr[currentPoint+2]
        num3 = inputArr[currentPoint+3]
        opCode1 = fullStr[2]
        opCode2 = fullStr[1]
        opCode3 = fullStr[0]
        realNum1 = num1
        if opCode1 == '0':
            realNum1 = inputArr[num1]
        realNum2 = num2
        if opCode2 == '0':
            realNum2 = inputArr[num2]
        result = 0
        if opCode == '01':
            result = realNum1 + realNum2
        if opCode == '02':
            result = realNum1 * realNum2
        inputArr[num3] = result
        currentPoint += 4
    if opCode == '04':
        print(inputArr[inputArr[currentPoint+1]])
        currentPoint += 2
    if opCode == '05':
        num1 = inputArr[currentPoint+1]
        num2 = inputArr[currentPoint+2]
        opCode1 = fullStr[2]
        opCode2 = fullStr[1]
        realNum1 = num1
        if opCode1 == '0':
            realNum1 = inputArr[num1]
        if realNum1 != 0:
            realNum2 = num2
            if opCode2 == '0':
                realNum2 = inputArr[num2]
            currentPoint = realNum2
        else:
            currentPoint += 3
    if opCode == '06':
        num1 = inputArr[currentPoint+1]
        num2 = inputArr[currentPoint+2]
        opCode1 = fullStr[2]
        opCode2 = fullStr[1]
        realNum1 = num1
        if opCode1 == '0':
            realNum1 = inputArr[num1]
        if realNum1 == 0:
            realNum2 = num2
            if opCode2 == '0':
                realNum2 = inputArr[num2]
            currentPoint = realNum2
        else:
            currentPoint += 3
    if opCode == '07':
        num1 = inputArr[currentPoint+1]
        num2 = inputArr[currentPoint+2]
        num3 = inputArr[currentPoint+3]
        opCode1 = fullStr[2]
        opCode2 = fullStr[1]
        realNum1 = num1
        if opCode1 == '0':
            realNum1 = inputArr[num1]
        realNum2 = num2
        if opCode2 == '0':
            realNum2 = inputArr[num2]
        if realNum1 < realNum2:
            inputArr[num3] = 1
        else:
            inputArr[num3] = 0
        currentPoint += 4
    if opCode == '08':
        num1 = inputArr[currentPoint+1]
        num2 = inputArr[currentPoint+2]
        num3 = inputArr[currentPoint+3]
        opCode1 = fullStr[2]
        opCode2 = fullStr[1]
        realNum1 = num1
        if opCode1 == '0':
            realNum1 = inputArr[num1]
        realNum2 = num2
        if opCode2 == '0':
            realNum2 = inputArr[num2]
        if realNum1 == realNum2:
            inputArr[num3] = 1
        else:
            inputArr[num3] = 0
        currentPoint += 4
    if currentPoint>len(inputArr):
        break
    