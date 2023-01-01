def my_gen(num):
     for i in range(num):
        yield i

   
try:
    g = my_gen(5)
    print(g)
    next(g)
    print(g)
    next(g)
    print(g)
    next(g)
    print(g)
    next(g)
    print(g)
    next(g)
    print(g)
    #next(g) 
    #at this point we get stop iteration error
    #since we get error here we go to the except block after which control is not restored back to the try block
    #Therefore the last next g is commented out
    #all the g are stored at the same location

    g2 = my_gen(5)
    print(next(g2))
    print(next(g2))
    print(next(g2))
    print(next(g2))
    print(next(g2))
    print(next(g2))

except StopIteration:
        print('We have encountered stop iteration error')
        
