import chess
from minimax import Minimax

if __name__ == '__main__':
    board = chess.Board()
    moveNum = 0
    while not board.is_game_over():
        if(board.turn):
            print(board)
            print(list(board.legal_moves))
            move = input("User Move: ")
            board.push(chess.Move.from_uci(move))
        else:
            print(board)

            #force AI to play sicilian defence
            if(moveNum == 0):
                sicilianMove1 = "c7c5"
                print("AI move:")
                print(sicilian)
                board.push(chess.Move.from_uci(sicilian))
            elif(moveNum == 1):
                sicilianMove2 = "d7d6"
                print("AI move:")
                print(sicilian)
                board.push(chess.Move.from_uci(sicilian))
            #run minimax
            else:
                m = Minimax(board)
                print("AI move:")
                aiMove = m.get_Move()
                print(aiMove)
                board.push(chess.Move.from_uci(str(aiMove)))
            moveNum+=1
