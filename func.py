def empty_fun ():# empty function
	pass

def sqrt_func(num):#"return sqrt number"
	return num**2

def even_odd(num):#even or odd
	if num % 2 == 0:
		print('yes')
	else:
		print('no')

def more_less (num1, num2):#more or less
	return ('да' if num1 > 10 else 'нет')


x = lambda x, y : x % y#lambda function
print(x(8,3))


def decorator_function(func):
    def wrapper():
        print('Функция-обёртка!')
        print('Оборачиваемая функция: {}'.format(func))
        print('Выполняем обёрнутую функцию...')
        func()
        print('Выходим из обёртки')
    return wrapper

@decorator_function
def hello_world():
     print('Hello world!')
print(hello_world())


list_number = list(map(lambda x: x**2, [i for i in range(10)]))
print(list_number)

list_word = list(filter(lambda x: x % 2 == 0, [i for i in range(20)]))
print(list_word)

l = []
x = 2
def clean(s):#clean function
	s += 1
	return s
print(clean(x))
print(x)

def dirty(l):#dirty function
	return l.append(2)
print(l)

def min_max (arg):#min max
	x_min = None
	x_max = None
	for i in arg:
		if x_min:
			if x_min > i:
				x_min = i
		else:
			x_min = i

	for n in arg:
		if x_max:
			if x_max < n:
				x_max = n
		else:
			x_max = n
	return x_min , x_max
print(min_max([1,2,3,4,20]))

def year(number):
	return (True if number % 4 == 0 and (number % 100 == 0  and number % 400 != 0) else False)
print(year(2000))

def season (month):
	d = {'Зима':[12,1,2],'Весна':[3,4,5],'Лето':[6,7,8],'Осень':[9,10,11]}
	for k,v in d.items():
		if month in v:
			return k
print(season (12))
