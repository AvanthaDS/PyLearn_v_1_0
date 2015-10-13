__author__ = 'Avantha'
class Enemy: # this function works and a template to be used in the following objects enemy1 and enemy 2
    life = 3

    def attack(self):
        print('outch !')
        self.life -= 1
    def checklife(self):
        if self.life<=0:
            print('I am fucked up')
        else:
            print(str(self.life)+ ' life left')

enemy1 = Enemy() # here the enemy1 is an object
enemy2 = Enemy()
enemy1.attack()
enemy1.attack()
enemy1.checklife()
enemy2.checklife()