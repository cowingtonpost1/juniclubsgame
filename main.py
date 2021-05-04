import pygame

successes, failures = pygame.init()
print("Initializing pygame: {0} successes and {1} failures.".format(successes, failures))

screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load('alien.png')
        self.rect = self.image.get_rect()  # Get rect of some size as 'image'.
        self.x = x
        self.y = y
    def update(self):
        screen.blit(self.image, (self.x, self.y))


player = Player(0,0)
running = True
while running:
    screen.blit(pygame.image.load('background.png'), (0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player.y -= 15# 200 pixels per second
            elif event.key == pygame.K_s:
                player.y += 15
            elif event.key == pygame.K_a:
                player.x  -= 15
            elif event.key == pygame.K_d:
                player.x += 15

    player.update()

    pygame.display.update()  # Or pygame.display.flip()

print("Exited the game loop. Game will quit...")
quit()  # Not actually necessary since the script will exit anyway.

