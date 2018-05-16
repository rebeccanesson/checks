from check50 import *

class Leap(Checks): 

	@check()
	def exists(self):
		"""leap.c exists"""
		self.require("leap.c")

	@check("exists")
	def compiles(self):
		"""leap.c compiles"""
		self.spawn("clang -o leap leap.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_2018(self):
		"""2018 is not a leap year"""
		self.spawn("./leap").stdin("2018").stdout("NO\n", "NO\n").exit(0)

	@check("compiles")
	def test_2016(self): 
		"""2016 is a leap year"""
		self.spawn("./leap").stdin("2016").stdout("YES!\n", "YES!\n").exit(0)

	@check("compiles")
	def test_2100(self): 
		"""2100 is not a leap year"""
		self.spawn("./leap").stdin("2100").stdout("NO\n", "NO\n").exit(0)

	@check("compiles")
	def test_2000(self): 
		"""2000 is a leap year"""
		self.spawn("./leap").stdin("2000").stdout("YES!\n", "YES!\n").exit(0)

