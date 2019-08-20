import pygame

Background_BOARD = []
for i in range(63):
    Background_BOARD.append(i)

class gui:
    def __init__(self):
        pygame.init()
        #represent 8x8 chess board as array from 0-63
        self.board = Background_BOARD
        self.screen = pygame.display.set_mode((625, 625))
        pygame.display.set_caption("Chess")

        #load image and resize to set as background
        self.background = pygame.image.load('gui_images//chess_board.png').convert()
        self.background = pygame.transform.scale(self.background, (600,600))
        self.screen.blit(self.background, (0,0))
        pygame.display.update()
        pygame.time.delay(100)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break