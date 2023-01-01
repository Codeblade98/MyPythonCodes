class PlayerCharacter:
    
    is_thirteen = True #is_thirteen is a class object attribute 

    #since is_thirteen is a class object attribute we can access it both by calling using class name or using self
    #refer notes

    def __init__(self, name = 'Guest', age = 18):

        '''

        __init__ is a magic method
        when we call init we a
        take name to be the parameter

        '''

        '''

        'self' is similar to 'this' keyword 
        in Java and is used to refer to 
        the current instance
        self is not a Python keyword but
        is a convention to write 'self' to 
        increase readability but we could use 
        any word for correct syntax

        '''
        

        if age>18: 
        #This would cause error if we tried to call player2 
        #This is because age of player2 is <18 so its attributes would not be instantiated
                   
            self.name = name #instantiation of an attribute
            self.age = age #instantiation of an attribute
            self._love = True #'_' is a covention to make other users understand that the attribute is private 

        # We always need to instantiate attributes
        # We cannot work upon non-instantiated attributes
   
   
    def run(self):
        print('Run')
    
    '''
    A class method receives the class as an implicit first argument, 
    just like an instance method receives the instance 

    class method is a method that is bound to the class and 
    not the object of the class.

    can modify a class state that would apply across all the instances of the class.
    ''' 
   
    @classmethod 
    def shoot(cls, new_name, new_age):
        return cls(new_name, new_age+1)

    def speak(self):
        print(f'{self.name} is speaking')


#player1 = PlayerCharacter() #creating new object player1 of class PlayerCharacter

#Exception has occurred: TypeError

#  we have a attribute 'name' which is not given

player1 = PlayerCharacter("Agnij", 19)
player2 = PlayerCharacter("Rahul", 25)
print(player1.name)
print(player2.age)
print(player1) #prints loctaion of player1
print(player2)

#on executing the code we see that player1 and player2 have different memory locations

player1.run() #calling run function
player1.dps = 100 #we give the attribute of dps to player1 which player2 cannot access
print(player1.dps)
print(player1.is_thirteen)
print(player2.is_thirteen)
print(PlayerCharacter.is_thirteen) #since is_thirteen is a class object method we can call it using the class name
#print(player2.dps) give error
print(player1.shoot('AWP',300))

player3 = PlayerCharacter.shoot('Destroy0p',19) #using the classmethod
print(player3.name)
print(player3.age)
player1.speak = 'BOOOO' #after this we cannot use speak function for player1 as it has changed to an attribute
print(player1.speak)
player2.speak() #but the speak function still works for player2
