print("Task 1")
a,b,c = list(map(int, input("enter tree numbers: ")))
the_same ={a, b, c}
if len(the_same)== 3:
	print("Error")
else:
	print("yes")

print("Task 2")

s = [a+b, a+c, b+c]

for i in s:
	if i in (a, b, c):
		print("yes")
		break

print("Task 3")
sum_num = 0
for i in range(15):
	sum_num += i
	print(sum_num)

print("Task 4")
day = {
	"Monday": 0,
	"Tuesday":1,
	"Wednsday":2,
	"Thursday":3,
	"Friday": 4,
	"Saturday": 5,
	"Sunday": 6,
}
count = 0
for i in to_day:
	if count < 5:
		print("Day", to_day[i] ,"it's weekday")
	else:
		print("Day", to_day[i] ,"it's weekend")
	count +=1
