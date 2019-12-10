orbitsMap = {}

class Oribit:
    name = ''
    preOribit = {}
    def __init__(self,name,oribit = None):
        self.name = name
        self.preOribit = oribit
with open('./day6.txt', 'r', encoding='utf-8') as f:
    for line in f:
        word = line.split(')')
        oribitsInner = word[0]
        oribitsOutter = word[1].replace('\n','')
        currentInnerOribit = {}
        currentOutterOribit = {}
        if oribitsInner in orbitsMap:
            currentInnerOribit = orbitsMap[oribitsInner]
        else:
            currentInnerOribit = Oribit(oribitsInner)
            orbitsMap[oribitsInner] = currentInnerOribit
        if oribitsOutter in orbitsMap:
            currentOutterOribit = orbitsMap[oribitsOutter]
            currentOutterOribit.preOribit = orbitsMap[oribitsInner]
        else:
            currentOutterOribit = Oribit(oribitsOutter)
            currentOutterOribit.preOribit = orbitsMap[oribitsInner]
            orbitsMap[oribitsOutter] = currentOutterOribit
sum = 0
def getOribCount(orbit):
    if orbit.preOribit != None:
        global sum
        sum+=1
        getOribCount(orbit.preOribit)

total = 0
for orbit in orbitsMap:
    sum = 0
    getOribCount(orbitsMap[orbit])
    total+= sum

youOrbit = orbitsMap['YOU']
sanOrbit = orbitsMap['SAN']
youArr = []
sanArr = []
def getOrbitArr(orbit,youArr):
    if orbit.preOribit != None:
        youArr.append(orbit.name)
        getOrbitArr(orbit.preOribit,youArr)
getOrbitArr(youOrbit,youArr)
getOrbitArr(sanOrbit,sanArr)
# for m in youArr:
#     for n in sanArr:
#         if m == n:
#             print(m)
#             break
youSum = 0
sanSum = 0
def getOrbitSum(orbit,youSum):
    if orbit.name != '5DV':
        youSum+=1
        getOrbitSum(orbit.preOribit,youSum)
    else:
        print(youSum)
getOrbitSum(youOrbit,youSum)
getOrbitSum(sanOrbit,sanSum)
