import math
import chess

ALPHA = -1000000
BETA = 1000000
#MiniMax with alpha beta pruning
class Minimax:
    def __init__(self, board = None):
        if board is None:
            self.board = chess.Board()
        else:
            self.board = board

    #run the minimax search and return the best move
    def get_Move(self):
        b = self.board
        moveDict = {}
        best_score, best_move = ALPHA, 0
        for move in b.legal_moves:
            b.push(move)
            score = self.MinimaxAlphaBeta(b, 3, False, ALPHA, BETA)
            #print(move, score)
            b.pop()
            moveDict[move] = score
            if(score >= best_score):
                best_score = score
                best_move = move
        print(moveDict)
        return best_move


    #minimax algorithim based on https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/
    def MinimaxAlphaBeta(self, board, depth, isMaximizing, alpha, beta):
        if(depth == 0):
            return self.evaluateBoard(board)
        if(isMaximizing):
            best_score = ALPHA
            for move in board.legal_moves:
                board.push(move)
                best_score = max(best_score, self.MinimaxAlphaBeta(board, depth-1, False, alpha, beta))
                board.pop()
                alpha = max(alpha, best_score)
                if(beta <= alpha):
                    break
            return best_score
        else:
            best_score = BETA
            for move in board.legal_moves:
                board.push(move)
                best_score = min(best_score, self.MinimaxAlphaBeta(board, depth-1, True, alpha, beta))
                board.pop()
                beta = min(beta, best_score)
                if (beta <= alpha):
                    break
            return best_score


    def evaluateBoard(self, board):
        score = 0
        for i in range(64):
            pp = board.piece_at(i)
            score += self.getPieceVal(board.piece_at(i))
        return score


    # returns piece worth: black = negative, white = positive
    def getPieceVal(self, piece) -> int:
        if piece != None:
            val = {"P": 800, "N": 2500, "B": 3000, "R": 4500, "Q": 9000, "K": 100000, \
                   "p": -800, "n": -2500, "b": -3000, "r": -4500, "q": -9000, "k": -100000}[piece.symbol()]
            return -val
        else:
            return 0