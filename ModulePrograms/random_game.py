import sys
from random import randint

print('Your input has been accepted')

def num_checker(num,start = 0,end = 10):
    try: 
        number = randint(start,end)
        return num == number
    
    except ValueError as err:
        return err

    except TypeError as err:
        return err


if __name__ == '__main__':       
    start = int(sys.argv[1])
    end = int(sys.argv[2])

    while True:    
        input_num = int(input('Enter your guess '))
        if num_checker(input_num, start, end):
            print('Well done')
            break
        else:
            print('Try harder......Try better')

