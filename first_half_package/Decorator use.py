def anakin_decorator(fun):
    def wrapper_fun():#wrapper function is always required otherwise function executed without call as decorator call highest order func
        print('\nAnakin Skywalker : ', end = '')
        fun()
    return wrapper_fun 

def obi_wan_decorator(fun):
    def wrapper_fun():#wrapper function is always required otherwise function executed without call as decorator call highest order func
        print('\nObi Wan Kenobi : ', end = '')
        fun()
    return wrapper_fun 
   

@obi_wan_decorator
def its_over():
    print('Its over Anakin, I have the high ground')
    
@anakin_decorator
def underestimate():
    print('You underestimate my power')

its_over()
underestimate()

#we can also do

obi_wan_decorator(its_over)()# calls the decorator as a function and takes its_over as a parameter


#The decorator assigns the to-be-modified function to a variable which on calling is used as a parameter of the decorator function 