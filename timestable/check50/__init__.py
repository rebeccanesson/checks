from check50 import *

class TimesTable(Checks): 

	@check()
	def exists(self):
		"""timestable.c exists"""
		self.require("timestable.c")

	@check("exists")
	def compiles(self):
		"""timestable.c compiles"""
		self.spawn("clang -o timestable timestable.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test(self):
		"""times table"""
		self.spawn("./timestable").stdout("\n    1   2   3   4   5   6   7   8   9  10\n\n   1   1   2   3   4   5   6   7   8   9  10\n\n   2   2   4   6   8  10  12  14  16  18  20\n\n   3   3   6   9  13  15  18  21  24  27  30\n\n   4   4   8  12  16  20  24  28  32  36  40\n\n   5   5  10  15  20  25  30  35  40  45  50\n\n   6   6  12  18  24  30  36  42  48  54  60\n\n   7   7  14  21  28  35  42  49  56  63  70\n\n   8   8  16  24  32  40  48  56  64  72  80\n\n   9   9  18  27  36  45  54  63  72  81  90\n\n  10  10  20  30  40  50  60  70  80  90 100\n\n","\n    1   2   3   4   5   6   7   8   9  10\n\n   1   1   2   3   4   5   6   7   8   9  10\n\n   2   2   4   6   8  10  12  14  16  18  20\n\n   3   3   6   9  13  15  18  21  24  27  30\n\n   4   4   8  12  16  20  24  28  32  36  40\n\n   5   5  10  15  20  25  30  35  40  45  50\n\n   6   6  12  18  24  30  36  42  48  54  60\n\n   7   7  14  21  28  35  42  49  56  63  70\n\n   8   8  16  24  32  40  48  56  64  72  80\n\n   9   9  18  27  36  45  54  63  72  81  90\n\n  10  10  20  30  40  50  60  70  80  90 100\n\n").exit(0)
