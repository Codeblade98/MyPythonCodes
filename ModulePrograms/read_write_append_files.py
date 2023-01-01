with open('test2.txt', mode = 'r+') as my_file:
# mode r+ allows us to read as well as write
    text = my_file.write('Hello There ')
    print(text) 

    #text stores the number of characters written
    #if we modify line 3 to write something else like 'AB', the cursor resets itself and the'He' of 'Hello There' is replaced by 'AB'

    # my_file.write('AB') 
    # this statement writes at the end but if some lines are changed it may cause unexpected problems
    # so we use append by changing mode to a

with open('test2.txt', mode = 'w') as my_file:
    #used to write in a completely brand new file
    text = my_file.write('Heyy')
    print(text)

    #Using mode w we rewrite the entire file, that is all previously written data is lost
    #We get a completely new file while using w

    
with open('test2.txt', mode = 'a') as my_file:
# mode a allows us to append
    text = my_file.write('Hello There ')
    print(text) 