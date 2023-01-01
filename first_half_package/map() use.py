#Use of map function

def multiply_by2(item):
    return(item*2)

print(map(multiply_by2,[1,2,3])) #prints object location as '<map object at 0x00000172EBABD030>'
print(list(map(multiply_by2,[1,2,3]))) #prints a list created by multiplying each element of the input list by 2
print(tuple(map(multiply_by2,[1,2,3]))) #prints a tuple created by multiplying each element of the input list by 2
print(set(map(multiply_by2,[1,2,3]))) #prints a set created by multiplying each element of the input list by 2



#map is a pure function and does not modify input list
#for the input we could have given any data structure and not just lists

