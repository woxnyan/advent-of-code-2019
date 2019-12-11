class MapPositin(object):
    x = 0
    y = 0
    is_asteroid = False
    def __init__(_self,x,y,is_asteroid):
        _self.is_asteroid = is_asteroid
        _self.x = x
        _self.y = y

allPosition = []
with open('./day10.txt','r', encoding = 'utf-8') as f:
    for index,line in enumerate(f):
        for i in range(len(line)):
            if line[i] == '\n':
                continue
            mapPositin = None
            if line[i] == '.':
                mapPositin = MapPositin(i,index,False)
            else:
                mapPositin = MapPositin(i,index,True)
            allPosition.append(mapPositin)

seeAsteroid = {}
seeAsteroidRepeat = {}
for position in allPosition:
    if not position.is_asteroid:
        continue
    seeAsteroid[position] = []
    seeAsteroidRepeat[position] = {}

def issame(ax,ay,bx,by,cx,cy):
    kac = 0
    if cx-ax == 0:
        if cy>=ay:
            kac = -9999999999
        else:
            kac = 9999999999
    elif cy-ay == 0:
        if cx>=ax:
            kac = 0
        else:
            kac = -0.0000000001
    else:
        kac=(cy-ay)/(cx-ax)
    
    kab = 0
    if bx-ax == 0:
        if by>=ay:
            kab = 9999999999
        else:
            kab = -9999999999
    elif by-ay == 0:
        if bx>=ax:
            kab = 0
        else:
            kab = -0.0000000001
    else:
        kab=(by-ay)/(bx-ax)
    return kac==kab,kac

for position in allPosition:
    if not position.is_asteroid:
        continue
    for positionCheck in allPosition:
        if position == positionCheck or  not positionCheck.is_asteroid:
            continue
        positionSeeAsteroid = seeAsteroid[position]
        canAdd = True
        for comparePosition in allPosition:
            if position == comparePosition or comparePosition == positionCheck or not comparePosition.is_asteroid:
                continue
            checkResult,k = issame(position.x,position.y,positionCheck.x,positionCheck.y,comparePosition.x,comparePosition.y)
            if checkResult:
                canAdd = False
                if k in seeAsteroidRepeat[position]:
                    if comparePosition not in seeAsteroidRepeat[position][k]:
                        seeAsteroidRepeat[position][k].append(comparePosition)
                    if positionCheck not in seeAsteroidRepeat[position][k]:
                        seeAsteroidRepeat[position][k].append(positionCheck)
                else:
                    seeAsteroidRepeat[position][k] = []
                    seeAsteroidRepeat[position][k].append(comparePosition)
                    seeAsteroidRepeat[position][k].append(positionCheck)
                break
            
        if canAdd:
            positionSeeAsteroid.append(positionCheck)

maxPoint = None
maxNum = 0
for i in seeAsteroid:
    sumSame=0
    for k in seeAsteroidRepeat[i]:
        x1=0
        x2=0
        y1=0
        y2=0
        x01=0
        x02=0
        y01=0
        y02=0
        for j in seeAsteroidRepeat[i][k]:
            if j.x>i.x:
                x1 = 1
            elif j.x<i.x:
                x2 = 1
            elif j.y>i.y:
                y1=1
            elif j.y<i.y:
                y2=1
            elif j.x == i.x:
                if j.y>i.y:
                    x01 = 1
                else:
                    x02 = 1
            elif j.y == i.y:
                if j.x>i.x:
                    y01 = 1
                else:
                    y02 = 1
        sumSame += x1+x2+y1+y2+x01+x02+y01+y02
    if len(seeAsteroid[i]) + sumSame>maxNum:
        maxNum = len(seeAsteroid[i])+ sumSame
        maxPoint= i
    if i.x==5 and i.y==8:
        print(len(seeAsteroid[i]) + sumSame)
        
        
            