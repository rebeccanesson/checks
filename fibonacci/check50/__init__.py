from check50 import *

class Fibonacci(Checks): 

	@check()
	def exists(self):
		"""fibonacci.c exists"""
		self.require("fibonacci.c")

	@check("exists")
	def compiles(self):
		"""fibonacci.c compiles"""
		self.spawn("clang -o fibonacci fibonacci.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_negative_input(self):
		"""negative number rejected, 0 allowed"""
		self.spawn("./fibonacci").stdin("-3").stdin("0").stdout("Fibonacci number 0 is 0\n", "Fibonacci number 0 is 0\n").exit(0)

	@check("compiles")
	def test_large_result(self): 
		"""10th fib number is 55"""
		self.spawn("./fibonacci").stdin("10").stdout("Fibonacci number 10 is 55\n", "Fibonacci number 10 is 55\n").exit(0)

