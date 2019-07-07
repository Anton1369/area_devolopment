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