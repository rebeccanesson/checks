from check50 import *

class Bmi(Checks): 

	@check()
	def exists(self):
		"""bmi.c exists"""
		self.require("bmi.c")

	@check("exists")
	def compiles(self):
		"""bmi.c compiles"""
		self.spawn("clang -o bmi bmi.c -lcs50 -lm").exit(0)

	@check("compiles")
	def test_132_64(self):
		"""132lbs, 64 inches, bmi: 23"""
		self.spawn("./bmi").stdin("132").stdin("64").stdout("BMI: 23\.203123\n", "BMI: 23.203123\n").exit(0)

	@check("compiles")
	def test_float_sides(self): 
		"""185lbs, 70 inches, bmi: 27"""
		self.spawn("./bmi").stdin("185").stdin("70").stdout("BMI: 27\.183674\n", "BMI: 27.183674\n").exit(0)

