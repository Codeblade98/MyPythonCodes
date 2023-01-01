def fib(num):
    t1 = 0
    t2 = 1
    
    if num > 0:
        for i in range(1,num+1):
            yield t1
            temp = t1
            t1 = t2
            t2 = temp + t1
    
    else:
        print('Invalid input, you may have inputted zero or a negative number')

#now since we have used a generator we can use the fib function as an iterable
#for automatically implements __next__() after each iteration

for fib_num in fib(20):
    print(fib_num, end = ' ') 
