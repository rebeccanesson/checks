from check50 import *

class Largest(Checks): 

	@check()
	def exists(self):
		"""largest.c exists"""
		self.require("largest.c")

	@check("exists")
	def compiles(self):
		"""largest.c compiles"""
		self.spawn("clang -o largest largest.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_678432(self):
		"""678432 produces 8"""
		self.spawn("./largest").stdin("6").stdin("7").stdin("8").stdin("4").stdin("3").stdin("2").stdout("Largest: 8\n", "Largest: 8\n").exit(0)

	@check("compiles")
	def test_negative(self): 
		"""-10 -5 -30 -20 -60 -100 produces -5"""
		self.spawn("./largest").stdin("-10").stdin("-5").stdin("-30").stdin("-20").stdin("-100").stdout("Largest: -5\n", "Largest: -5\n").exit(0)

