from copy import deepcopy
import math

# -------------------------------
# start class board
# -------------------------------

class Board:
    def __init__(self, mat=[['','',''],['','',''],['','','']]):#[['o','o','x'],['o','o','x'],['x','','']]):
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
        hmap = {
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
                if self.mat[i][j] == '' : hmap[f'{i}{j}'] = ' '
                else: hmap[f'{i}{j}'] = self.mat[i][j]
        
        print(f'\n[{hmap["00"]}][{hmap["01"]}][{hmap["02"]}]\n[{hmap["10"]}][{hmap["11"]}][{hmap["12"]}]\n[{hmap["20"]}][{hmap["21"]}][{hmap["22"]}]\n')

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

    # base condition: returns prob of maximizing player winning
    # -1 / 0 / +1
    if board.winner() != None:
        stat = board.winner()
        return stat

    # else, recur into score
    if isMaximizingPlayer is True:
        x_moves     = board.all_row_major_empty_moves()
        maxScore    = -math.inf
        bestMove    = None

        for (i, j) in x_moves:
            board.update(i, j, 'x')
            score = minimax(board, depth+1, not isMaximizingPlayer)
            if score > maxScore:
                maxScore  = score
                bestMove  = (i, j)
            # log
            if depth==0: print(f'---move: {i},{j} \t score: {score} \t best_score: {maxScore} \t {board.show()}')
            board.update(i, j, '')
        
        # return differently for top most recursion call(as we need data)
        if depth==0: return bestMove, maxScore
        return maxScore

    elif isMaximizingPlayer is False:
        o_moves     = board.all_row_major_empty_moves()
        minScore    = +math.inf
        bestMove    = None

        for (i, j) in o_moves:
            board.update(i, j, 'o')
            score = minimax(board, depth+1, not isMaximizingPlayer)
            if score < minScore:
                minScore  = score
                bestMove  = (i, j)
            if depth==1: print(f'move: {i},{j} \t score: {score} \t best_score: {minScore} \t {board.show()}')        
            board.update(i, j, '')
        return minScore

def retBestMove(board):
    board_copy  = Board(deepcopy(board.mat))

    bestMove, bestScore = minimax(board_copy, 0, True)
    return bestMove, bestScore



if __name__ == '__main__':
    board = Board()

    # [ ][ ][ ]
    # [ ][ ][ ]
    # [ ][ ][o]
    #board.update(2,2, 'o')
    
    #board.show()
    #print(minimax(board, 0, True))

    
    # [x][ ][o]
    # [ ][o][ ]
    # [ ][ ][ ]
    board.update(1,1,'o')
    board.update(0,0,'x')
    board.update(0,2,'o')
    board.show()

    print(retBestMove(board))
    
    '''
    iter = 0
    while iter<8:
        board.show()
        
        _i, _j = list(map(lambda x: int(x), input().split()))
        board.update(_i, _j, 'o')

        (i, j), score = retBestMove(board)
        board.update(i, j, 'x')

        iter += 1
    '''