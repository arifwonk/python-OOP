class Hero: # Template
    jumlah = 0
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        # instance variables
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor
        Hero.jumlah += 1
        print("Membuat hero dengan nama " + inputName, Hero.jumlah)


hero1 = Hero("Alucard", 100, 90, 5)
print(Hero.jumlah)
hero2 = Hero("Bruno", 300, 15, 10)
print(Hero.jumlah)
hero3 = Hero("Gatot", 1000, 200, 0)
print(Hero.jumlah)



