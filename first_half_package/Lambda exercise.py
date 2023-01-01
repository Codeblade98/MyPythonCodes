my_list = [5,4,3] #write one line expression to return a list pf squares
print(list(map(lambda item : item * item, my_list)))

a = [(0,2) , (4,3) , (9,9) , (10,-1)] #write one line expression to return list sorted acc to 2nd element of each tuple
b =[1,2,5,4,0,67,51]
b.sort()
print (b)
a.sort(key = lambda a: a[1])# the sort function accepts the key on basis of which it sorts a list
print (a)
