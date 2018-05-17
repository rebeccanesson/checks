from check50 import *

class EmptyBox(Checks): 

	@check()
	def exists(self):
		"""emptybox.c exists"""
		self.require("emptybox.c")

	@check("exists")
	def compiles(self):
		"""emptybox.c compiles"""
		self.spawn("clang -o emptybox emptybox.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_4(self):
		"""side length 4"""
		self.spawn("./emptybox").stdin("4").stdout("####\n#  #\n#  #\n####\n", "####\n#  #\n#  #\n####\n").exit(0)

	@check("compiles")
	def test_bad_inputs(self): 
		"""inputs 3 and 11 are rejected"""
		self.spawn("./emptybox").stdin("3").stdin("11").stdin("4").stdout("####\n#  #\n#  #\n####\n", "####\n#  #\n#  #\n####\n").exit(0)

