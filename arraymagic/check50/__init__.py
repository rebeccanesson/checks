from check50 import *

class ArrayMagic(Checks): 

	@check()
	def exists(self):
		"""arraymagic.c exists"""
		self.require("arraymagic.c")

	@check("exists")
	def compiles(self):
		"""arraymagic.c compiles"""
		self.spawn("clang -o arraymagic arraymagic.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_magic(self):
		"""276951438"""
		self.spawn("./arraymagic").stdin("2").stdin("7").stdin("6").stdin("9").stdin("5").stdin("1").stdin("4").stdin("3").stdin("8").stdout("MAGIC!\n", "MAGIC!\n").exit(0)

	@check("compiles")
	def test_not_magic(self): 
		"""275691843"""
		self.spawn("./arraymagic").stdin("2").stdin("7").stdin("5").stdin("6").stdin("9").stdin("1").stdin("8").stdin("4").stdin("3").stdout("NOT MAGIC.\n", "NOT MAGIC.\n").exit(0)

	@check("compiles")
	def test_rows_sum(self): 
		"""123123123"""
		self.spawn("./arraymagic").stdin("1").stdin("2").stdin("3").stdin("1").stdin("2").stdin("3").stdin("1").stdin("2").stdin("3").stdout("NOT MAGIC.\n", "NOT MAGIC.\n").exit(0)
	
	@check("compiles")
	def test_cols_sum(self): 
		"""111222333"""
		self.spawn("./arraymagic").stdin("1").stdin("1").stdin("1").stdin("2").stdin("2").stdin("2").stdin("3").stdin("3").stdin("3").stdout("NOT MAGIC.\n", "NOT MAGIC.\n").exit(0)
