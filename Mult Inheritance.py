__author__ = 'Avantha'
class Mario():
    def move(self):
        print('move around')

class Shroom():
    def eat_shroom(self):
        print('now I am big')

class BigMario(Mario,Shroom):
    pass

bm = BigMario()
bm.move()
bm.eat_shroom()
