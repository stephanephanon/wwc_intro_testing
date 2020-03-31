"""
This module has the answers that go with debug_examples.py

Note that all of these can be debugged in multiple ways! 
Choose a way that works for you and practice it. :)

Try debugging these examples by using one or more of the following:
1. print
2. logging
3. assertions
4. pdb debugger
"""

# 1. syntax error
# -----------------
def say_hello(name):
	print("hello {}".format(nmae))

# ANSWER:
# raises an exception NameError. 
# Look at the stack trace. 
# It says something is wrong around line 17. 
# There is a typo in this code (syntax error)

# How would you fix? Get rid of the typo.

# 2. basic logic - missed an edge case
# --------------------------------------
def divide_by(num, denom):
	# divide num by denum
	return num / denom

# ANSWER: 
# This code misses an edge case. ZeroDivisionError.
# Dividing by 0 is NOT allowed
# Look at the stack trace.

# How would you fix? Can you add a check for that denominator?

# 3. conceptual error and/or typo
# ---------------------------------
def bigger_than_ten(x):
	# return True if x is bigger than 10 else False
	return 10 > x

# ANSWER:
# This code has a conceptual error or it could be a typo.
# The code should return True if x is BIGGER THAN 10

# How would you fix? Update the > to be <


# 4. conceptual error
# ---------------------
def less_than_elements(l, x):
	# return a list of all elements less than x
	for element in l:
	    low = []
	    if element < x:
	        low.append(element)
	return low

# ANSWER: 
# This code has a conceptual error. The code SHOULD return 
# a list of elements in low, but low is getting reset to empty 
# list for EACH loop of l.
# You could troubleshoot by printing 'element', 'l', and 'low' as the function executes

# How would you fix? Move low = [] ABOVE the for loop

