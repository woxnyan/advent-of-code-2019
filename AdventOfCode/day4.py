471-781
num = 272091
correctArr = []
# 排除没有相邻相同数字的数
while num<=815432:
    # haveSame = False
    numStr = str(num)
    sameWordArr = []
    sameWordStr = ''
    for i in range(len(numStr)):
        if i<len(numStr) -1:
            if numStr[i]==numStr[i+1]:
                # haveSame = True
                sameWordStr += numStr[i]
                if i==len(numStr)-2:
                    sameWordStr += numStr[i+1]
                    sameWordArr.append(sameWordStr)
            else:
                if len(sameWordStr)>0:
                    sameWordStr += numStr[i]
                    sameWordArr.append(sameWordStr)
                    sameWordStr = ''
    # if haveSame:
    #     correctArr.append(num)
    haveDouble = False
    for data in sameWordArr:
        if len(data) == 2:
            haveDouble = True
    if haveDouble:
        correctArr.append(num)
    num += 1
finalArr = []
for checkNum in correctArr:
    numStr = str(checkNum)
    # 检查两边为三位数的情况
    # num1 = numStr[:3]
    # num2 = numStr[3:]
    # if num1[0] != '0' and num2[0]!='0':
    #     if num2>=num1:
    #         finalArr.append(checkNum)
    #         continue
    
    # 检查三个两位数的情况
    # num1 = numStr[:2]
    # num2 = numStr[2:4]
    # num3 = numStr[4:6]
    # if num1[0] != '0' and num2[0]!='0' and num3[0]!='0':
    #     if num3>=num2 and num2>=num1:
    #         finalArr.append(checkNum)
    #         continue
    # 检查全部都是1位数的情况
    num1 = numStr[:1]
    num2 = numStr[1:2]
    num3 = numStr[2:3]
    num4 = numStr[3:4]
    num5 = numStr[4:5]
    num6 = numStr[5:6]
    if num6>=num5 and num5>=num4 and num4>=num3 and num3>=num2 and num2>=num1:
        finalArr.append(checkNum)
        continue
    # 检查1位数+2位数+3位数的情况
    # num1 = numStr[:1]
    # num2 = numStr[1:3]
    # num3 = numStr[3:6]
    # if num3[0] != '0' and num2[0]!='0':
    #     finalArr.append(checkNum)
    #     continue
print(len(finalArr))