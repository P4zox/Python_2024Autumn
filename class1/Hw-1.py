import random as r

class RPG:
    def __init__(self, name, health, bossHealth, weapon, skillname, skilldg):
        self.name=name
        self.health=health
        self.bossHealth=bossHealth
        self.atk=weapon
        self.bskill=skillname
        self.bskilln=skilldg
    def hurt(self):
        self.health= self.health - self.bskilln
    
    def bossHurt(self):
        self.bossHealth=self.bossHealth-self.atk

    def death(self):
        print("you die")
    
    def win(self):
        print("{} win".format(game.name))
    

    def changeSkill(self):
        s=[10,25,5,self.atk*2]
        s2=["punch","slash","stomp","stab"]
        rand=r.randrange(0,4)
        self.bskilln=s[rand]
        self.bskill=s2[rand]    


def ask():
    q=input("Type y to attack and n to dodge: ")
    if q == "y":
        game.bossHurt()
        game.changeSkill()
        print("you make {} damage to the swordman, swordman hp: {}".format(game.atk, game.bossHealth))
        game.hurt()
        print("the swordman attack you with {}, which give you {} dmg\nyour health is now {}".format(game.bskill,game.bskilln,game.health))
    if q == "n":
        print("you dodge the attack")


game=RPG(input("name: "),int(input("health: ")), int(input("bossHealth: ")), int(input("atk: ")), "punch", 10)

print("you encounter a swordman, which have {} of hp max".format(game.bossHealth))


while True:
    ask()
    if game.health <= 0:
        game.death()
        break
    elif game.bossHealth <= 0:
        game.win()
        break