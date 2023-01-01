from functools import reduce

my_list = [1,2,3,4,5,6,7,8,9]
print(list(map(lambda item: item*2, my_list))) #using map by using lambda function
print(list(filter(lambda item: item%2 == 0, my_list))) #using filter using lambda function
print(reduce(lambda acc, item: acc+item, my_list, 0)) #using reduce using lambda function

#general syntax of lambda function is - 'lambda' parameters : action