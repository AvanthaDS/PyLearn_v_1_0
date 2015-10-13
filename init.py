__author__ = 'Avantha'
class Tuna:
    def __init__(self):
        print('This is Tuna')
    def swim(self):
        print('i am the best')

flipper = Tuna()
flipper.swim()

class Enemy:
    def __init__(self, x):
        self.energy = x

    def get_energy(self):
        print(self.energy)

jason = Enemy(5)
sandy = Enemy(18)

jason.get_energy()
sandy.get_energy()