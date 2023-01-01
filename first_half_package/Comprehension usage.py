#list comprehension with examples
#syntax [param for param in iterable if condition]
#eg
my_list1 = [ char for char in 'Agnij Biswas']
print(my_list1)
my_list2 = [ num**2 for num in range(1,11)] #stores squares of numbers from 1 to 10
print(my_list2)
my_list3 = [ num for num in range(1,16) if num%2 == 0]
print(my_list3)

#similar for set comprehension
#eg
my_set1 = { char for char in 'Agnij Biswas'}
print(my_set1)
my_set2 = { num**2 for num in range(1,11)}#stores squares of numbers from 1 to 10
print(my_set2)
my_set3 = {num for num in range(1,16) if num%2 == 0}
print(my_set3)

#dictionary comprehension is a bit different
#eg
your_dict = {
    'a' : 1,
    'b' : 2,
    'c': 3
}
my_dict1 = {key:value*3 for key,value in your_dict.items()}
print(my_dict1)

my_dict2 = {num:num**2 for num in range(1,11)} #stores numbers from 1 to 10 as keys and squares as values
print(my_dict2)

my_dict3 = {key:value for key,value in enumerate('Agnij Biswas') if key%2 == 0}
print(my_dict3)
#we can use enumerate for dictionary comprehension

