class superhero:
    def introduce(self):
        print(f'i am {self.name},and my power is {self.power}!')
hero1 = superhero()
hero1.name = 'goku'
hero1.power = 'super saiyan'

hero2 = superhero()
hero2.name = 'naruto'
hero2.power = '9 tails'

hero3 = superhero()
hero3.name = 'luffy'
hero3.power = 'imagination'

hero1.introduce()
hero2.introduce()
hero3.introduce()