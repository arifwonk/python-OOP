class Hero: # Template
    pass


Hero1 = Hero() # Object atau instance (instansiate)
Hero2 = Hero()
Hero3 = Hero()

Hero1.name = "alucard"
Hero1.health = 100

Hero2.name = "bruno"
Hero2.health = 200

Hero3.name = "gatot"
Hero3.health = 300

print(Hero1)
print(Hero1.__dict__)
print(Hero1.name)

print(Hero2)
print(Hero2.__dict__)
print(Hero2.name)