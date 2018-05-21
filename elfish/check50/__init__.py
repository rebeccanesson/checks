from check50 import *

class Elfish(Checks): 

	@check()
	def exists(self):
		"""elfish.c exists"""
		self.require("elfish.c")

	@check("exists")
	def compiles(self):
		"""elfish.c compiles"""
		self.spawn("clang -o elfish elfish.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_elf(self):
		"""elf is elfish"""
		self.spawn("./elfish").stdin("elf").stdout("YES!\n", "YES!\n").exit(0)
	
	@check("compiles")
	def test_troll(self):
		"""troll is not elfish"""
		self.spawn("./elfish").stdin("troll").stdout("NO\n", "NO\n").exit(0)

	@check("compiles")
	def test_whiteleaf(self):
		"""whiteleaf is elfish"""
		self.spawn("./elfish").stdin("whiteleaf").stdout("YES!\n", "YES!\n").exit(0)
	
	@check("compiles")
	def test_hellish(self):
		"""hellish is not elfish"""
		self.spawn("./elfish").stdin("hellish").stdout("NO\n", "NO\n").exit(0)
