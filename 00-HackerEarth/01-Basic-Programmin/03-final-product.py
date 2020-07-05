class FinalProduct:
    def __init__(self, A, N):
        self.arr = A
        self.size = N

    def solve(self):
        ans = 1
        for idx in range(0, self.size):
            cur = self.arr[idx]
            ans = (ans*cur) % (pow(10,9)+7)
        return ans



if __name__ == '__main__':
    N = int(input())
    A = list(map(int,input().split()))
    
    soln = FinalProduct(A, N)
    print(soln.solve())