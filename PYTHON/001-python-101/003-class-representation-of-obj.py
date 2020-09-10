class A:
    """
    Test class
    """
    def __init__(self, a):
        self.a = a
    
    def get_a(self):
        return self.a

    def set_a(self, a):
        self.a = a

if __name__ == '__main__':
    print("======================")
    print("+ CLASS.__dict__")
    print("======================")
    print(A.__dict__)

    print("======================")
    print("+ obj.__dict__")
    print("======================")
    obj = A(10)
    # prints all data members 
    print(obj.__dict__)
    # can even re-write
    # same as obj.set_a("changed!")
    obj.__dict__['a'] = 'changed indirectly!!'
    print(obj.get_a())


