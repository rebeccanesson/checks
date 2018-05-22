from check50 import *

class Santizer(Checks): 

	@check()
	def exists(self):
		"""santizer.c exists"""
		self.require("sanitizer.c")

	@check("exists")
	def compiles(self):
		"""santizer.c compiles"""
		self.spawn("clang -o sanitizer sanitizer.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_song(self):
		"""I don't give a minkle"""
		self.spawn("./sanitizer").stdin("I don't give a minkle if you don't like my schmaltzy song.\n").stdout("I don't give a m$#%!e if you don't like my s$#@@!#zy song.\n", "I don't give a m$#%!e if you don't like my s$#@@!#zy song.\n").exit(0)

