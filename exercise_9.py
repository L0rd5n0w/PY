from functools import reduce
#Square using lambda

my_list = [5,4,3]

print(list(map(lambda item: item*item, my_list)))

#PASSED

#List sorting

a = [(0,2), (4,3), (9,9), (10,-1)]

print(list(filter(lambda item: item, a.sort)))

#FAILED
