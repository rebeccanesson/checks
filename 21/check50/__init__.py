from check50 import *

class TwentyOne(Checks): 

	@check()
	def exists(self):
		"""21.c exists"""
		self.require("21.c")

	@check("exists")
	def compiles(self):
		"""21.c compiles"""
		self.spawn("clang -o 21 21.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_123456(self):
		"""123456 produces 21"""
		self.spawn("./21").stdin("1").stdin("2").stdin("3").stdin("4").stdin("5").stdout("Sum: 21\n", "Sum: 21\n").exit(0)

	@check("compiles")
	def test_55555(self): 
		"""55555 produces 25"""
		self.spawn("./21").stdin("5").stdin("5").stdin("5").stdin("5").stdin("5").stdout("Sum: 25\n", "Sum: 25\n").exit(0)

	@check("compiles")
	def test_33(self): 
		"""33 produces 33"""
		self.spawn("./21").stdin("33").stdout("Sum: 33\n").exit(0)

