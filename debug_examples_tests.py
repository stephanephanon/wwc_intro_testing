"""
This module contains some test cases you can try for the 
broken code in debug_examples.py

Can you think of additional edge cases and test cases to add?

Note that some of these tests are going to fail until you 
fix the logic in the functions. That's the unit tests 
hard at work!

"""

# 2. basic logic - missed an edge case
# --------------------------------------
def divide_by(num, denom):
	# divide num by denum
	return num / denom

# 3. conceptual error and/or typo
# ---------------------------------
def bigger_than_ten(x):
	# return True if x is bigger than 10 else False
	return 10 > x

# 4. conceptual error
# ---------------------
def less_than_elements(l, x):
	# return a list of all elements less than x
	for element in l:
	    low = []
	    if element < 5:
	        low.append(element)
	return low

# -------------------------------------------------------------
# NOTE!! You usually want to put your tests in a different file
# than your code. We are going to keep them together to make
# this example easier to follow
# -------------------------------------------------------------
import unittest
from unittest import TestCase

class DebugTests(TestCase):
	"""
	Tests on the functions in this file
	"""
	def test_divide_by_zero(self):
		# given that the denominator is 0
		test_denom = 0

		# when the function is called
		# then ZeroDivisionError is raised
		with self.assertRaises(ZeroDivisionError):
			divide_by(10, 0)

	def test_divide_ten_and_five(self):
		# given a non-0 numerator and denominator
		n = 10
		d = 5
		# when the function is called
		result = divide_by(n, d)

		# then the result = 2
		self.assertEqual(result, 2)

	def test_bigger_than_ten_is_eleven(self):
		# given a number > 10
		test_number = 11

		# when the function is called
		result = bigger_than_ten(test_number)

		# then True is returned
		self.assertTrue(result)

	def test_bigger_than_ten_is_ten(self):
		# given a number = 10
		test_number = 10

		# when the function is called
		result = bigger_than_ten(test_number)

		# then False is returned
		self.assertFalse(result)

	def test_bigger_than_ten_is_five(self):
		# given a number = 5
		test_number = 5

		# when the function is called
		result = bigger_than_ten(test_number)

		# then False is returned
		self.assertFalse(result)

	def test_less_than_elements_all_greater(self):
		# given a number x = 5
		# and given a list where all numbers are > 5
		x = 5
		l = [6, 7, 8, 10, 13]

		# when the function is called
		result = less_than_elements(l, x)

		# then an empty list is returned
		self.assertEqual(len(result), 0)

	def test_less_than_elements_all_less_than(self):
		# given a number x = 5
		# and given a list where all numbers are < 5
		x = 5
		l = [4, 1, 3, 2, 0]

		# when the function is called
		result = less_than_elements(l, x)

		# then a list with all the same elements is returned
		self.assertEqual(result, l)

	def test_less_than_elements_all_equal_to_x(self):
		# given a number x = 5
		# and given a list where all numbers are < 5
		x = 5
		l = [5, 5, 5, 5, 5]

		# when the function is called
		result = less_than_elements(l, x)

		# then an empty list is returned
		self.assertEqual(len(result), 0)

	def test_less_than_elements_empty_list(self):
		# given a number x = 5
		# and given a list where all numbers are > 5
		x = 5
		l = []

		# when the function is called
		result = less_than_elements(l, x)

		# then an empty list is returned
		self.assertEqual(len(result), 0)

