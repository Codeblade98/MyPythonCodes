name_list = ['Agnij', 'Nabayan', 'Chandril']
age_list = (17,18, 18)
rank_list = {1600, 3500, 5000}

print(list(zip(name_list, age_list, rank_list)))
print(tuple(zip(name_list, age_list, rank_list)))

# zip() can accept any number of iterables
# zip compiles the items of the iterables with same index number into a tuple