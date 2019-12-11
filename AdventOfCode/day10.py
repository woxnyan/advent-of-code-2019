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
  kac=(ax-cx)*(cy-by)
  kbc=(cx-bx)*(ay-cy)   
  return kac==kbc,kac

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
                seeAsteroidRepeat[position][k] = 0
                break
            
        if canAdd:
            positionSeeAsteroid.append(positionCheck)

maxPoint = None
maxNum = 0
for i in seeAsteroid:
    if len(seeAsteroid[i]) + len(seeAsteroidRepeat[i])>maxNum:
        maxNum = len(seeAsteroid[i])+ len(seeAsteroidRepeat[i])
        maxPoint= i
    if i.x==5 and i.y==8:
        print(len(seeAsteroid[i]) + len(seeAsteroidRepeat[i]))
        

print(maxNum)
print(maxPoint.x)
print(maxPoint.y)
        
        
            