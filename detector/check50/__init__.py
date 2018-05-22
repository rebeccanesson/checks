from check50 import *

class Detector(Checks): 

	@check()
	def exists(self):
		"""detector.c exists"""
		self.require("detector.c")

	@check("exists")
	def compiles(self):
		"""detector.c compiles"""
		self.spawn("clang -o detector detector.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_foobar(self):
		"""foobar is a great word"""
		self.spawn("./detector").stdin("foobar").stdin("Foobar is a great word").stdout("YES!\n", "YES!\n").exit(0)
	
	@check("compiles")
	def test_terrible(self):
		"""foobar is a terrible word"""
		self.spawn("./detector").stdin("terrible").stdin("Foobar is a terrible word").stdout("YES!\n", "YES!\n").exit(0)

	@check("compiles")
	def test_great(self):
		"""foobar is a great and terrible word"""
		self.spawn("./detector").stdin("great").stdin("Foobar is a terrible word").stdout("NO\n", "NO\n").exit(0)
	
	@check("compiles")
	def test_foo(self):
		"""that is a lot of foo"""
		self.spawn("./detector").stdin("FOOBAR").stdin("Wow, that is a lot of foo!").stdout("NO\n", "NO\n").exit(0)

