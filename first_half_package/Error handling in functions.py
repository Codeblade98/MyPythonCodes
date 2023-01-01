def add(num1, num2):
    try:
        n1 = int(num1)
        print(n1+num2)
        print(50/n1)
    
    except (TypeError, ValueError, ZeroDivisionError) as err: # if we want similar output for multiple errors we do like this
        print(f'Error occured : \n {err}')
    

n1 = input('Enter 1st')
n2 = input('Enter 2nd')
add(n1,n2)
