#Hand Coded Openings for the AI to play
import random as rndm

class OpeningBook:
    def get_opening(self, board):
        move = str(board.pop())
        def switch(move):
            s = {
                #known openings against e4
                "e2e4": ["french_defense", "sicilian_defense", "kings_pawn", "scandinavian_defense", "caro_kann"],
                #known openings against d4
                "d2d4": ["queens_pawn", "indian_game", "horwitz_defense"]
            }
            return s.get(move, "kings_indian_attack") #if not e4 or d4, go into kings indian attack
        poss_openings = switch(move)

        if(poss_openings == "kings_indian_attack"):
            return self.kingsIndianAttack()
        else:
            i = rndm.randint(0, len(poss_openings)-1)
            opening = poss_openings[i]

    def kingsIndianAttack(self):
        moveList = ["d7d5", "g8f6", "c7c6"]
        return moveList

    def