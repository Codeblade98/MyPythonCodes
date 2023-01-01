from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']


#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]


#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]


#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

def convert_to_upper(item):
    return item.upper()

def accumulate(acc, item):
    return acc+item

def only_above_50(score):
    return score>50

print(list(map(convert_to_upper, my_pets)))
my_sorted_numbers = sorted(my_numbers)
print(list(zip(my_strings, my_sorted_numbers )))
print(list(filter(only_above_50, scores)))
print(reduce(accumulate, scores))
print(reduce(accumulate, my_numbers))