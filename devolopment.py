# Max or min number
from random import randrange
rand_list = [randrange(20) for i in range(5)]
num_min = rand_list[0]
num_max = rand_list[0]

print(rand_list)
for i in range(len(rand_list)):
	if num_min > rand_list[i]:
		num_min = rand_list[i]
	elif num_max < rand_list[i]:
		num_max = rand_list[i]


print ("Min: ",num_min,"\n","Max: ",num_max)