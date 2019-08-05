# Chess States
import chess
import numpy as np
from minimax import Minimax

if __name__ == '__main__':
    board = chess.Board()
    while not board.is_game_over():
        if(board.turn):
            print(list(board.legal_moves))
            move = input("User Move: ")
            board.push(chess.Move.from_uci(move))
            print(board)
        else:
            m = Minimax(board)
            print("AI move:")
            aiMove = m.get_Move()
            print(aiMove)
            board.push(chess.Move.from_uci(str(aiMove)))
            print(board)