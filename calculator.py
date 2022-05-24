class Calculator():
	"""Calculator"""
	
	def add(self, *args):
		return sum(args)

	def sub(self, x, y):
		return x - y

	def multi(self, x, y):
		return x * y

	def division(self, x, y):
		if y == 0:
			return None
		return x / y

	def is_even(self, x):
		if x % 2 == 0:
			return True 
		return False 

	def divisors(self, x):
		divisors = []
		for i in range(1,x + 1):
			if x % i == 0:
				divisors.append(i)
		return divisors



if __name__ == '__main__':
	calc = Calculator()
	print(calc.add(3,3))
	print(calc.add("ab","cd"))
	print(calc.sub(3,3))
	print(calc.multi(3, 3))

		