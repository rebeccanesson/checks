from check50 import *

class Pythagoras(Checks): 

	@check()
	def exists(self):
		"""pythagoras.c exists"""
		self.require("pythagoras.c")

	@check("exists")
	def compiles(self):
		"""pythagoras.c compiles"""
		self.spawn("clang -o pythagoras pythagoras.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_3_4(self):
		"""sides 3 and 4 produce hypotenuse 5"""
		self.spawn("./pythagoras").stdin("3").stdin("4").stdout("5.000000\n", "5.000000\n").exit(0)

	@check("compiles")
	def test_3.6_7.2(self): 
		"""sides 3.6 and 7.2 produce hypotenuse 8.049845"""
		self.spawn("./pythagoras").stdin("3.6").stdin("7.2").stdout("8.049845\n", "8.049845\n").exit(0)

