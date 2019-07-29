class nick(object):

    nickcounter = 1

    def __init__(self,ethnicity, gender, age, surname):
        self.ethnicity = ethnicity
        self.gender = gender
        self.age = age
        self.surname = surname
        self.nicknum = nick.nickcounter
        nick.nickcounter += 1
        self.strength = None
        self.intel = None
        self.levelpoints = 10

    def get_nicknum(self):
        return str(self.nicknum) .zfill(3)

    def set_strength(self):
        self.strength = random.randint(1,100)

    def set_intel(self):
        self.intel = random.random() * 5

    def __str__(self):
        return "Nick "+str(self.surname)+" is "+str(self.ethnicity)+", "+str(self.gender)+" and is "+str(self.age)+" years old, with strength " + str(self.strength) + " and intelligence " + str(self.intel)

    def fuse(self,othernick):
        if self.ethnicity == othernick.ethnicity:
                self.ethnicity = self.ethnicity
        else:
            self.ethnicity = self.ethnicity +"-"+othernick.ethnicity
        self.age = (self.age + othernick.age)/2
        if self.gender == othernick.gender:
                self.gender = self.gender
        else:
            self.gender = "hermaphrodite"
        self.surname = self.surname+"-"+othernick.surname
        self.strength = self.strength + othernick.strength
        self.intel = self.intel * othernick.intel
        return self

    def hitthegym(self):
        self.levelpoints -= 1
        add = random.randint(1,10)
        self.strength += add

    def hitthelib(self):
        self.levelpoints -=2
        add = random.random() + random.randint(1,3)
        self.intel *= add

def newnick():
    newnickethnicity = input("nick number "+str(nick.nickcounter)+"'s ethnicity: ")
    newnickgender = input("nick number "+str(nick.nickcounter)+"'s  gender: ")
    newnickage = int(input(" nick number "+str(nick.nickcounter)+"'s age: "))
    newnicksurname = input(" nick number "+str(nick.nickcounter)+"'s surname: ")
    nick1 = nick(newnickethnicity, newnickgender, newnickage, newnicksurname)
    return nick1

def yesorno():
    query = input("yes or no: ")
    if query == "yes":
        return 1

def gotogym():
    print("would you like to hit the gym?")
    if yesorno() == 1:
        print("this is your original strength: " + str(nick001.strength))
        time.sleep(1.3)
        nick.hitthegym(nick001)
        print("this is your new strength: " + str(nick001.strength))
        return
    else:
        return

def gotolib():
    print("would you like to chill at the library?")
    if yesorno() == 1:
        print("this is your original intelligence: " + str(nick001.intel))
        time.sleep(1.3)
        nick.hitthelib(nick001)
        print("this is your new intelligence: " + str(nick001.intel))
        return
    else:
        return

def cave():
    print("you are walking along in the cave, and come across an intersection: ")
    print("")
    response = input("left or right?: ")
    if response == "left":
        caveleft()
    elif response == "right":
        caveright()
    print("now that you have completed the cave, you can enter the maze. Do you wish to enter the maze?")
    print("")
    if yesorno() == 0:
        return
    else:
        maze()


def caveleft():
    print("you find a strong wooden chest. Try and open it?")
    print("")
    response = input("yes or no?: ")
    if response == "yes":
        if nick001.strength > 75:
            print("you smash open the chest, revealing an ancient tome and the sterling greatsword")
            nick001.strength += 10
            nick001.intel *= 1.5
            time.sleep(1)
            print("with the new weapon and knowledge, your new strength is: " + str(nick001.strength))
            print(" and your new intelligence is: " + str(nick001.intel))
            print("")
        elif 75>= nick001.strength > 40:
            print("you hit the chest hard, creating a gap wide enough to look inside.")
            print("you see a book and sword, but can only get the book")
            time.sleep(1)
            print("you learned some knowledge, but hurt your hand.")
            nick001.strength -= 5
            nick001.intel *= 1.5
            print("with your hurt hand and new knowledge, your new strength is: " + str(nick001.strength))
            print(" and your new intelligence is: " + str(nick001.intel))
        else:
            print("you weakly punch the chest, breaking a finger and crying a little")
            time.sleep(1)
            nick001.strength -= 4
            print("you slink off, and your strength decreases 4 points, now: " + str(nick001.strength))
        time.sleep(3)
        print("you then exit the cave")
        print("")
        return

def caveright():
    nick2age = random.randint(10,40)
    gendercoinflip = random.randint(1,2)
    if gendercoinflip == 1:
        nick2gender = "male"
    else:
        nick2gender = "female"
    nickcave = nick("jewish", nick2gender, nick2age, "Anderes")
    nickcave.set_strength()
    nickcave.set_intel()
    print("You meet a random stranger. Their name is Nick as well")
    print("")
    time.sleep(3)
    print(nickcave)
    time.sleep(2)
    print("They sees you are questing, and challenges you to an arm wrestle. Do you accept?")
    print("")
    if yesorno() == 1:
        if nickcave.strength > nick001.strength:
            print("you were overpowered")
            nick001.strength += 10
            time.sleep(2)
            print("you gained 10 strength for good effort")
        else:
            print("you best Nick in the arm wrestle. For winning, they offer to fuse with you so you can gain their attributes")
            response = input("do you accept?: ")
            if response == "yes":
                nick.fuse(nick001, nickcave)
                print("fusing...")
                time.sleep(5)
                print("your traveler info is now: ")
                print(nick001)
            else:
                return
    print("your new strength and intelligence are: " + str(nick001.strength) +" and "+ str(nick001.intel))
    print("")
    print("you can exit the cave, or go to the left wing you skipped")
    response = input("exit or left?: ")
    if response == "left":
        caveleft()
    else:
        return

