"""
This module contains broken code examples to accompany the 
Women Who Code DC Python workshop on debugging and testing

It contains BROKEN CODE! You will need to uncomment/comment 
code as you go.

Try debugging these examples by using one or more of the following:
1. print
2. logging
3. assertions
4. pdb interactive debugger

How to Run This File
--------------------
On the command line run unittest against the test_example module (-m)
>> python debug_examples.py

"""

# 1. syntax error
# -----------------
def say_hello(name):
	print("hello {}".format(nmae))

# what happens when you uncomment this code? how would you debug it?
# say_hello("judy")


# 2. basic logic - missed an edge case
# --------------------------------------
def divide_by(num, denom):
	# divide num by denum
	return num / denom

# what happens when you run this code? uncomment next lines and test it.
# good_result = divide_by(10, 5)
# bad_result = divide_by(100, 0)


# 3. conceptual error and/or typo
# ---------------------------------
def bigger_than_ten(x):
	# return True if x is bigger than 10 else False
	return 10 > x

# what happens when you run this code? uncomment next line and test it
# bad_result = bigger_than_ten(5)


# 4. conceptual error
# ---------------------
def less_than_elements(l, x):
	# return a list of all elements less than x

	# import pdb; pdb.set_trace()
	for element in l:
	    low = []
	    if element < 5:
	        low.append(element)
	return low


# what happens when you run this code? uncomment the next lines and test it
# my_list = [5, 2, 14, 7, 1, 9, -2]
# bad_result = less_than_elements(my_list, 5)

