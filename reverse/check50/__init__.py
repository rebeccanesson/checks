from check50 import *

class Reverse(Checks): 

	@check()
	def exists(self):
		"""reverse.c exists"""
		self.require("reverse.c")

	@check("exists")
	def compiles(self):
		"""reverse.c compiles"""
		self.spawn("clang -o reverse reverse.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_4(self):
		"""1 2 3 4 produces 4 3 2 1"""
		self.spawn("./reverse").stdin("4").stdin("1").stdin("2").stdin("3").stdin("4").stdout("4 3 2 1\n", "4 3 2 1\n").exit(0)

	@check("compiles")
	def test_illegal_input(self): 
		"""negative and 0 inputs"""
		self.spawn("./reverse").stdin("-4").stdin("0").stdin("1").stdin("5").stdout("5\n", "5\n").exit(0)

