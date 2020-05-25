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
	
	
	def append(self, ele):
		"""
		Inputs
			ele: python literal or object
			
		Trick for amortized time complexity 0(1).
		Create new list double the size and copy into itevery time 
		limit is reached and append.
		O(1) - O(n)
		"""
		
		if self._size < 0:
			raise IndexError("index out of range")
		
		# create new big list and copy to it
		elif self._size == self._len:
			new_list = [None] * (self._size * 2)
			for i in range(self._size):
				new_list[i] = self._list[i]
			self._list = new_list # same as `self._list = [None] * 2`
			
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
	
	
	
	

def main():
	#empty list
	my_list = PyList()
	
	#append
	my_list = PyList([1,2,3,4,5,6,7,8,9])
	my_list.append(10)
	print("after appnd 10:", my_list._list)
	my_list.append(11)
	print("after appnd 11:", my_list._list)
	
	# get, set
	print( "\nelement at 4:", my_list[4] )
	my_list[4] = 999
	print("changed ele at 4:", my_list[4])
	
	# concat
	res = PyList([1,2,3]) + PyList([6,7,8,9,10,11,12,13,14])
	print("\nconcatenated:", res._list)
	
	
	
	
if __name__ == "__main__":
	main()