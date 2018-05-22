from check50 import *

class Max3(Checks): 

	@check()
	def exists(self):
		"""max3.c exists"""
		self.require("max3.c")

	@check("exists")
	def compiles(self):
		"""max3.c compiles"""
		self.spawn("clang -o max3 max3.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_77_99_88(self):
		"""77 99 88 produces 99"""
		self.spawn("./max3").stdin("77").stdin("99").stdin("88").stdout("Max: 99\n", "Max: 99\n").exit(0)

	@check("compiles")
	def test_99_77_88(self): 
		"""99 77 88 produces 99"""
		self.spawn("./max3").stdin("99").stdin("77").stdin("88").stdout("Max: 99\n", "Max: 99\n").exit(0)

	@check("compiles")
	def test_88_77_99(self): 
		"""88 77 99 produces 99"""
		self.spawn("./max3").stdin("88").stdin("77").stdin("99").stdout("Max: 99\n", "Max: 99\n").exit(0)

