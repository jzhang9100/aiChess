import os
import chess.pgn
from AIgame import State
import  numpy as np

def get_training_data():
    X_train, y_train = [], []
    # pgn files from games of GM Vassily Ivanchuk and GM Gary Kasparov
    gamenum = 0
    dir = 'D:\\AIGameProject\\Games\\'
    for file in os.listdir(dir):
        pgn = open(os.path.join(dir, file))
        print(pgn)
        while 1:
            try:
                game = chess.pgn.read_game(pgn)
                result = game.headers["Result"]
                value = {'1-0': 1, '0-1': -1, '1/2-1/2': 0}[result]
                board = game.board()
                print("parsing game %d" % gamenum)
                gamenum += 1
            except Exception:
                break

            for moveNum, move in enumerate(game.mainline_moves()):
                board.push(move)
                print(move)
                
                serialize = State(board).serialize()#[:, :, 0]
                X_train.append(serialize)
                y_train.append(value)
            break
        break
    X_train = np.array(X_train)
    y_train = np.array(y_train)
    return X_train, y_train

if __name__ == "__main__":
    #save training data
    X_train, y_train = get_training_data()
    np.savez("D:\\AIGameProject\\dataset\\trainedData", X_train, y_train)