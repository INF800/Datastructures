from utility import Queue

class RadixSort:

    def __init__(self, inputs=[]):
        # 1. main queue
        self.main_q = Queue(inputs)
        # 2. max length of input words
        self.max_len = 0
        for word in inputs:
            if len(word) > self.max_len:
                self.max_len = len(word)-1
        # 3. alphabet queues
        self.qs = {}
        alphabets = ' abcdefghijklmnopqrstuvwxyz'
        for sym in alphabets:
            self.qs[sym] = Queue()

    def char_at(self, s, pos):
        if pos <= len(s)-1:
            return s[pos]
        return ' '

    def sort(self):
        for pos in range(self.max_len, -1, -1):
            for _ in range(0, len(self.main_q)):
                word        = self.main_q.dequeue()
                print(word)
                cur_char    = self.char_at(word, pos)
                print('cur char: ', cur_char)
                self.qs[cur_char].enqueue(word)
            
            print('space: ',self.qs[' ']._list)
            print('m:', self.qs['m']._list)
            print('n:', self.qs['n']._list)

            for sym in ' abcdefghijklmnopqrstuvwxyz':
                ret = self.qs[sym].dequeue()
                if ret != 'Queue is empty':
                    self.main_q.enqueue( ret )
            
            print(self.main_q._list)

if __name__ == '__main__':
    """
    Using Queues to sort strings lexiographically!
    """
    inputs = ['cat', 'hat', 'car', 'barn', 'farm', 'bat']
    rs = RadixSort(inputs)
    rs.sort()