class PyList:
	
	def __init__(self, contents=[], size=10): 
		"""
		Inputs
			contents: python list of any variable size.
			size: 				integer. It is size of `internal list` NOT of `contents`
		"""
		
		self._list = [None]*size 				# internal list. `size` != `_size`
		self._size = 0															# size of FILLED in _list
		self._len = len(self._list)	# size of _list including Nones
		
		# copy `contents` into `_list`.
		# CALL custom append method to reduce redundant code
		for ele in contents:
			self.append(ele)
			
	#end def __init__
	
	
	
	def __makeroom__(self):
		"""
		same as : `self._list += [None] * self._size.
		
		Makes room when once in a while internal list gets filled.`
		
		O(n)
		"""
		
		# create new list double the size
		new_list = [None] * (self._size * 2)
		
		# copy into tge new list
		for i in range(self._size):
			new_list[i] = self._list[i]
		
		# replace the old list with new
		self._list = new_list
	
	
	
	def append(self, ele):
		"""
		Inputs
			ele: python literal or object
			
		Trick for amortized time complexity 0(1).
		Create new list double the size and copy into itevery time 
		limit is reached and append.
		
		O(1) to O(n)
		"""
		
		if self._size < 0:
			raise IndexError("index out of range")
		
		# create new big list and copy to it
		elif self._size == self._len:
			self.__makeroom__()
			
		# append
		self._list[self._size] = ele
		self._size = self._size + 1
			
	#end def append
	
	
	
	def __getitem__(self, idx):
		"""
		inputs:
			idx: integer. index for accesor 
			
		usage: a = PyListObject[idx]
		
		O(1)
		"""
		
		if idx >= 0 and idx <= self._size:
			return self._list[idx]
		
		raise IndexError("Out of range")
	
	#end def __getitem__
	
	
	
	def __setitem__(self, idx, ele):
		"""
		inputs:
			idx: integer. index for mutator
			ele: python obj. to be mutated at idx
			
		usage: PyListObject[idx] = ele
		
		O(1)
		"""
		
		if idx >= 0 and idx <= self._size:
			self._list[idx] = ele
			return
		
		raise IndexError("Out of range")
		
	#end def __setitem__
	
	
	
	def __add__(self, other):
		"""
		inputs
			other: python obj of type PyList()
		
		usage: res_pylist = my_list1 + my_list2
		
		We will is the `append` method on new empty PyList
		object.
		
		O(n1 + n2)
		"""
		
		# create empty pylist and fill
		# using append
		res_pylist = PyList()
		
		for i in range(self._size):
			res_pylist.append(self._list[i])
			
		for i in range(other._size):
			res_pylist.append(other._list[i])
			
		return res_pylist
		
	#end def __add__
	
	
	
	def insert(self, i, ele):
		"""
		inputs
			ele {py obj} : element to be insterted
			i   {int}    : index where `ele` must be inserted
		
		usage: lst.insert(i, e)
		
		Shift to `n`(here 1) places right side starting from from end 
		and insert in the empty spaces formed in the middle
		
		O(n)
		"""
		
		if i < 0: raise IndexError("Index can not be negative")
		
		if self._size == self._len:
			self.__makeroom__()
			
		# because we are always incrementing by 1,
		# `_size` may have lower bound 0 but upper bound 
		# is `n` NOT `n-1`
		
		# if user tries to insert at first empty posn. at end (i=`n`)
		# our _size is already pointing to it.
		# or is user is trying to insert at i>n simply inserta at final
		# posn as we already had invariant assumption that there will be
		# no holes in middle
		
		if i <  self._size:
			
			# i. create emtpty space in middle (shift to right)
			for j in range(self._size-1, i-1, -1):
				self._list[j+1] = self._list[j]
				
			# ii. insert in empty space
			self._list[i] = ele
			self._size += 1 # >>>> see: we always update
			
		# if i in [last to inf], appenf at end
		else:
			self.append(ele)
	
	# end def insert
	
	
	
	def __delitem__(self, i):
		"""
		inputs
			i {int} : index of ele to be deleted
			
		usage: del py_list[i]
		
		O(n)
		"""
		
		# _size is always incremented by 1 in any magic func.
		# so, it will always be one unit greater
		if i < 0 or i > (self._size - 1):
			raise IndexError("	Index out of range")
			
		# always shift to left starting from empty loc
		else:
			for j in range(i, self._size - 1):
				self._list[j] = self._list[j+1]
			self._size -= 1 # see >> funcs always incr/decr _size
			
			# at pos `_size+1` we will not have None. instead we will have last element.
			# anyway tht wont be problem as our pointer `_size` isnt pointing to it. 
			# it was decremented (see last line above).
			# nontheless we can make it none using :
			self._list[ self._size ] = None
			
	# end def __delitem__
	
	
	
	def __iter__(self):
		"""
		usage: for ele in pylist: pass
		
		generator for iterator
		"""
		for i in range(self._size):
			yield self._list[i]
			
	# end def __iter__
	
	
	
	def __len__(self):
		"""
		usage: len(py_list)
		
		returns size of internal list (filled)
		"""
		return self._size
		
	#end def size
	
	
	
	def __eq__(self, other):
		"""
		inputs
			other {PyList obj}
			
		outputs
			returns bool
			
		usage: py_list1 == py_list2
			
		checks if two PyLists are identical
		
		O(n)
		"""
		
		# check for false rather than true.
		# easy and def 
		
		if type(self) != type(other):
			return False
		if len(self) != len(other):
			return False
			
		for i in range(self._size): # could have also use len() as we defined __len__()
			if self._list[i] != other._list[i]:
				return False
				
		#else
		return True
		
	# end def __eq__
	
	
	
	def __contains__(self, ele):
		"""
		input
			ele {py obj}
			
		output
			bool
			
		usage: ele in py_list2
		
		O(n) : linear search(unsorted)
		"""
		
		# easy and eff to return true first
		
		for i in range(search._size): # _size is always +1 even if it starts from 0 as we incr it everytime
			if self._list[i] == ele:
				return True
				
		return False
		
	#end def __contains__
	
	
	
	

