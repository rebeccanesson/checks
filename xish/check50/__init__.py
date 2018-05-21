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


