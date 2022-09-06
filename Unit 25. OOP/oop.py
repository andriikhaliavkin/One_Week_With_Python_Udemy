#object oriented programming

class Character:
    def __init__(self, name, hp, level):
        self.name = name
        self.hp = hp
        self.level = level

    def run(self):
        print('run')

    def show_info(self):
        print('{} level {} HP {}'.format(self.name, self.level, self.hp))

    def fight(self, skill):
        print('use a skill {}'.format(skill))


wizzard = Character('Merlin', 50, 12)
wizzard.show_info()
wizzard.fight('fireball')


warrior = Character('Conan', 75, 7)
warrior.show_info()

wizzard.run()
warrior.run()

wizzard.name = 'Gandalf'
wizzard.show_info()





