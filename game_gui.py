import pygame

RANK_8 = 7
RANK_7 = 6
RANK_6 = 5
RANK_5 = 4
RANK_4 = 3
RANK_3 = 2
RANK_2 = 1
RANK_1 = 0

def gui_update():
    pygame.init()
    screen = pygame.display.set_mode((500, 500))
    screenbox = screen.get_rect()
    pygame.display.set_caption("Chess")

    # load image and resize to set as background
    background = pygame.image.load('gui_images//chess_board.png').convert()
    background = pygame.transform.scale(background, (500, 500))

    pawn = Pawn(True)
    pawn.rect.x = 0
    pawn.rect.y = 0

    piece_list = pygame.sprite.Group()
    piece_list.add(pawn)

    screen.blit(background, (0, 0))
    piece_list.draw(screen)
    pygame.display.update()
    pygame.time.delay(100)
    try:
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    break
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q or event.unicode == 'q':
                        break
    finally:
        pygame.quit()

class Pawn(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        if not color:
            self.image = pygame.image.load('gui_images//black_pieces//bP.png')
        else:
            self.image = pygame.image.load('gui_images//white_pieces//wP.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (63, 63))

class Rook(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        if not color:
            self.image = pygame.image.load('gui_images//black_pieces//bP.png')
        else:
            self.image = pygame.image.load('gui_images//white_pieces//wP.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (63, 63))

class Bishop(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        if not color:
            self.image = pygame.image.load('gui_images//black_pieces//bP.png')
        else:
            self.image = pygame.image.load('gui_images//white_pieces//wP.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (63, 63))

class Knight(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        if not color:
            self.image = pygame.image.load('gui_images//black_pieces//bP.png')
        else:
            self.image = pygame.image.load('gui_images//white_pieces//wP.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (63, 63))

class King(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        if not color:
            self.image = pygame.image.load('gui_images//black_pieces//bP.png')
        else:
            self.image = pygame.image.load('gui_images//white_pieces//wP.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (63, 63))

class Queen(pygame.sprite.Sprite):
    def __init__(self, color):
        pygame.sprite.Sprite.__init__(self)
        if not color:
            self.image = pygame.image.load('gui_images//black_pieces//bP.png')
        else:
            self.image = pygame.image.load('gui_images//white_pieces//wP.png')
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (63, 63))

