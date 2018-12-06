import random #D&D char gen WIP

class DNDClass:
    def __init__(self, n):
        self.name = n
        self.background = ''
        self.statl = []
        self.skilllist=[]
        self.hp=0
        self.ac=0
        self.inti=0
        self.specialhealthmod=0
        self.mods=[]

    def introd(self):
        return("%s, Lvl 1 %s %s %s \nHP=%s AC=%s Intitative=%s" %(self.name, self.race, self.chacla, self.background, self.hp, self.ac, self.inti))
            
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
        elif self.race == 'Mountain Dwarf':#+2 Con +2 Str
            stl[0]=stl[0]+2
            stl[3]=stl[3]+2
        elif self.race== 'High Elf':#+2 Dex +1 Int
            stl[4]=stl[4]+1
            stl[1]=stl[1]+2
        elif self.race== 'Wood Elf':#+2 Dex +1 Wis
            stl[2]=stl[2]+1
            stl[1]=stl[1]+2
        elif self.race== 'Drow Elf':#+2 Dex +1 Cha
            stl[5]=stl[5]+1
            stl[1]=stl[1]+2
        elif self.race== 'Lightfoot Halfling':#+2 Dex +1 Cha
            stl[5]=stl[5]+1
            stl[1]=stl[1]+2
        elif self.race== 'Stout Halfling':#+2 Dex +1 Con
            stl[3]=stl[3]+1
            stl[1]=stl[1]+2
        elif self.race== 'Dragonborn':#+2 Str +1 Cha
            stl[5]=stl[5]+1
            stl[0]=stl[0]+2
        elif self.race== 'Forest Gnome':#+2 Int +1 Dex
            stl[1]=stl[1]+1
            stl[4]=stl[4]+2
        elif self.race== 'Rock Gnome':#+2 Int +1 Con
            stl[3]=stl[3]+1
            stl[4]=stl[4]+2
        elif self.race== 'Half Elf':#+2 Cha +1? + 1?
            stl[5]=stl[5]+2
            untildis=0
            nono=0
            while untildis != 2:
                pee=random.randrange(1,4)
                if pee !=nono:
                    stl[pee]=stl[pee]+1
                    print(pee)
                    nono=pee
                    untildis=untildis+1
        elif self.race=='Half Orc':#+2 Str +1 Con
            stl[3]=stl[3]+1
            stl[0]=stl[0]+2
    def addremovepart2(self, st1, st2, st3, st4, st5, st6):
        stat2=self.statl
        newstat=[0,0,0,0,0,0]
        self.addremoveit(st1,stat2,newstat)
        self.addremoveit(st2,stat2,newstat)
        self.addremoveit(st3,stat2,newstat)
        self.addremoveit(st4,stat2,newstat)
        self.addremoveit(st5,stat2,newstat)
        self.addremoveit(st6,stat2,newstat)
        self.racemod(newstat)
        self.statl=newstat
                    

    def calcstat2(self): #reference code [Str, Dex, Wis, Con, Int, Cha]
        stat2=self.statl
        newstat=[0,0,0,0,0,0]
        if self.chacla=='Rogue': #Stat Prio [Dex, Con, Cha, Str, Int, Wis]
                self.addremovepart2(1,3,5,0,4,2)
        elif self.chacla=='Fighter' or self.chacla=='Barbarian' or self.chacla=='Paladin': #Stat Prio [Str, Con, Dex, Cha, Wis, Int]
                self.addremovepart2(0,3,1,5,2,4)
        elif self.chacla=='Bard' or self.chacla=='Sorcerer' or self.chacla=='Warlock': #Stat Prio [Cha, Con, Dex, Int, Str, Wis]
                self.addremovepart2(5,3,1,4,0,2)
        elif self.chacla=='Cleric' or self.chacla=='Druid': #Stat Prio [Wis, Con, Dex, Cha, Str, Int] #reference code [Str(0), Dex(1), Wis(2), Con(3), Int(4), Cha(5)]
                self.addremovepart2(2,3,1,5,0,4)
        elif self.chacla=='Monk' or self.chacla=='Ranger': #Stat Prio [Dex, Wis, Con, Str, Int, Cha]
                self.addremovepart2(1,2,3,0,4,5)
        elif self.chacla=='Wizard': #Stat Prio [Int, Con, Dex, Str, Wis, Cha]
                self.addremovepart2(4,3,1,0,2,5)
                

    def printstat(self, l):
        return("Str = %s\nDex = %s\nWis = %s\nCon = %s\nInt = %s\nCha = %s" %(l[0], l[1], l[2], l[3], l[4], l[5]))


    def getstats(self):
        attrlis=[]
        for y in range(0,6):
            numlis=[]
            for x in range(0,4):
                numlis.append(random.randrange(1,7))
            numlis.remove(min(numlis))
            attrlis.append(sum(numlis))
        self.statl=attrlis

    def classdice(self):
        if self.chacla=='Wizard' or self.chacla=='Sorcerer':
            self.hitdie=6
        elif self.chacla=='Bard' or self.chacla=='Cleric' or self.chacla=='Druid' or self.chacla=='Monk' or self.chacla=='Rogue' or self.chacla=='Warlock':
            self.hitdie=8
        elif self.chacla=='Fighter' or self.chacla=='Paladin' or self.chacla=='Ranger':
            self.hitdie=10
        elif self.chacla=='Barbarian':
            self.hitdie=12
    


    def randoBG(self):
        choicelist=['Outlander','Sage', 'Acolyte', 'Charlatan', 'Criminal', 'Entertainer', 'Folk Hero', 'Guild Artisan', 'Hermit', 'Noble', 'Sailor', 'Soldier', 'Urchin']
        x= random.randrange(0,13)
        self.background = choicelist[x]
        if self.background == 'Sage':
            self.skilllist.append('Arcana')
            self.skilllist.append('History')
        elif self.background == 'Outlander':
            self.skilllist.append('Athletics')
            self.skilllist.append('Survival')
        elif self.background == 'Acolyte':
            self.skilllist.append('Religion')
            self.skilllist.append('Insight')
        elif self.background == 'Charlatan':
            self.skilllist.append('Deception')
            self.skilllist.append('Sleight of Hand')
        elif self.background == 'Criminal':
            self.skilllist.append('Deception')
            self.skilllist.append('Stealth')
        elif self.background == 'Entertainer':
            self.skilllist.append('Acrobatics')
            self.skilllist.append('Performance')
        elif self.background == 'Folk Hero':
            self.skilllist.append('Animal Handling')
            self.skilllist.append('Survival')
        elif self.background == 'Guild Artisan':
            self.skilllist.append('Insight')
            self.skilllist.append('Persuasion')
        elif self.background == 'Hermit':
            self.skilllist.append('Medicine')
            self.skilllist.append('Religion')
        elif self.background == 'Noble':
            self.skilllist.append('History')
            self.skilllist.append('Persuasion')
        elif self.background == 'Sailor':
            self.skilllist.append('Athletics')
            self.skilllist.append('Perception')
        elif self.background == 'Soldier':
            self.skilllist.append('Athletics')
            self.skilllist.append('Intimidation')
        elif self.background == 'Urchin':
            self.skilllist.append('Sleight of Hand')
            self.skilllist.append('Stealth')
    def randoSkill(self):
        RogueValidSkill=['Acrobatics', 'Athletics', 'Deception', 'Insight', 'Intimidation', 'Investigation', 'Perception', 'Persuasion', 'Sleight of Hand', 'Stealth'] #4
        FighterValidSkill=['Acrobatics', 'Animal Handling', 'Athletics', 'History', 'Insight', 'Intimidation', 'Perception', 'Survival'] #2
        BarbValidSkill=['Animal Handling', 'Athletics', 'Intimidation', 'Nature', 'Perception', 'Survival'] #2
        BardValidSkill=['Acrobatics', 'Animal Handling','Arcana','Athletics','Deception','History','Insight','Intimidation','Investigation', 'Medicine', 'Nature','Perception','Performance','Persuasion','Religion','Sleight of Hand', 'Stealth', 'Survival'] #3
        ClericValidSkill=['History','Insight','Medicine','Persuasion','Religion'] #2
        DruidValidSkill=['Arcana','Animal Handling','Insight','Medicine','Nature','Perception','Religion','Survival']#2
        MonkValidSkill=['Acrobatics', 'Athletics','History','Insight','Religion','Stealth']#2
        PallyValidSkill=['Athletics','Insight','Intimidation','Medicine','Persuasion','Religion']#2
        RangerValidSkill=['Animal Handling','Athletics','Insight','Investigation','Nature','Perception','Stealth','Survival']#3
        SorcValidSkill=['Arcana','Deception','Insight','Intimidation','Persuasion','Religion']#2
        LockValidSkill=['Arcana','Deception','History','Intimidation','Investigation','Nature','Religion']#2
        WizValidSkill=['Arcana','History','Insight','Intimidation','Investigation','Medicine','Religion']#2
        if self.chacla=='Rogue':
            self.mathrandoSkill(4, RogueValidSkill)
        elif self.chacla=='Fighter':
            self.mathrandoSkill(2, FighterValidSkill)
        elif self.chacla=='Barbarian':
            self.mathrandoSkill(2, BarbValidSkill)
        elif self.chacla=='Bard':
            self.mathrandoSkill(3, BardValidSkill)
        elif self.chacla=='Cleric':
            self.mathrandoSkill(2, ClericValidSkill)
        elif self.chacla=='Druid':
            self.mathrandoSkill(2, DruidValidSkill)
        elif self.chacla=='Monk':
            self.mathrandoSkill(2, MonkValidSkill)
        elif self.chacla=='Paladin':
            self.mathrandoSkill(2, PallyValidSkill)
        elif self.chacla=='Ranger':
            self.mathrandoSkill(3, RangerValidSkill)
        elif self.chacla=='Sorcerer':
            self.mathrandoSkill(2, SorcValidSkill)
        elif self.chacla=='Warlock':
            self.mathrandoSkill(2, LockValidSkill)
        elif self.chacla=='Wizard':
            self.mathrandoSkill(2, WizValidSkill)

    def mathrandoSkill(self, amount, skillzee):
        t=[]
        #print(self.skilllist[0])
        if self.skilllist[0] in skillzee:
            #print("t")
            t.append(skillzee.index(self.skilllist[0]))
        if self.skilllist[1] in skillzee:
            #print("t")
            t.append(skillzee.index(self.skilllist[1]))
        x = 0
        while x !=amount:
            l = random.randrange(0, len(skillzee))
            if l not in t:
                self.skilllist.append(skillzee[l])
                t.append(l)
                x=x+1
                
            
    def pickClass(self):
        classList=['Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk', 'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
        #classList=['Rogue', 'Fighter']
        x= random.randrange(0,12)
        #print(x)
        self.chacla=classList[x]

    def pickRace(self):
        raceList=['Human', 'Tiefling', 'Hill Dwarf', 'Half Elf', 'Half Orc', 'Mountain Dwarf', 'High Elf', 'Wood Elf', 'Drow Elf', 'Lightfoot Halfling', 'Stout Halfling', 'Dragonborn', 'Forest Gnome','Rock Gnome']
        x= random.randrange(0,14)
        #print(x)
        self.race=raceList[x]

    def healthACinti(self):
        self.hp=self.hitdie+self.mods[3]+self.specialhealthmod
        self.inti=self.mods[1]

    def getMod(self):
        for x in range(0, 6):
            if self.statl[x]==1:
                self.mods.append(-5)
            elif self.statl[x]==2 or self.statl[x]==3:
                self.mods.append(-4)
            elif self.statl[x]==4 or self.statl[x]==5:
                self.mods.append(-3)
            elif self.statl[x]==6 or self.statl[x]==7:
                self.mods.append(-2)
            elif self.statl[x]==8 or self.statl[x]==9:
                self.mods.append(-1)
            elif self.statl[x]==10 or self.statl[x]==11:
                self.mods.append(0)
            elif self.statl[x]==12 or self.statl[x]==13:
                self.mods.append(1)
            elif self.statl[x]==14 or self.statl[x]==15:
                self.mods.append(2)
            elif self.statl[x]==16 or self.statl[x]==17:
                self.mods.append(3)
            elif self.statl[x]==18 or self.statl[x]==19:
                self.mods.append(4)
            elif self.statl[x]==18 or self.statl[x]==19:
                self.mods.append(4)
            elif self.statl[x]==20:
                self.mods.append(5)

c3 = DNDClass('Zeph')
c4 = DNDClass('Nowi')
c3.randoBG()
c4.randoBG()
c3.pickClass()
c4.pickClass()
c4.classdice()
c3.pickRace()
c4.pickRace()
c4.getstats()
print(c4.statl)
c4.calcstat2()
c4.getMod()
c4.randoSkill()
c4.healthACinti()
print(c4.introd())
print(c4.printstat(c4.statl))
print("Skilllist: " + ", ".join(c4.skilllist))
