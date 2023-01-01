def fun_test(*args, **kwargs):
    count = 0
    try:
        for item in args:
            int(item) 
            print(item)
            count +=1
        for key,value in kwargs.items():
            print(key, value)
            count += 1
        return count
    except ValueError as err:
        return err



    
