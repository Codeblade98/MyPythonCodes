class User(object):
    coins = 1000
    def __init__(self, username, password):
            print(f'Your username is {username} and password is ', '*'*(len(password)))
            self.username = username
            self.password = password
        
    def login(self):
        print('Login Successful')

class Wizard(User):
    def __init__( self, username, password, power = 'Fireball', damage = 200, health = 100):
        self.power = power
        self.damage = damage
        self.health = health
        User.__init__(self, username, password) #this statement helps us to access attributes of superclass
    
    def upgrade(self):
        upgrade_flag = input('Do you want to upgrade for 50 coins? Press 1 for yes and 0 for no ')
        if upgrade_flag:
            self.damage += 100 #always add self.'attribute name'
            self.health += 100
            self.coins -= 50 #coins is a class object attribute of the superclass so after inheritance we can directly use self


wizard1 = Wizard('Agnij', '*********')
print(wizard1.power)
wizard1.login()
print(wizard1.username)
print(wizard1.damage)
print(wizard1.health)
print(wizard1.coins)
wizard1.upgrade()
print(wizard1.damage)
print(wizard1.health)
print(wizard1.coins)
