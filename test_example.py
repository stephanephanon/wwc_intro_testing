"""
This module contains code and testing examples to accompany the
Women Who Code DC Python workshop on debugging and testing

https://docs.python.org/3/library/unittest.html

We will be investigating unit tests to the fizz_buzz function

How to Run Your Tests
---------------------

On the command line run unittest against the test_example module (-m)
>> python -m unittest test_example.py

And Python will run your tests and report results like this:
.....
----------------------------------------------------------------------
Ran 5 tests in 0.000s

OK

"""

# our function to test
def fizz_buzz(int_number):
    """
    Return fizz if number is a multiple of 3
    Return buzz if number is a multiple of 5
    Return fizzbuzz if number is a multiple of 3 and 5
    Else return the number
    If the number is NOT a number, then raise a ValueError
    """
    # don't work with non-numeric input
    if not isinstance(int_number, int):
        raise ValueError("int_number must be an integer")

    # got a number!
    if int_number % 3 == 0 and int_number % 5 == 0:
        return 'fizzbuzz'
    elif int_number % 3 == 0:
        return 'fizz'
    elif int_number % 5 == 0:
        return 'buzz'
    else:
        return int_number


# -------------------------------------------------------------
# NOTE!! You usually want to put your tests in a different file
# than your code. We are going to keep them together to make
# this example easier to follow
# -------------------------------------------------------------
import unittest
from unittest import TestCase


class FizzBuzzTests(TestCase):
    def test_multiple_of_three(self):
        # given number is a multiple of 3 but not 5
        test_number = 6

        # when fizz_buzz is called
        result = fizz_buzz(test_number)

        # then fizz is returned
        self.assertEqual(result, "fizz")

    def test_multiple_of_five(self):

        # given number is multiple of 5 but not 3
        test_number = 10

        # when fizz_buzz is called
        result = fizz_buzz(test_number)

        # then buzz is returned
        self.assertEqual(result, "buzz")

    def test_multiple_of_three_and_five(self):

        # given number is a multiple of 3 and 5
        test_number = 15

        # when fizz_buzz is called
        result = fizz_buzz(test_number)

        # then fizz is returned
        self.assertEqual(result, "fizzbuzz")

    def test_not_a_multiple_of_three_or_five(self):

        # given number is NOT a multiple of 3 and 5
        test_number = 22

        # when fizz_buzz is called
        result = fizz_buzz(test_number)

        # then fizz is returned
        self.assertEqual(result, test_number)

    def test_bad_input(self):
        # NOTE! assertRaises has a different format

        # given a non-numeric test_bad_input
        test_number = "oops"

        # when fizz_buzz is called
        # then a ValueError is raised
        with self.assertRaises(ValueError):
            fizz_buzz(test_number)

