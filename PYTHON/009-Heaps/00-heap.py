# =====================================================================================================================
# Heap
# =====================================================================================================================
# Heap is a complete binary tree ( Max. possible ht. is log(n) )
# - Cannot be used for searching ele
# - used only for 1. inserting 2. Deleting (that too only max/min)

import os, time

class Heap:
    """
    KEY: Indices start from 1 not 0.
        + parent_idx        = child_idx//2
        + left_child_idx    = parent_idx*2
        + right_child_idx   = parent_idx*2 + 1 


    DATA MEMBERS
        + _list                     : internal list representation of heap
        + __internal_list_size      : actual size of internal list
        + _size                     : size of heap

    METHODS
        + insert_from(lst)          : calls `__siftUp` on every ele of lst left to right
                                      or calls `__heapify` (check docstring)

    HELPER METHODS
        + __get_cur                 : returns to the last position idx (>=1 cz inices start from 1) in _list of heap
        + __append                  : appends to last empty pos of _list making sure indices start from 1
        + __make_room(max_ratio)    : if `_list` is full more than `max_ratio` increases size
        + __sift_up                 : 
        + __hepify                  : 
    """

    def __init__(self, contents=[], initial_size=10, creation_method="siftup"):
        # Note: idxs start from 1 not 0
        self._list  = [None]*initial_size 
        self._size  = 0

        self.__internal_list_size = initial_size

        # build heap
        self.insert_from(contents, method=creation_method)
    
    # ----------------------------------------------------------
    # Insertion
    # ----------------------------------------------------------
    def __get_cur(self):
        """returns idx of first `none` @end of _list"""
        # need `__get_cur` because even if we have `self._size` we cannot use
        # it as iit is for indexing of _list cz, it will always be one less
        # (because of empty `0`th idx)
        return  self._size + 1

    def __append(self, e):
        """
        makes sure indices start from 0

        Note: does not append to `Heap`. Appends to `_list`
        """
        self._list[self.__get_cur()] = e
        self._size += 1
        # no need to increment self.cur by 1 because,
        # it is dependant on size. (_size + 1)

    def __make_room(self, max_ratio=0.75, factor=2):
        # No need to make room at beginig of internal list 
        # as it will never be empty.
        cur_ratio = self._size / self.__internal_list_size
        if cur_ratio > max_ratio:
            new_list = [None] * (factor * self.__internal_list_size)
            for idx, e in enumerate(self._list):
                new_list[idx] = e
            # update:
            # self._size remains same
            self._list = new_list 
            self.__internal_list_size = factor * self.__internal_list_size

    """
    Method to add element `e` to the conceptual
    heap i.e to internal list in it's rightful place

    Note: CANNOT USE HEAPIFY HERE. IT IS MERELY A
    TECHNIQUE TO "CREATE HEAP FROM A SEQUENCE".
    BUT CANNOT BE USED TO APPEND AN ele TO CONCEPTUAL
    HEAP IN IT'S RIGHTFUL PLACE.
    """
    def __siftUp(self, e):
        """
        TIME:   O(logn)
        """

        # simply append e to the end of internal list.
        # simply appending in case of initial condition works just fine. 
        #  cz, no traversal cz, parent idx is 0 and while loop won't accept it
        self.__append(e)
        
        # sift up appended `e` from it's cur pos `self._size` to rightful positon
        # by succesively bringing down smaller parents until bigger parent is reached
        cur_idx = self._size
        par_idx = self._size // 2
        par_ele = self._list[par_idx]

        while (par_idx >= 1) and (e > par_ele):
            
            # bring parent **down** to it's child posn. if (cur_ele > par_ele)
            # note: but not swapping i.e bringing cur_ele to top 
            # (will be done in end of while loop)
            self._list[cur_idx] = par_ele

            # update:
            # cur_idx -> it's parent
            # par_idx -> it's parent
            cur_idx = cur_idx // 2
            par_idx = par_idx // 2
            par_ele = self._list[par_idx]
        
        # as `cur_idx`  will be updated to it's parent idx which is
        # the rightful place
        self._list[cur_idx] = e

    def __heapify(self, a_seq):
        """
        - right-to-left unlike left-to-right siftup
        - check if each cur e is root to max heap (if not, make it!)
        - inevitably we have to skip half of eles cz, leafs are already maxheaps

        TIME: O(n) ammortized as half of seq(leafs) need not be processed
        """
 
        # helpert recursive func
        def __make_p_maxheap_root(p_idx):
            """ 
            checks if parent at `p_idx` in internal list `self._list`
            is root of maxheap. and makes sure it is root of maxheap IN-PLACE.
            
            + Implemented recursively (can be done iteratively too)

            Time : O(logn)
            """
            c1_idx = p_idx*2
            c2_idx = c1_idx + 1

            # base condition [edge cases] 
            # 1. not out of idx (or)
            # 2. if children <= parent (or)
            if ((c1_idx > self._size+1) or (c1_idx == 0)) or \
                ((self._list[c1_idx] <= self._list[p_idx]) and (self._list[c2_idx] <= self._list[p_idx])):
                return # already max heap
            
            # PRE-ORDER ACTION
            # base condn failed i.e parent is less than one
            # of it's chldren.
            # So, replace parent with max_child 
            max_c_idx = None
            if (self._list[c1_idx] > self._list[c2_idx]): max_c_idx = c1_idx
            else: max_c_idx = c2_idx

            # swap inside _list
            _temp                   = self._list[max_c_idx]
            self._list[max_c_idx]   = self._list[p_idx]
            self._list[p_idx]       = _temp

            # recur not into both children!
            # only into the one we swapped.
            __make_p_maxheap_root(p_idx=max_c_idx)


        # end recursie def __is_p_maxheap_root

 
        p_idx_crawler = len(a_seq)-1
        while (p_idx_crawler>=1): 
            # check if p is root of max heap            
            c1_idx_crawler = p_idx_crawler * 2

            # avoid range error and leaves (as already maxheaps)
            # is it avoiding leaves?
            if (c1_idx_crawler < self._size+1):
                # makes parents maxheap in-place in `self._list`
                '''print("+"*40)
                print(self._list)
                print("bef")
                print(self._list)
                print(self._list[p_idx_crawler])
                print(self._list[c1_idx_crawler])
                print(self._list[c1_idx_crawler+1])'''
                __make_p_maxheap_root(p_idx_crawler)
                '''print("aft")
                print(self._list)
                print(self._list[p_idx_crawler])
                print(self._list[c1_idx_crawler])
                print(self._list[c1_idx_crawler+1])'''

            # update:
            # right to left
            p_idx_crawler = p_idx_crawler-1
        



    """
    Note: `Heapify` 
    """
    def insert_from(self, a_sequence, method="siftup"):
        """
        heapify is more efficient       --> O(n) ammortized
        Here, we are using __siftUp     --> O(nlogn)

        SIFTUP
            + starts from left-to-right of (raw)internal list from user
            + bottom-to-top approach - replaces by traversing parents
                + traverse parent-of-parent-of-parent ... until parent < cur_ele. 
                + while continuing to traverse, bring the parents down, 
                  then swap top-most parent with the cur_ele
                + O(n*logn)

        HEAPIFY
            + starts from right-to-left of (raw)internal list from user
            + top-to-bottom approach - replaces by traversing children
                + As half of eles will be leafs i.e no childern, no need to traverse them
                    + because [1] - no children - [2] - already a maxheap 
                + Hence, ammortized O(n) complexity
                + while moving left-to-right(of raw _list from user), 
                    + build maxheap w/ cur ele as root 
        
        Note: 
        - SIFTUP can replace HAEPIFY but NOT vice-versa! because,
        - SIFTUP >>cannot<< be used to insert SINGLE element

        TIME        : O(nlogn) / O(n)
        """
        # Note: idxs start from 1 not 0
        
        if method == 'siftup':
            # left to  right
            # --------------
            for e in a_sequence:
                    # makeroom if load > 0.75 ratio
                    self.__make_room(0.75)
                    # add element to heap using siftup
                    self.__siftUp(e)

        if method == 'heapify':
            # copy everything into internal list
            # which (heap w/ eles not in their rightful places)
            # time: O(2n) = O(n)
            for e in a_sequence:
                self.__make_room(0.75)
                self.__append(e)

            # crawl right to left and place eles n
            # in their rightful places
            self.__heapify(a_sequence)

    # ----------------------------------------------------------
    # Insertion single ele
    # ----------------------------------------------------------
    def insert(self, e):
        """ cannot use heapify. must use siftup """
        self.insert_from([e], method="siftup")

    # ----------------------------------------------------------
    # Deletion
    # ----------------------------------------------------------
    def pop(self):
        """ top of the maxheap is popped 
        
        - replace top w/ max of it's children (shift the child top)
        - repeat until c1_idx_crawler < self._size+1 (avoid out-of-idx error)


        TIME    : O(logn)
        """

        __cache = self._list[1]
        
        p_idx_crawler   = 1
        c1_idx_crawler  = p_idx_crawler * 2
        c2_idx_crawler  = c1_idx_crawler + 1
        
        while (c1_idx_crawler < self._size+1):
            
            # find max of children to top shifted 
            # in parent's position
            max_c_idx = None
            if (self._list[c1_idx_crawler] > self._list[c2_idx_crawler]): 
                max_c_idx = c1_idx_crawler
            else:
                max_c_idx = c2_idx_crawler

            # shift the child top
            self._list[p_idx_crawler] = self._list[max_c_idx]

            # update: (respective to the child that was sent above)
            p_idx_crawler   = max_c_idx
            c1_idx_crawler  = p_idx_crawler * 2
            c2_idx_crawler  = c1_idx_crawler + 1
        
        return __cache # popped


