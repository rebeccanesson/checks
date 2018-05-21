from check50 import *

class ArrayMagic2(Checks): 

	@check()
	def exists(self):
		"""arraymagic2.c exists"""
		self.require("arraymagic2.c")

	@check("exists")
	def compiles(self):
		"""arraymagic2.c compiles"""
		self.spawn("clang -o arraymagic2 arraymagic2.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_magic_3(self):
		"""276951438"""
		self.spawn("./arraymagic2").stdin("3").stdin("2").stdin("7").stdin("6").stdin("9").stdin("5").stdin("1").stdin("4").stdin("3").stdin("8").stdout("MAGIC!\n", "MAGIC!\n").exit(0)

	@check("compiles")
	def test_not_magic_3(self): 
		"""275691843"""
		self.spawn("./arraymagic2").stdin("3").stdin("2").stdin("7").stdin("5").stdin("6").stdin("9").stdin("1").stdin("8").stdin("4").stdin("3").stdout("NOT MAGIC.\n", "NOT MAGIC.\n").exit(0)

	@check("compiles")
	def test_magic_4(self): 
		"""1 15 14 4 12 6 7 9 8 10 11 5 13 3 2 16"""
		self.spawn("./arraymagic2").stdin("4").stdin("1").stdin("15").stdin("14").stdin("4").stdin("12").stdin("6").stdin("7").stdin("9").stdin("8").stdin("10").stdin("11").stdin("5").stdin("13").stdin("3").stdin("2").stdin("16").stdout("MAGIC!\n", "MAGIC!\n").exit(0)
	
	@check("compiles")
	def test_magic_5(self): 
		"""17 24 1 8 15 23 5 7 14 16 4 6 13 20 22 10 12 19 21 3 11 18 25 2 9"""
		self.spawn("./arraymagic2").stdin("5").stdin("17").stdin("24").stdin("1").stdin("8").stdin("15").stdin("23").stdin("5").stdin("7").stdin("14").stdin("16").stdin("4").stdin("6").stdin("13").stdin("20").stdin("22").stdin("10").stdin("12").stdin("19").stdin("21").stdin("3").stdin("11").stdin("18").stdin("25").stdin("2").stdin("9").stdout("MAGIC!\n", "MAGIC!\n").exit(0)

	
	@check("compiles")
	def test_not_magic_illegal_inputs_5(self): 
		"""rejects size 2 and 6, 17 24 8 1 15 23 5 7 14 16 4 6 13 20 22 10 12 19 21 3 11 18 25 2 9"""
		self.spawn("./arraymagic2").stdin("2").stdin("6").stdin("5").stdin("17").stdin("24").stdin("8").stdin("1").stdin("15").stdin("23").stdin("5").stdin("7").stdin("14").stdin("16").stdin("4").stdin("6").stdin("13").stdin("20").stdin("22").stdin("10").stdin("12").stdin("19").stdin("21").stdin("3").stdin("11").stdin("18").stdin("25").stdin("2").stdin("9").stdout("NOT MAGIC.\n", "NOT MAGIC.\n").exit(0)
