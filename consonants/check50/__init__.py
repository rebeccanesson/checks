from check50 import *

class Consonants(Checks): 

	@check()
	def exists(self):
		"""consonants.c exists"""
		self.require("consonants.c")

	@check("exists")
	def compiles(self):
		"""consonants.c compiles"""
		self.spawn("clang -o consonants consonants.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_ABCs(self):
		"""ABCs"""
		self.spawn("./consonants").stdin("Now I know my ABCs, next time won't you sing with me!").stdout("Nw  knw my BCs, nxt tm wn't y sng wth m!\n", "Nw  knw my BCs, nxt tm wn't y sng wth m!\n").exit(0)