if __name__ == '__main__':
    
    def printline(text):
        print("="*100)
        print(f"+ {text}")
        print("="*100)    
    
    def test_childrens_small(internal_list, _internal_list_size):
        """ tests if children are less than parent """
        for p_idx in range(1, _internal_list_size+1):
            c1_idx = p_idx * 2
            c2_idx = c1_idx + 1 
            # avoid out-of-index error
            if c1_idx < (_internal_list_size+1):
                # test
                if (internal_list[p_idx] < internal_list[c1_idx]) or (internal_list[p_idx] < internal_list[c2_idx]):
                    return False
        
        return True


    lst = [11,77,33,66,99,33,66,44,-44,-22,-33]


    printline("1. Test creation (using siftup)")
    # 1. Test creation (using siftup)
    h = Heap(lst)
    # internal list retaining conceptual max-top tree
    is_parent_max = test_childrens_small(h._list, h._size)
    if is_parent_max is True:
        print("Test-1: Passed")
    else:
        print("Test-1: Failed")


    printline("2. Test creation (using heapify)")
    # 2. Test creation (using heapify)
    h2 = Heap(lst, creation_method="heapify")
    #print("heapify:", h2._list)
    #print("_siftup:", h._list)
    print("Note: different _list for heapify and siftup but both are maxheaps!")
    is_parent_max = test_childrens_small(h2._list, h2._size)
    if is_parent_max is True:
        print("Test-2: Passed")
    else:
        print("Test-2: Failed")


    printline("3. Test single ele insert")
    # 3. Test single ele insert
    # (cannot use heapify here)
    h.insert(98)
    h.insert(97)
    is_parent_max = test_childrens_small(h._list, h._size)
    if is_parent_max is True:
        print("Test-3: Passed")
    else:
        print("Test-3: Failed")


    printline("4. Test Deletion")
    # 4. Test Deletion
    popped = h.pop()
    print("deleted: ", popped)
    is_parent_max = test_childrens_small(h._list, h._size)
    if is_parent_max is True:
        print("Test-4: Passed")
    else:
        print("Test-4: Failed")