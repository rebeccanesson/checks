from check50 import *

class Digits(Checks): 

	@check()
	def exists(self):
		"""digits.c exists"""
		self.require("digits.c")

	@check("exists")
	def compiles(self):
		"""digits.c compiles"""
		self.spawn("clang -o digits digits.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_1_23_456(self):
		"""1 23 456 produces 6"""
		self.spawn("./digits").stdin("1").stdin("23").stdin("456").stdout("Digits: 6\n", "Digits: 6\n").exit(0)

	@check("compiles")
	def test_0_100_10(self): 
		"""0 100 10 produces 6"""
		self.spawn("./digits").stdin("0").stdin("100").stdin("10").stdout("Digits: 6\n", "Digits: 6\n").exit(0)

	@check("compiles")
	def test_negative(self): 
		"""-1 -2 -3 produces 3"""
		self.spawn("./digits").stdin("-1").stdin("-2").stdin("-3").stdout("Digits: 3\n", "Digits: 3\n").exit(0)

