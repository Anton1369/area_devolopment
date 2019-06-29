# Max or min number
from random import randrange
rand_list = [randrange(25) for i in range(15)]
num_min = rand_list[0]
num_max = rand_list[0]

print(rand_list)
for i in range(len(rand_list)):
	if num_min > rand_list[i]:
		num_min = rand_list[i]
	elif num_max < rand_list[i]:
		num_max = rand_list[i]


print ("Min: ",num_min,"\n","Max: ",num_max)
# list 0 and 1
o_1 = []
for i in range(6):
	if i % 2 == 0 :
		o_1.append(0)
	else:
		o_1.append(1)
print(o_1)

#first and lost elemen list = 1 rest of us 0
one_0_0_one = []
for i in range(4):
	if i == 0 or i == 3:
		one_0_0_one.append(1)
	else:
		one_0_0_one.append(0)
print(one_0_0_one)

coppy_list = rand_list[:]
# if the list contains the same values display them
for i in rand_list:
	if coppy_list.count(i) > 1:
		print(i)
		del coppy_list[coppy_list.index(i)]
print(coppy_list)

#four simbol in the center string
a_z = "qwertyuiopasdfghjklzxcvbnm"
string = ""
for i in rand_list:
	string += a_z[i]
print(string)
a = len(string)//2-2
b = len(string)//2+2
print(string[a:b])
