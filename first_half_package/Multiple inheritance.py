class God(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age
    

class Dad(God):
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def attack(self):
        print('100 Damage done')


class Mom(God):
    def __init__(self,name, car):
        self.name = name
        self.car = car


class Child(Dad, Mom): #multiple inheritance
    def __init__(self, name, house, car):
        self.name = name
        Dad.__init__(self, name, house)
        Mom.__init__(self, name, car)
    
    def show(self):
        print(self.name, self.house, self.car)


child1 = Child('Andrew Tate', 'House', 'Bugatti')
child1.show()