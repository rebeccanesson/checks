from check50 import *

class Palindrome(Checks): 

	@check()
	def exists(self):
		"""palindrome.c exists"""
		self.require("palindrome.c")

	@check("exists")
	def compiles(self):
		"""palindrome.c compiles"""
		self.spawn("clang -o palindrome palindrome.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_Racecar(self):
		"""Racecar is a palindrome"""
		self.spawn("./palindrome").stdin("Racecar").stdout("YES!\n", "YES!\n").exit(0)

	@check("compiles")
	def test_Clunker(self): 
		"""Clunker is not a palindrome"""
		self.spawn("./palindrome").stdin("Clunker").stdout("NO\n", "NO\n").exit(0)


