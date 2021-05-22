import unittest 
from leapyear import leapCalc 

class TestLeapYear(unittest.Testcase):

	def test_leapyear(self):
		assert leapCalc('2000') is True
		assert leapCalc('2020') is True

	def test_notleap(self):
		assert leapCalc('2015') is False
		assert leapCalc('2014') is False

	def test_character(self):
		assert leapCalc('2015!') is False
		assert leapCalc('2020!') is False

if __name__ == '__main__':
	unittest.main()
	 
