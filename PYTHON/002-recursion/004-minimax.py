from copy import deepcopy

# -------------------------------
# start class board
# -------------------------------

class Board:
    def __init__(self, mat=[['','',''],['','',''],['','','']]):
        self.mat = mat
    
    def size(self):
        size = 0
        for i in range(0, 3):
            for j in range(0, 3):
                if self.mat[i][j] != '' : size += 1
        return size

    def update(self, i, j, val):
        self.mat[i][j] = val

    def reset(self):
        self.mat = [['','',''],['','',''],['','','']]

    def show(self):
        map = {
            '00' : None,
            '01' : None,
            '02' : None,
            '10' : None,
            '11' : None,
            '12' : None,
            '20' : None,
            '21' : None,
            '22' : None,
        }

        for i in range(0, 3):
            for j in range(0,3):
                if self.mat[i][j] == '' : map[f'{i}{j}'] = ' '
                else: map[f'{i}{j}'] = self.mat[i][j]
        
        print(f'\n[{map["00"]}][{map["01"]}][{map["02"]}]\n[{map["10"]}][{map["11"]}][{map["12"]}]\n[{map["20"]}][{map["21"]}][{map["22"]}]\n')

    @staticmethod
    def __id(xo):
        if xo=='x': return 1
        if xo=='o': return -1

    def winner(self):
        """
        - x     : +1
        - o     : -1
        - tie   : 0 (SIZE==9)
        - wip   : null 
        """
        # check rows & cols
        for i in range(0, 3):
            if (self.mat[i][0] == self.mat[i][1]) and (self.mat[i][0] == self.mat[i][2]) and (self.mat[i][0] != ''):
                return Board.__id(self.mat[i][0])
            if (self.mat[0][i] == self.mat[1][i]) and (self.mat[0][i] == self.mat[2][i]) and (self.mat[0][i] != ''):
                return Board.__id(self.mat[0][i])

        # check principal diag
        if (self.mat[0][0] == self.mat[1][1]) and (self.mat[0][0] == self.mat[2][2]) and (self.mat[0][0] != ''):
            return Board.__id(self.mat[0][0])
        
        # check non-principal diag
        if (self.mat[0][2] == self.mat[1][1]) and (self.mat[0][2] == self.mat[2][0]) and (self.mat[0][2] != ''):
            return Board.__id(self.mat[0][2])

        # else, check tie
        if board.size() == 9: return 0

        # esle, game in progress
        return None

    def all_row_major_empty_moves(self):
        empty_moves = []
        for i in range(0, 3):
            for j in range(0, 3):
                if self.mat[i][j] == '' : empty_moves.append((i, j))
        return empty_moves

# -------------------------------
# end class board
# -------------------------------

def minimax(board, depth, isMaximizingPlayer):
    # base condition: returns score
    if board.winner() != None:
        score = board.winner()
        #print(score)
        #board.reset()
        return score

    # else, recur into score
    if isMaximizingPlayer == True:
        x_moves = board.all_row_major_empty_moves()
        bestScore = -999999999999999999
        for (i, j) in x_moves:
            board.update(i, j, 'x')
            score = minimax(board, depth+1, not isMaximizingPlayer)
            if score > bestScore:
                bestScore = score
            board.update(i, j, '')
        return bestScore

    if isMaximizingPlayer == False:
        o_moves = board.all_row_major_empty_moves()
        bestScore = 999999999999999999
        for (i, j) in o_moves:
            board.update(i, j, 'o')
            score = minimax(board, depth+1, not isMaximizingPlayer)
            if score < bestScore:
                bestScore = score
            board.update(i, j, '')
        return bestScore

def retBestMove(board):
    boardCopy = Board(deepcopy(board.mat))
    moves = board.all_row_major_empty_moves()

    bestScore = -999999999999999999
    bestRow, bestCol = None, None
    for (i, j) in moves:
        score = minimax(boardCopy, depth=0, isMaximizingPlayer=True)
        if score > bestScore:
            bestScore   = score
            bestRow     = i
            bestCol     = j
    
    return bestRow, bestCol, bestScore

if __name__ == '__main__':
    board = Board()

    # [ ][ ][ ]
    # [ ][ ][ ]
    # [ ][ ][o]
    #board.update(2,2, 'o')
    #board.show()

    iter = 0
    while iter<9:
        board.show()
        
        _i = int(input())
        _j = int(input())
        board.update(_i, _j, 'o')

        i, j, score = retBestMove(board)
        board.update(i, j, 'x')

        iter += 1