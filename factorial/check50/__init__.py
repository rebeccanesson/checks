from check50 import *

class Factorial(Checks): 

	@check()
	def exists(self):
		"""factorial.c exists"""
		self.require("factorial.c")

	@check("exists")
	def compiles(self):
		"""factorial.c compiles"""
		self.spawn("clang -o factorial factorial.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_negative_input(self):
		"""negative number and 0 rejected"""
		self.spawn("./factorial").stdin("-3").stdin("0").stdin("7").stdout("Fact: 5040\n", "Fact: 5040\n").exit(0)

	@check("compiles")
	def test_large_result(self): 
		"""no overflow on large input"""
		self.spawn("./fact").stdin("20").stdout("Fact: 2432902008176640000\n", "Fact: 2432902008176640000\n").exit(0)

