"""
oops object methods are 2 types
    1. mutators
    2. accessors

All objects have accessors. some have mutators and some do not.
Objects without mutators - "immutable"

eg. str, int and float
"""

a = "python"

print("accessors access:", a[2])

try:
	a[2] = "x"
except Exception as e:
	print("mutation error:", e)
	
try:
	del a[2]
except Exception as e:
	print("mutation error:", e)
	

