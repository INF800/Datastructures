from utility import Queue

class RadixSort:
    """
    DATA MEMEBRS
        - main_q    : main queue for storing inputs (sorted inplace here)
        - max_len   : length of largest item/word in inputs >>(inclusive)<<
        - qs        : alphabet queues dictionary
                        + k - alphabet; v - empty queue initialy 

    METHODS
        - char_at   : helper func. Rreturns space for smaller words
        - sort      : radix sort implementation
    """

    def __init__(self, inputs=[]):

        # 1. main queue
        self.main_q = Queue(inputs)
        
        # 2. max length of input words
        self.max_len = 0
        for word in inputs:
            if len(word) > self.max_len:
                self.max_len = len(word)-1 # note -1 
        
        # 3. alphabet queues
        self.qs = {}
        self.ALPHABETS_W_BEGSPACE = ' abcdefghijklmnopqrstuvwxyz'
        for sym in self.ALPHABETS_W_BEGSPACE:
            self.qs[sym] = Queue()

    def char_at(self, s, pos):
        if pos <= len(s)-1:
            return s[pos]
        return ' '

    def sort(self):
        """ RADIX SORT (Exploits Queues)
        
        - for every idx from >>end to 0<< in max-lengthed word
        - for every WORD in main queue (EMPTY MAIN QUEUE, FILL Qs)
            - get the CHAR at cur idx (or pos)
            - deque THE WORD and enque into qs based on CHAR
        - Begining with space, in alphabetic order, Deque all Qs until empty
            + (EMPTY Qs, FILL MAIN QUEUE)
            + (MAIN QUEUE SORTED FROM END TO IDX)
                + Hence called radix sort, cz, comes from end to beg
        """
        
        # for every idx from >>end to 0<<  
        # in max-lengthed word
        for pos in range(self.max_len, -1, -1):

            # for every word in main queue.
            # --------------------------------------------
            # >> beg of this loop: qs empty & main_q fulll
            # >> end of this loop: qs fulll & main_q empty
            for _ in range(0, len(self.main_q)):

                # - get the char at "cur pos idx" (in iteration from end to beg)
                # - based on char
                #       - deque the word form main queue 
                #       - enqueue same word into qs
                word        = self.main_q.dequeue()
                cur_char    = self.char_at(word, pos)
                
                print('pos: ', pos)
                print('word: ',word)
                print('cur char: ', cur_char)
                
                self.qs[cur_char].enqueue(word)
            
            # print('space: ',self.qs[' ']._list)
            # print('m:', self.qs['m']._list)
            # print('n:', self.qs['n']._list)

            # starting from space, in alphbetic order,
            # deque all queues in qs into main_q.
            # main_q is sorted iterativey
            # --------------------------------------------
            # >> beg of this loop: qs fulll & main_q empty
            # >> end of this loop: qs empty & main_q full 
            for sym in self.ALPHABETS_W_BEGSPACE:
                if self.qs[sym].isempty():
                    continue
                while self.qs[sym].isempty() is not True:
                    self.main_q.enqueue(self.qs[sym].dequeue())
            
            print(self.main_q._list)

if __name__ == '__main__':
    """
    Using Queues to sort strings lexiographically!
    """
    inputs = ['bat', 'farm', 'barn', 'car', 'hat', 'cat']
    rs = RadixSort(inputs)
    rs.sort()