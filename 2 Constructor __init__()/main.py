class Hero: # Template
    def __init__(self, inputName, inputHealth, inputPower, inputArmor):
        self.name = inputName
        self.health = inputHealth
        self.power = inputPower
        self.armor = inputArmor


Hero1 = Hero("Alucard", 100, 90, 5)
Hero2 = Hero("Bruno", 300, 15, 10)
Hero3 = Hero("Gatot", 1000, 200, 0)

print(Hero1)
print(Hero1.__dict__)
print(Hero1.name)

print(Hero2)
print(Hero2.__dict__)
print(Hero2.health)

print(Hero3)
print(Hero3.__dict__)
print(Hero3.armor)