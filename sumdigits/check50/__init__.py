from check50 import *

class Sumdigits(Checks): 

	@check()
	def exists(self):
		"""sumdigits.c exists"""
		self.require("sumdigits.c")

	@check("exists")
	def compiles(self):
		"""sumdigits.c compiles"""
		self.spawn("clang -o sumdigits sumdigits.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_123(self):
		"""123 produces 6"""
		self.spawn("./sumdigits").stdin("123").stdout("Sum: 6\n", "Sum: 6\n").exit(0)

	@check("compiles")
	def test_negative_67(self): 
		"""-67 produces -13"""
		self.spawn("./sumdigits").stdin("-67").stdout("Sum: -13\n", "Sum: -13\n").exit(0)

