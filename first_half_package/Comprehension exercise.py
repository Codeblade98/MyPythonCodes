my_list = ['a', 'b', 'c', 'd', 'e', 'b', 'f', 'd', 'b', 'g']
duplicate_list = list({item for item in my_list if my_list.count(item)>1})
print(duplicate_list)