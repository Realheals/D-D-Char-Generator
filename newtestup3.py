import random #D&D char gen WIP

class DNDClass:
    def __init__(self, n, b):
        self.name = n
        self.background = b
        self.statl = []
        self.skilllist=[]
        self.specialhealthmod=0

    def introd(self):
        return("%s, Lvl 1 %s %s %s" %(self.name, self.race, self.chacla, self.background))
            
    def addremoveit(self, x, l, nl):
        nl[x]=max(l)
        l.remove(max(l))

    def racemod(self, stl): #reference code [Str(0), Dex(1), Wis(2), Con(3), Int(4), Cha(5)]
        if self.race == 'Tiefling': #+2 Cha, +1 Int
            stl[5]=stl[5]+2
            stl[4]=stl[4]+1
        elif self.race == 'Human': #+1 All
            y=0
            for x in stl:
                stl[y]=stl[y]+1
                y=y+1
        elif self.race == 'Hill Dwarf':#+1 Wis +2 Con (Extra HP)
            stl[2]=stl[2]+1
            stl[3]=stl[3]+2
            self.specialhealthmod=+1 #REMEMBER TO ADD THIS TO HP SCORE
        #if self.race == '
        
                    

    def calcstat2(self): #reference code [Str, Dex, Wis, Con, Int, Cha]
        stat2=self.statl
        newstat=[0,0,0,0,0,0]
        do = self.addremoveit
        if self.chacla=='Rogue': #Stat Prio [Dex, Con, Cha, Str, Int, Wis]
                self.addremoveit(1,stat2,newstat)
                self.addremoveit(3,stat2,newstat)
                self.addremoveit(5,stat2,newstat)
                self.addremoveit(0,stat2,newstat)
                self.addremoveit(4,stat2,newstat)
                self.addremoveit(2,stat2,newstat)
                self.racemod(newstat)
                self.statl=newstat
        elif self.chacla=='Fighter' or self.chacla=='Barbarian' or self.chacla=='Paladin': #Stat Prio [Str, Con, Dex, Cha, Wis, Int]
                self.addremoveit(0,stat2,newstat)
                self.addremoveit(3,stat2,newstat)
                self.addremoveit(1,stat2,newstat)
                self.addremoveit(5,stat2,newstat)
                self.addremoveit(2,stat2,newstat)
                self.addremoveit(4,stat2,newstat)
                self.racemod(newstat)
                self.statl=newstat
        elif self.chacla=='Bard' or self.chacla=='Sorcerer' or self.chacla=='Warlock': #Stat Prio [Cha, Con, Dex, Int, Str, Wis]
                self.addremoveit(5,stat2,newstat)
                self.addremoveit(3,stat2,newstat)
                self.addremoveit(1,stat2,newstat)
                self.addremoveit(4,stat2,newstat)
                self.addremoveit(0,stat2,newstat)
                self.addremoveit(2,stat2,newstat)
                self.racemod(newstat)
                self.statl=newstat
        elif self.chacla=='Cleric' or self.chacla=='Druid': #Stat Prio [Wis, Con, Dex, Cha, Str, Int] #reference code [Str(0), Dex(1), Wis(2), Con(3), Int(4), Cha(5)]
                self.addremoveit(2,stat2,newstat)
                self.addremoveit(3,stat2,newstat)
                self.addremoveit(1,stat2,newstat)
                self.addremoveit(5,stat2,newstat)
                self.addremoveit(0,stat2,newstat)
                self.addremoveit(4,stat2,newstat)
                self.racemod(newstat)
                self.statl=newstat
        elif self.chacla=='Monk' or self.chacla=='Ranger': #Stat Prio [Dex, Wis, Con, Str, Int, Cha]
                self.addremoveit(1,stat2,newstat)
                self.addremoveit(2,stat2,newstat)
                self.addremoveit(3,stat2,newstat)
                self.addremoveit(0,stat2,newstat)
                self.addremoveit(4,stat2,newstat)
                self.addremoveit(5,stat2,newstat)
                self.racemod(newstat)
                self.statl=newstat
        elif self.chacla=='Wizard': #Stat Prio [Int, Con, Dex, Str, Wis, Cha]
                self.addremoveit(4,stat2,newstat)
                self.addremoveit(3,stat2,newstat)
                self.addremoveit(1,stat2,newstat)
                self.addremoveit(0,stat2,newstat)
                self.addremoveit(2,stat2,newstat)
                self.addremoveit(5,stat2,newstat)
                self.racemod(newstat)
                self.statl=newstat       
                

    def printstat(self, l):
        return("Str = %s\nDex = %s\nWis = %s\nCon = %s\nInt = %s\nCha = %s" %(l[0], l[1], l[2], l[3], l[4], l[5]))

    def backgcalc(self, c, Skillz): #OLD CODE DISCONTINUED
        y = c
        print("Choose " + str(c) +" from "+ str(Skillz))
        while y > 0:
            skill=input("Pick 1(%s remaining)" %str(y))
            if skill in Skillz and skill not in self.skilllist:
                self.skilllist.append(skill)
                y=y-1
            else:
                print("Invalid Choice, Repick")

    def backg(self): #OLD CODE DISCONTINUED
        RogueValidSkill=['Acrobatics', 'Athletics', 'Deception', 'Insight', 'Intimidation', 'Investigation', 'Perception', 'Persuasion', 'Sleight of Hand', 'Stealth']
        FighterValidSkill=['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Perception', 'Survival']
        BarbarianValidSkill=[] #Also do the rest of the classes + background skills
        if self.chacla=='Rogue':
            self.backgcalc(4, RogueValidSkill)
        elif self.chacla=='Fighter':
            self.backgcalc(2, FighterValidSkill)
        return(self.skilllist)

    def getstats(self):
        attrlis=[]
        for y in range(0,6):
            numlis=[]
            for x in range(0,4):
                numlis.append(random.randrange(1,7))
            numlis.remove(min(numlis))
            attrlis.append(sum(numlis))
        self.statl=attrlis

    def randoBG(self):
        choicelist=['Outlander','Sage']
        x= random.randrange(0,2)
        self.background = choicelist[x]

    def randoSkill(self):
        RogueValidSkill=['Acrobatics', 'Athletics', 'Deception', 'Insight', 'Intimidation', 'Investigation', 'Perception', 'Persuasion', 'Sleight of Hand', 'Stealth']
        FighterValidSkill=['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Perception', 'Survival']
        BarbarianValidSkill=[]

    def mathrandoSkill():
        Rge=10
        Fig=8

    def pickClass(self):
        classList=['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
        x= random.randrange(0,12)
        print(x)
        self.chacla=classList[x]

    def pickRace(self):
        raceList=['Human', 'Tiefling', 'Hill Dwarf']
        x= random.randrange(0,3)
        print(x)
        self.race=raceList[x]

c3 = DNDClass('Zeph', 'Outlander')
c4 = DNDClass('Nowi', 'Sage')
c3.randoBG()
c4.randoBG()
c3.pickClass()
c4.pickClass()
c3.pickRace()
c4.pickRace()
print(c4.introd())
c4.getstats()
print(c4.statl)
c4.calcstat2()
print(c4.printstat(c4.statl))
#c4.backg()

#print(c3.printstat(c3.calcstat2()))
#print(c1.introd())
#c1.calcstat2()
#print(c1.printstat(c1.calcstat2()))
#print(" ")
#print(c2.introd())
#c2.calcstat2()
#print(c2.printstat(c2.calcstat2()))
#c1.backg()

