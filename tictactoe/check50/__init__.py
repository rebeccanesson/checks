from check50 import *

class TicTacToe(Checks): 

	@check()
	def exists(self):
		"""tictactoe.c exists"""
		self.require("tictactoe.c")

	@check("exists")
	def compiles(self):
		"""tictactoe.c compiles"""
		self.spawn("clang -o tictactoe tictactoe.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_X_wins(self):
		"""X wins"""
    		self.spawn("./tictactoe").stdin("1").stdin("1").stdin("0").stdin("0").stdin("2").stdin("2").stdin("1").stdin("0").stdin("0").stdin("1").stdin("2").stdin("0").stdout("\nPlayer X wins!!\n", "\nPlayer X wins!!\n").exit(0)

