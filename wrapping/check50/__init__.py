from check50 import *

class Wrapping(Checks): 

	@check()
	def exists(self):
		"""wrapping.c exists"""
		self.require("wrapping.c")

	@check("exists")
	def compiles(self):
		"""wrapping.c compiles"""
		self.spawn("clang -o wrapping wrapping.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_7_5_2(self):
		"""7, 5, 2 produces 15 x 11"""
		self.spawn("./wrapping").stdin("7").stdin("5").stdin("2").stdout("Length: 15\.000000 Width: 11\.000000\n", "Length: 15.000000 Width: 11.000000\n").exit(0)

	@check("compiles")
	def test_float_sides(self): 
		"""6.5, 6.5, 1 produces 16 x 8.5"""
		self.spawn("./wrapping").stdin("6.5").stdin("6.5").stdin("1").stdout("Length: 16\.000000 Width: 8\.500000\n", "Length: 16.000000 Width: 8.500000\n").exit(0)