# end class PyList
	
	
	

def main():
	# 1. empty list
	my_list = PyList()
	
	# 2. append
	my_list = PyList([1,2,3,4,5,6,7,8,9])
	my_list.append(10)
	print("after appnd 10:", my_list._list)
	my_list.append(11)
	print("after appnd 11:", my_list._list)
	
	# 3. get, set
	print( "\nelement at 4:", my_list[4] )
	my_list[4] = 999
	print("changed ele at 4:", my_list[4])
	
	# 4. concat
	res = PyList([1,2,3]) + PyList([6,7,8,9,10,11,12,13,14])
	print("\nconcatenated:", res._list)
	
	# 5. insert 
	# res.insert(-3, 999)
	res.insert(4, 999)
	print("999 inserted at 4:\n", res._list)
	res.insert(999, "x")
	print("x inserted at 999:(invar assumption)\n", res._list)
	res.insert(14, 'zz')
	print("zz inserted at end pos 14:\n", res._list)
	
	# 6. delete
	# del res[-1]
	# del res [15]
	del res[4]
	print("\ndeleted idx 4: ", res._list)
	del res[10]
	print("\ndeleted idx 10: ", res._list)
	
	# 6. Iterator
	print("\n iterator:")
	for i in res:
		print(i, end=" ")
	
	# 7. length
	print("\n\nlength is: ", len(res))
	
	# 8. equality
	a = [1,2,3]
	b = [1,2,3]
	c = [1,2,2]
	print("\npy_list a==b: ", PyList(a) == PyList(a))
	print("py_list a==c: ", PyList(a) == PyList(c))
	
	#9. search (contains)
	
	
	
	
	
	

# end def main
	
	
	
	
	
if __name__ == "__main__":
	main()