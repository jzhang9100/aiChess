#!/bin/usr/python3
import chess
from minimax import Minimax
from OpeningBook import openingbook

if __name__ == '__main__':
    board = chess.Board()
    o = openingbook()
    moveNum = 0
    openingLength = 0
    opening = []

    while not board.is_game_over():
        if (board.turn):
            print(board)
            print(list(board.legal_moves))
            move = input("User Move: ")
            board.push(chess.Move.from_uci(move))
            if (moveNum == 0):
                opening = o.get_opening(board)
                openingLength = len(opening)
        else:
            print(board)
            if (moveNum < openingLength):
                openingMove = opening[moveNum]
                print("AI move:", openingMove)
                board.push(chess.Move.from_uci(openingMove))
            else:
                m = Minimax(board)
                aiMove = m.get_Move()
                print("AI move: ", aiMove)
                board.push(chess.Move.from_uci(str(aiMove)))
            moveNum += 1
