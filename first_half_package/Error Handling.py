#Error Handling
# any error of the try block is caught by the except block
count = 0
while(True):
    try:
        age = int(input('Enter your age '))
        print(age)
        print(10/age)
        print
        raise NameError('Variable does not exist') #This raises an error which can be caught by the debugger 
        #if except block exists for a raised error, the debugger does not catch it
    
    except ValueError as err: #unless error specified all errors are caught by that
        print(f'Invalid Input, Enter a number \nError occured as {err}')

    #the as keyword helps us to take a variable which can store the python generated error message

    except ZeroDivisionError as err:
        print(f'Invalid Input, Enter a number greater than 0 \nError occured as {err}')
    
    except ValueError: #makes no difference as the exception for ValueError is already done before
        print('!!!')
    
    # except: This block if not a comment would catch all remaining errors, commented to show use of raise
    #     print('Something is wrong')

    else: #executed when try block is executed
        print('Thank you')
        break

    finally: #executed at the end of everything, both try and errors
        count+=1
        if count > 5:
            print('Entered wrong too man times, run again')
            break
    
