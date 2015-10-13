__author__ = 'Avantha'


# class Girls:
class Student:
    # gender ='male'

    nationality = 'Sri Lankan'  # This value will be inherited for all

    def __init__(self, name):
        self.name = name  # these are attributes these can be accessed outside the class
        self.attend = 0
        self.grades = []
        self.age = 'test coment'
        print('Hi my name is {0}'.format(self.name))  # , self.name would also work

    def addGrade(self, grade):
        self.grades.append(grade)

    def attenday(self):
        self.attend += 1

    def getAv(self):
        avg = sum(self.grades) / len(self.grades)
        return avg


student1 = Student('Avantha')
print(student1.nationality)
student1.age = 'xxx'
print(student1.age)
print(student1.attend)

for x in range(1, 11):
    student1.attenday()

student1.addGrade(90)
student1.addGrade(69)
student1.addGrade(30)
student1.getAv()
print(student1.attend)
print(student1.grades)
print(student1.getAv())

student2 = Student('Tharanga')
print(student2.nationality)
print(student2.age)
print(student2.attend)

for y in range(1, 21):
    student2.attenday()

student2.addGrade(50)
student2.addGrade(29)
student2.addGrade(70)
student2.getAv()
print(student2.attend)
print(student2.grades)
print(student2.getAv())

'''
r = Girls('Rachel')
s = Girls('Stanky')
print(r.gender)
print(s.gender)
print(r.name)
print(s.name)
'''


class Ads:
    a = 'this is called in from the class'

    def __init__(self, p1, p2):
        if p1 > p2:
            print('P1>P2')
        else:
            print('P2>P1')

    def cal(self, t1, t2):
        res = t1 + t2
        return res


al = Ads(10, 12)
a2 = Ads(15, 2)

tes = 100

print(al.a)
print(Ads.cal(tes, 15, 15))
