class DNDClass:
    def __init__(self, n, r, c, b, stat1, stat2, stat3, stat4, stat5 ,stat6):
        self.name = n
        self.race = r
        self.chacla = c
        self.background = b
        self.stat1 = stat1
        self.stat2=stat2
        self.stat3=stat3
        self.stat4=stat4
        self.stat5=stat5
        self.stat6=stat6
        self.skilllist=[]

    def introd(self):
        return("%s, Lvl 1 %s %s" %(self.name, self.race, self.chacla))
            
    def addremoveit(self, x, l, nl):
        nl[x]=max(l)
        l.remove(max(l))

    def racemod(self, stl):
        if self.race == 'Tiefling':
            stl[5]=stl[5]+2
            stl[4]=stl[4]+1
        if self.race == 'Human':
            y=0
            for x in stl:
                stl[y]=stl[y]+1
                y=y+1
                    

    def calcstat2(self): #reference code [Str, Dex, Wis, Con, Int, Cha]
        stat2=[self.stat1,self.stat2,self.stat3,self.stat4, self.stat5,self.stat6]
        newstat=[0,0,0,0,0,0]
        if self.chacla=='Rogue': #Stat Prio [Dex, Con, Cha, Str, Int, Wis]
                self.addremoveit(1,stat2,newstat)
                self.addremoveit(3,stat2,newstat)
                self.addremoveit(5,stat2,newstat)
                self.addremoveit(0,stat2,newstat)
                self.addremoveit(4,stat2,newstat)
                self.addremoveit(2,stat2,newstat)
                self.racemod(newstat)
                return(newstat)
        if self.chacla=='Fighter': #Stat Prio [Str, Con, Dex, Cha, Wis, Int]
                self.addremoveit(0,stat2,newstat)
                self.addremoveit(3,stat2,newstat)
                self.addremoveit(1,stat2,newstat)
                self.addremoveit(5,stat2,newstat)
                self.addremoveit(2,stat2,newstat)
                self.addremoveit(4,stat2,newstat)
                self.racemod(newstat)
                return(newstat)

    def printstat(self, l):
        return("Str = %s\nDex = %s\nWis = %s\nCon = %s\nInt = %s\nCha = %s" %(l[0], l[1], l[2], l[3], l[4], l[5]))

    def backgcalc(self, c, Skillz):
        y = c
        print("Choose " + str(c) +" from "+ str(Skillz))
        while y > 0:
            skill=input("Pick 1(%s remaining)" %str(y))
            if skill in Skillz and skill not in self.skilllist:
                self.skilllist.append(skill)
                y=y-1
            else:
                print("Invalid Choice, Repick")

    def backg(self):
        RogueValidSkill=['Acrobatics', 'Athletics', 'Deception', 'Insight', 'Intimidation', 'Investigation', 'Perception', 'Persuasion', 'Sleight of Hand', 'Stealth']
        FighterValidSkill=['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Perception', 'Survival']
        if self.chacla=='Rogue':
            self.backgcalc(4, RogueValidSkill)
        if self.chacla=='Fighter':
            self.backgcalc(2, FighterValidSkill)
        return(self.skilllist)



c1 = DNDClass('Nowi', 'Tiefling', 'Rogue', 'Sage', 18, 16, 16, 15, 8, 8)
c2 = DNDClass('Zeph', 'Human', 'Fighter', 'Outlander', 18, 13, 17, 16, 18, 12)

print(c1.introd())
c1.calcstat2()
print(c1.printstat(c1.calcstat2()))
print(" ")
print(c2.introd())
c2.calcstat2()
print(c2.printstat(c2.calcstat2()))
#c1.backg()

