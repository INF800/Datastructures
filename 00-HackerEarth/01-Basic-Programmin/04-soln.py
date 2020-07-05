class Solution:
    def __init__(self, l, r, k):
        self.l = l
        self.r = r
        self.k = k

    def solve(self):
        cntr = 0 
        for i in range(l, r+1):
            if i%self.k == 0: cntr += 1
        return cntr    


if __name__ == '__main__':
    l, r, k = list(map(int,input().split()))
    soln = Solution(l,r,k)
    print(soln.solve())