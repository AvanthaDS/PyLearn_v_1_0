__author__ = 'Avantha'

class Parent():
    def print_last_name(self):
        print('De Silva')

class Child(Parent):

    def print_first_name(self):
        print('Avantha')

    def print_last_name(self): # THis overrides the inherited variable information, if it is not for this my second name will appear as avantha de silva'
        print('Pilippu Heva')

avantha = Child()
avantha.print_first_name()
avantha.print_last_name()

