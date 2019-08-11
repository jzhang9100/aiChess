#Hand Coded Openings for the AI to randomly play
import random as rndm

class openingbook:
    def get_opening(self, board):
        b = board
        move = str(b.pop())
        def switch(move):
            s = {
                #known openings against e4
                "e2e4": [self.french_defense(), self.sicilian_defense(),
                         self.kings_pawn(), self.caro_kann()],
                #known openings against d4
                "d2d4": [self.queens_gambit_declined(), self.indian_game(), self.horwitz_defence()]
            }
            return s.get(move, "kings_indian_attack") #if not e4 or d4, go into kings indian attack
        poss_openings = switch(move)

        if(poss_openings == "kings_indian_attack"):
            return self.kings_indian_attack()
        else:
            i = rndm.randint(0, len(poss_openings)-1)
            opening = poss_openings[i]
            return opening

    def kings_indian_attack(self):
        moveList = ["d7d5", "g8f6", "c7c6"]
        return moveList

    def french_defense(self):
        moveList = ["e7e6", "d7c5"]
        return moveList

    def sicilian_defense(self):
        moveList = ["c7c5", "d7d6", "g8f6"]
        return moveList

    def kings_pawn(self):
        moveList = ["e7e5", "b8c6"]
        return moveList

    def caro_kann(self):
        moveList = ["c7c6", "d7d5"]
        return moveList

    def queens_gambit_declined(self):
        moveList = ["d7d5", "e7e6"]
        return moveList

    def indian_game(self):
        moveList = ["g8f6", "e7e6"]
        return moveList

    def horwitz_defence(self):
        moveList = ["e7e6", "g8f6"]
