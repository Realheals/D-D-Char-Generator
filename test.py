import random #D&D stat gen WIP
attrlis=[]
for y in range(0,6):
    numlis=[]
    for x in range(0,4):
        numlis.append(random.randrange(1,7))
    numlis.remove(min(numlis))
    attrlis.append(sum(numlis))
print(attrlis)
