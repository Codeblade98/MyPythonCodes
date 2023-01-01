from functools import reduce
my_list = [1,2,3,4,5]
def accumulation(acc, item):
    return acc+item

print(reduce(accumulation, my_list, 0))
# check copy for algorithm of how reduce works