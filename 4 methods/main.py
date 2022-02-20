class Hero:
    # Class variable
    jumlah = 0

    def __init__(self,inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1

    # void function, method tanpa return, tanpa argumen
    def siapa(self):
        print('namaku adalah ' + self.name)

    # method dengan argumen, tanpa return
    def healthUP(self,up):
        self.health += up

    def healthDown(self, DW):
        self.health -= DW
    
    # method dengan return
    def getHealth(self):
        return self.health


hero1 = Hero('alucard', 100, 20, 5)
hero2 = Hero('bruno', 200, 50, 0)

hero1.siapa()


hero1.healthUP(10) # tambah darah
print(hero1.health)
print(hero1.getHealth())

hero1.healthDown(80) # mengurangi darah
print(hero1.health)
print(hero1.getHealth())

