class numSubMatricesSumDivisibleByP:
    def __init__(self, M, N, P, matrix):
        self.rows   = M
        self.cols   = N
        self.P      = P
        self.matrix = matrix

    def brute0(self):
        '''
        TIME        : O(n^4)
        '''
        n_sub_mat_sum_div_by_p = 0

        for r in range(0, self.rows):
            for c in range(0, self.cols): 
                for br in range(r, self.rows): # row cur
                    for bc in range(c, self.cols): # col cursor

                        # total (m)(m+1)(n)(n+1)/ 4 submatrices = 36 sub matrices for 3x3
                        #print(f'top idx:({r}, {c}) \t  bottom idx:({br}, {bc})')
                        sum = 0
                        for row in range(r, br+1):
                            for col in range(c, bc+1):
                                sum += self.matrix[row][col]
                        #print('sum: ', sum) 
                        if sum%self.P == 0:
                            n_sub_mat_sum_div_by_p += 1
        
        return n_sub_mat_sum_div_by_p

    
    def eff(self):
        '''
        TIME        : O(n^3)
        '''
        pass


if __name__ == '__main__':
    '''
    3 3 99
    1 2 3
    4 5 6
    7 8 9
    '''
    matrix = []
    M, N, P = list(map(int,input().split()))
    for _ in range(0, M):
        row = list(map(int,input().split()))
        matrix.append(row)

    soln = numSubMatricesSumDivisibleByP(M, N, P, matrix)
    
    print(soln.brute0())