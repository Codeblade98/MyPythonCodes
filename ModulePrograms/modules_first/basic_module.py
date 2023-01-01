print('You have imported the basic_module')
def multiply(num1, num2):
    print(num1 * num2)

def divide(num1, num2):
    print(num1 / num2)

def add(num1, num2):
    print(num1 + num2)

def subtract(num1, num2):
    print(num1 - num2)

if __name__ == '__main__': #runs only if this is run, if imported this does not run
    print('The basic_module class is being executed in itself and not while imported')

