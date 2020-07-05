class numSubMatricesSumDivisibleByP:
    def __init__(self, M, N, P, matrix):
        self.rows   = M
        self.cols   = N
        self.P      = P
        self.matrix = matrix

    def brute(self):
        sum = 0
        cntr = 0
        
        # O(n^4)
        
        return cntr


if __name__ == '__main__':
    matrix = []
    M, N, P = list(map(int,input().split()))
    for _ in range(0, M):
        row = list(map(int,input().split()))
        matrix.append(row)

    soln = numSubMatricesSumDivisibleByP(M, N, P, matrix)
    print(soln.brute())
    