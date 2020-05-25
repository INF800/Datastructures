class PyList:
	
	def __init__(self, contents=[], size=10): 
		"""
		Inputs
			contents: python list of any variable size.
			size: 				integer. It is size of `internal list` NOT of `contents`
		"""
		
		self.__list = [None]*size 				# internal list. `size` != `__size`
		self.__size = 0															# size of FILLED in __list
		self.__len = len(self.__list)	# size of __list including Nones
		
		# copy `contents` into `__list`.
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
		"""
		
		if self.__size < 0:
			raise IndexError("index out of range")
		
		elif self.__size == self.__len:
			new_list = [None] * (self.__size * 2)
			for i in range(self.__size):
				new_list[i] = self.__list[i]
			self.__list = new_list
			
		self.__list[self.__size] = ele
		self.__size = self.__size + 1
			
	#end def append
	

	
	
	

	def get__list(self):
		return self.__list
	
	
	
	


def main():
	#empty list
	my_list = PyList()
	
	my_list = PyList([1,2,3,4,5,6,7,8,9])
	my_list.append(10)
	print("after appnd 10:", my_list.get__list())
	my_list.append(11)
	print("after appnd 11:", my_list.get__list())
	
	
if __name__ == "__main__":
	main()