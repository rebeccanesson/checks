from check50 import *

class Xish(Checks): 

	@check()
	def exists(self):
		"""xish.c exists"""
		self.require("xish.c")

	@check("exists")
	def compiles(self):
		"""xish.c compiles"""
		self.spawn("clang -o xish xish.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_elf(self):
		"""elf is elfish"""
		self.spawn("./xish").stdin("elf").stdin("elf).stdout("YES!\n", "YES!\n").exit(0)
	
	@check("compiles")
	def test_troll(self):
		"""troll is not elfish"""
		self.spawn("./xish").stdin("elf").stdin("troll").stdout("NO\n", "NO\n").exit(0)

	@check("compiles")
	def test_carrot(self):
		"""carrot is cattish"""
		self.spawn("./xish").stdin("cat").stdin("carrot").stdout("YES!\n", "YES!\n").exit(0)
	
	@check("compiles")
	def test_card(self):
		"""card is not cattish"""
		self.spawn("./xish").std("cat").stdin("card").stdout("NO\n", "NO\n").exit(0)

	@check("compiles")
	def test_dandy(self)
		"""Dan is a dandy"""
		self.spawn("./xish").stdin("Dan").stdin("dandy").stdout("YES!\n", "YES!\n").exit(0)
	
	@check("compiles")
	def test_card(self):
		"""Doug is doggish"""
		self.spawn("./xish").std("dog").stdin("Doug").stdout("YES!\n", "YES!\n").exit(0)