def bossbattle(ip, np, o):
    print("Nick Cage hulks above you, wearing a thick armor. You realize you must remove his armor before")
    print("being able to injure him")
    time.sleep(3)
    print("you see a grappling hook on the ground that a past traveler dropped")
    print("")
    cagearmor = ["shoulder", "chest"]
    for i in range(3):
        print("you can grapple his shoulder armor, or his chest armor")
        response = input("shoulder or chest?")
        if response == "shoulder":
            rand = random.randint(1,3)
            print("you receive a " + str(rand * (i +1)) + "x multiplier!")
            if ip * rand * (i + 1) > 25:
                print("you knock off his shoulder armor")
                cagearmor.remove("shoulder")
            else:
                print("your intelligence value was too low and you fail to remove any armor, and your hook has " + str(2 - i) + " uses left")
        if response == "chest":
            if "shoulder" in cagearmor:
                print("you couldn't remove his chest armor because his shoulder armor was still attached")
            else:
                print("since his shoulder armor is gone, you can grapple his chest armor")
                if ip > np:
                    print("you pull off his chest armor, leaving him exposed for a physical attack")
                    cagearmor.remove("chest")
                    finishcage(cagearmor, nick001.strength, o)
                    return
                else:
                    print("your intelligence was not high enough to remove his chestplate")
def finishcage(list, strengt, other):
    time.sleep(3)
    if list != []:
        print("you failed to remove his armor. with no other way to defeat him, Nick Cage pummels you into the dust")
        return
    else:
        print("You remove his armor, exposing his chest for a final blow")
        print("")
        time.sleep(3)
        print("you wind up, and smash him into oblivion with " + str(strengt) + " strength!!")
        print("his spirit lingers, though, and glows. You can feel it pull closer, and it fuses into you")
        nick.fuse(nick001,other)
        print("after defeating Nick Cage, you reign supreme as the most powerful Nick to ever exist.")
        return



def maze():
    print("")
    print("You enter the maze. It winds around, and you follow the reasonable path")
    time.sleep(3)
    print("You come across a locked door. On the door is a six pointed star with a toggle in the middle.")
    time.sleep(2)
    print("the toggle goes up, down, right and left")
    print("you must move the toggle in some pattern to open the door")
    print("")
    t = 0
    while t != 6:
        tog = input ("left, right, up or down? ")
        if tog == "left":
            t += 2.5
            print("you hear a large click")
        if tog == "right":
            t += 1.5
            print("you hear a medium click")
        if tog == "up":
            t -= .5
            print("the lock unclicks a halfclick")
        if tog == "down":
            t =0
            print("the lock jams and resets")
    print("unlocking...")
    time.sleep(5)
    print("you continue into the maze, coming closer and closer to the end")
    time.sleep (3)
    print("the cave grows dim, with light flickering around")
    time.sleep(3)
    print("you hear a roar! continue?")
    if yesorno() != 1:
        return
    else:
        print("you approach the roar, and enter a large, open room.")
        time.sleep(2)
        print("you see a figure... could that be...?")
        time.sleep(3)
        print("it's NICK CAGE! The ultimate boss!")
        time.sleep(3)
        nickcage = nick("northern european", "male", 55, "Cage")
        nickcage.strength = 100
        nickcage.intel = 25
        print(nickcage)
        time.sleep(3)
        print("")
        print("you have no choice but to fight. BOSS BATTLE!")
        time.sleep(3)
        bossbattle(nick001.intel, nickcage.intel, nickcage)


import random
import time
print("This game was created by Sam Raphaelson on Sunday, July 28th, 2019. with love")
print("Hello there! Welcome to the world of Nicks.")
time.sleep(2)
print("")
print("To begin, make a new nick! This will be your adventurer for this quest to become the most powerful nick!")
nick001 = newnick()
nick001.set_strength()
nick001.set_intel()
print("you have " + str(nick001.levelpoints) + " level points -- whenever you increase an attribute, you spend 1 level point")
time.sleep(2)
print("what would you like to do? you can hit the gym, or chill at the library (hint: you have to spend 6 points)")
while nick001.levelpoints >= 4:
    print("level points: " + str(nick001.levelpoints))
    response = input("gym or library: ")
    if response == "gym":
        gotogym()
    elif response == "library":
        gotolib()
time.sleep(1)
print("now that you have strengthened your body and mind, you can go quest")
time.sleep(1.3)
print("you can explore a brawler's cave or a puzzle maze")
response = input("cave or maze?: ")
if response == "cave":
    cave()
elif response == "maze":
    maze()
time.sleep(5)
print("here are your adventurer's final stats: ")
print(nick001)