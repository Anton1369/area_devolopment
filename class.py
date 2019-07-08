#Task 1
class Apple():
	def __init__(self, width, size, sort, color):
		self.width = width
		self.size = size
		self.sort = sort
		self.color = color


a = Apple(10, 30, 'Big_boy','green')
print(a.sort)

#Task 2
from math import pi
class Circle():
	def __init__(self, p, r):
		self.r = r
		self.p = p
	
	def area(self):
		return (self.r)**2 * self.p

c = Circle(pi, 20)
print(c.area())

#Task 3
class Person():
	def __init__(self, first_name, last_name, kwalification = 1):
		self.first_name = first_name
		self.last_name = last_name
		self.kwalification = kwalification

	def information(self):
		return "name : {0}; last name :{1}; kwalification: {2}".format(self.first_name, self.last_name, self.kwalification)

pers = Person('Anton', 'Anikin')
print(pers.information())

class Rectangle():
	def __init__(self, higth, width):
		self.higth = higth
		self.width = width

	def calculate_perimeter(self):
		return (self.higth * 2) + (self.width * 2)

class Square():
	def __init__(self, higth, width):
		self.higth = higth
		self.width = width

	def calculate_perimeter(self):
		return (self.higth * 2) + (self.width * 2)

	def change_size(self, num):
		self.higth += num
		self.width += num



s = Square(5, 10)
print(s.calculate_perimeter())
print(s.higth)
s.change_size(10)
print(s.calculate_perimeter())
s.change_size(-10)
print(s.calculate_perimeter())
