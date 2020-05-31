class LinkedList:
	
	class __Node:
		
		def __init__(self, item=None, next=None):
			"""
			+---------+---------
			|         |        |
			| item    |  next --->
			+---------+--------+
			"""
			self.item = item
			self.next = next
			
			
		# two main methods for two data members
		#  - set
		#  - get
		
		def getItem(self):
			return self.item
			
		def setItem(self, item):
			self.item = item
			
		def getNext(self):
			return self.next
			
		def setNext(self, next):
			self.next = next
			
			
	#end class __Node
	
	
	
	def __init__(self, contents=[]):
		"""
		first element and last element always point to
		dummy empty node to avoid spl. cases.
		Note: it is present even in non-empty linked list.
		"""
		self.first = self.__Node(None, None)
		self.last  = self.__Node(None, None) 
		self.size  = 0
		
		for ele in contents:
			# use built-in func to add items to 
			# linked list from py list
			self.append(ele)
			
	#end def __init__
	
	
	
	def append(self, ele):
		"""
		inputs
		  - ele - python object
		  
		usage: list1.append("abc")
		"""
		
		# 1. create new node with item `ele` pointing to `none`.
		# make new node as last node
		new_node  = self.__Node(ele, None)
		self.last = new_node
		
		# 2. if llist is empty, first and last node should be same
		# (otherwise dummy node will remain first node)
		if self.size == 0:
			self.first = self.last
			
		# 3. update len
		self.size += 1
		
		
	#end def __append__
	
	
	
def main():
	llist = LinkedList([1,0,-6,3])
	print("\nllist size: ", llist.size)
	print("last ele data, next: ", llist.last.item, llist.last.next)
	print("first ele data, next: ", llist.first.item, llist.first.next)
	
	
	
	
# end def 


if __name__ == "__main__":
	
	main()