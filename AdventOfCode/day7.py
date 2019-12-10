import math
import copy

# 获取所有排列组合
inputArrSecond = [5,6,7,8,9]
allArr = []
isAdd = False
def getAllSitiation(deliverArr = []):
    global inputArrSecond,allArr,isAdd
    currentArr = copy.deepcopy(deliverArr)
    for inputNum in list(set(inputArrSecond).difference(set(currentArr))):
        deliverArr.append(inputNum)
        if len(currentArr) + 1 == len(inputArrSecond):
            addArr = copy.deepcopy(deliverArr)
            allArr.append(addArr)
        else:
            getAllSitiation(deliverArr)
        deliverArr.remove(inputNum)
            
getAllSitiation([])

def calcMaxOutPut2(innerArr):
    maxValue = 0
    maxArr = []
    lastInput = [0]
    currentInputIndex = 0
    currentIndex = 0
    initValue = 0
    initArr = [3,8,1001,8,10,8,105,1,0,0,21,30,39,64,81,102,183,264,345,426,99999,3,9,1001,9,2,9,4,9,99,3,9,1002,9,4,9,4,9,99,3,9,1002,9,5,9,101,2,9,9,102,3,9,9,1001,9,2,9,1002,9,2,9,4,9,99,3,9,1002,9,3,9,1001,9,5,9,1002,9,3,9,4,9,99,3,9,102,4,9,9,1001,9,3,9,102,4,9,9,1001,9,5,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,1,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,99]
    positionDict = {}
    arrDict = {}
    for i,num in enumerate(innerArr):
        positionDict[num] = initValue
        arrDict[num] = initArr
    while True:
        for j, innerNum in enumerate(innerArr):
            inputArr = copy.deepcopy(arrDict[innerNum])
            currentPoint = positionDict[innerNum]
            if currentIndex < 5:
                lastInput.insert(0, innerNum)
            arrLen = len(lastInput)
            while True:
                positionDict[innerNum] = currentPoint
                currentStr = str(inputArr[currentPoint])
                fullStr = currentStr.zfill(5)
                opCode = fullStr[3:]
                if opCode == '03':
                    if arrLen == 0:
                        arrDict[innerNum] = inputArr
                        break
                    inputNum = lastInput.pop(0)
                    arrLen -= 1
                    inputArr[inputArr[currentPoint+1]] = int(inputNum)
                    currentPoint += 2
                    currentInputIndex += 1
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
                    lastInput.append(inputArr[inputArr[currentPoint+1]])
                    if j == len(innerArr) - 1:
                        if maxValue < lastInput[len(lastInput)-1]:
                            maxValue = lastInput[len(lastInput)-1]
                            maxArr = innerArr
                    # break
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
                if opCode == '99':
                    if j == len(innerArr) - 1:
                        return maxValue
                    arrDict[innerNum] = inputArr
                    break
                if currentPoint >= len(inputArr):
                    arrDict[innerNum] = inputArr
                    break
            currentIndex += 1


def calcMaxOutPut():
    global allArr
    maxValue = 0
    for i,innerArr in enumerate(allArr):
        valueNew = calcMaxOutPut2(innerArr)
        if valueNew>maxValue:
            maxValue = valueNew
    print(maxValue)
calcMaxOutPut()
