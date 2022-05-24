class Calculator():
	"""Calculator"""
	
	def add(self, x, y):
		return x + y

	def sub(self, x, y):
		return x - y

	def multi(self, x, y):
		return x * y


if __name__ == '__main__':
	calc = Calculator()
	print(calc.add(3,3))
	print(calc.sub(3,3))
	print(calc.multi(3, 3))

		