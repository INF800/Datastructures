class isPalindrome:
    def __init__(self, S):
        self.s = S

    def solve(self):
        _size = len(self.s)
        
        if _size%2:
            lcur_end = _size//2 # not inclusive
            rcur_end = _size//2 # inclusive
        else:
            lcur_end = _size//2 # not inclusive
            rcur_end = (_size//2)+1 #inclusive

        lcur = 0
        rcur = _size-1
        while (lcur < lcur_end) and (rcur>=rcur_end):
            if self.s[lcur] != self.s[rcur]:
                return 'NO'
            lcur += 1
            rcur -= 1
        return 'YES'

if __name__ == '__main__':
    S = str(input())
    soln = isPalindrome(S)
    print(soln.solve())