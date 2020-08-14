# =====================================================================================================================
# Heap
# =====================================================================================================================
# Heap is a complete binary tree ( Max. possible ht. is log(n) )
# - Cannot be used for searching ele
# - used only for 1. inserting 2. Deleting (that too only max/min)

class Heap:
    """
    DATA MEMBERS
        + _list                     : internal list representation of heap
        + __internal_list_size      : actual size of internal list
        + _size                     : size of heap

    METHODS
        + insert_from(lst)          : calls `__siftUp` on every ele of lst left to right
                                        - makes room if load increases using __make_room()

    HELPER METHODS
        + __make_room(max_ratio)    : if `_list` is full more than `max_ratio` increases size
    """

    def __init__(self, contents=[], initial_size=10):
        self._list = [None] # idxs start from 1 not 0
        self._size = 0

        self.__internal_list_size = initial_size

        # build heap
        self.insert_from(contents)
    
    # ----------------------------------------------------------
    # Insertion
    # ----------------------------------------------------------
    def __make_room(self, max_ratio=0.75):
        cur_ratio = self.__internal_list_size / self._size
        if cur_ratio > max_ratio:
            new_list = [None] * (2 * self.__internal_list_size)
            for idx, e in enumerate(self._list):
                new_list[idx] = e
            # self._size remains same
            self._list = new_list 

    def __siftUp(self, cur_idx, cur_e):
        
        parent_idx  = cur_idx // 2
        parent_ele  = self._list[parent_idx]
        temp        = cur_e

        while (cur_idx>1) or (cur_e < parent_ele):
            # make parent child
            self._list[cur_idx] = self._list[parent_idx]
            
            cur_idx = cur_idx // 2



    def insert_from(self, a_sequence):
        """
        heapify is more efficient -- O(n)

        TIME        : O(nlogn)
        """
        for e in a_sequence:
            
            # initial condition (executed only once)
            # directly add root as there won't be anything to compare
            if self._list == [None]:
                self._list.append(e)
                self._size = 1
                continue

            # makeroom if filling > 0.75 ratio
            self.__make_room(0.75)

            # add element to heap
            last_idx = self._size + 1
            self.__siftUp(last_idx, e)