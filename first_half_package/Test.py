T = int(input('Enter number of test cases '))

for case_num in range(0, T):
    input_num = int(input('Enter decision of referee '))
    sum = 0
    for i in range(0,4):
        k = input_num%10
        input_num = input_num//10
        sum+=k
    if sum > 3:
        print('IN')
    else:
        print('OUT')