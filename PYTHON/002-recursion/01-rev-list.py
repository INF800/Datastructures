"""
MY SOLN
"""
def recur(length):

	if length == 0:
		print(lst[length]) #LEGB
		return
	
	print(lst[length])
	recur(length-1)

lst = ['a', 'b', 'c', 'd']
recur(len(lst)-1)



"""
BOOK SOLN
"""
def revList(lst):
	# Here is the base case
	if lst == []:
		return []
	
	# The rest of this function is the recursive case.
	# This works because we called it on something smaller.
	# The lst[1:] is a slice of all but the first item in lst.
	restrev = revList(lst[1:])
	first = lst[0:1]
	
	# Now put the pieces together.
	result = restrev + first
	
	return result
 
print(revList(lst))