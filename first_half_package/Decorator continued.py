def my_dec(fun):
    def wrap():
        print('Hey I am using my_dec')
        fun()
    return wrap

def my_dec1(fun):
    def wrap(param): #wrap func accepts the parameter as it is returned
        print('Hey I am using my_dec1')
        fun(param) #the param is used as a parameter of the to-be-modified func
    return wrap


def my_dec2(fun):
    def wrap(*args, **kwargs): #general use of a decorator
        print('Hey I am using my_dec2')
        fun(*args, **kwargs)
    return wrap


@my_dec
def hello():
    print('hello')

@my_dec1
def hello2(x):
    print(x)

@my_dec2
def hello3(greet1, greet2, emoji1 = ':)', emoji2= ':('):
    print(greet1, greet2, emoji1, emoji2)

#The system essentially works as
fun = my_dec(hello)
fun()
#these two lines can be replaced by decorator and same output is repeated while calling the function


#parameterised function using decorator
hello2('Hello')

#This works in the following way
fun1 = my_dec1(hello2)
fun1('Hello')


#calling hello3 
hello3('Hello again', 'heyy again', ':)', ':(')