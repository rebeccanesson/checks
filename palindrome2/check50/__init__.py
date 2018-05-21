from check50 import *

class Palindrome2(Checks): 

	@check()
	def exists(self):
		"""palindrome2.c exists"""
		self.require("palindrome2.c")

	@check("exists")
	def compiles(self):
		"""palindrome2.c compiles"""
		self.spawn("clang -o palindrome2 palindrome2.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_Racecar(self):
		"""Racecar is a palindrome"""
		self.spawn("./palindrome2").stdin("Racecar").stdout("YES!\n", "YES!\n").exit(0)

	@check("compiles")
	def test_Clunker(self): 
		"""Clunker is not a palindrome"""
		self.spawn("./palindrome2").stdin("Clunker").stdout("NO\n", "NO\n").exit(0)

	@check("compiles")
	def test_poop(self): 
		"""poop is a palindrome"""
		self.spawn("./palindrome2").stdin("poop").stdout("YES!\n", "YES!\n").exit(0)

	@check("compiles")
	def test_adam(self): 
		"""Madam, I'm Adam! is a palindrome"""
		self.spawn("./palindrome2").stdin("Madam, I'm Adam!").stdout("YES!\n", "YES!\n").exit(0)
