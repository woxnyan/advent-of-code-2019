import math
import copy
inputArr = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,2,9,19,23,1,23,6,27,1,13,27,31,1,31,10,35,1,9,35,39,1,39,9,43,2,6,43,47,1,47,5,51,2,10,51,55,1,6,55,59,2,13,59,63,2,13,63,67,1,6,67,71,1,71,5,75,2,75,6,79,1,5,79,83,1,83,6,87,2,10,87,91,1,9,91,95,1,6,95,99,1,99,6,103,2,103,9,107,2,107,10,111,1,5,111,115,1,115,6,119,2,6,119,123,1,10,123,127,1,127,5,131,1,131,2,135,1,135,5,0,99,2,0,14,0]
myArr = [[] for i in range(len(inputArr)//4+1)]
def getNewArr():
    global myArr
    myArr = [[] for i in range(len(inputArr)//4+1)]
    for i,myNum in enumerate(inputArr):
        if myNum == 99 and i%4==0:
            break
        myArr[i//4].append(myNum)

for i in range(100):
    for j in range(100):
        inputArr = [1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,13,19,2,9,19,23,1,23,6,27,1,13,27,31,1,31,10,35,1,9,35,39,1,39,9,43,2,6,43,47,1,47,5,51,2,10,51,55,1,6,55,59,2,13,59,63,2,13,63,67,1,6,67,71,1,71,5,75,2,75,6,79,1,5,79,83,1,83,6,87,2,10,87,91,1,9,91,95,1,6,95,99,1,99,6,103,2,103,9,107,2,107,10,111,1,5,111,115,1,115,6,119,2,6,119,123,1,10,123,127,1,127,5,131,1,131,2,135,1,135,5,0,99,2,0,14,0]
        inputArr[1] = i
        inputArr[2] = j
        loopIndex = 0
        while(1):
            try:
                getNewArr()
                if len(myArr[loopIndex])<4:
                    break
                num1 = inputArr[myArr[loopIndex][1]]
                num2 = inputArr[myArr[loopIndex][2]]
                result = 0
                if myArr[loopIndex][0] == 1:
                    result = num1+num2
                else:
                    result = num1*num2
                inputArr[myArr[loopIndex][3]] = result
                loopIndex+=1
            except Exception as e:
                break
        if inputArr[0] == 19690720:
            print(inputArr[1]*100+inputArr[2])