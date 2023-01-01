import re
pass_valid = re.compile(r"(^[a-zA-Z0-9@#$%]{7,}[0-9]$)")
while True:
    password = input('Enter your password ')
    check = pass_valid.search(password) #if password input is valid then give Match object else give none
    if check == None:
        print('Invalid password input')
        continue
    print('Thanks, password accepted')
    break


