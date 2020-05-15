import pygame
from math import pi, cos, sin, hypot


width, height = 640, 480


def main():
    running = True
    background_color = (0, 0, 10)
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Space Invaders")
    screen.fill(background_color)
    pygame.display.update()

    while running:
        events = pygame.event.get()

        for event in events:

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    running = False

            if event.type == pygame.QUIT:
                running = False

        screen.fill(background_color)  # start
        # in between code

        EnemySpaceship.update_direction()

        for enemy in enemies:
            enemy.move()

        for enemy in enemies:
            enemy.draw()

        EnemySpaceship.ALL_SPRITES.draw(screen)

        pygame.display.update()  # end


class EnemySpaceship:
    # image
    ALL_SPRITES = pygame.sprite.Group()
    IMG = pygame.image.load("spaceship.png")

    # graphics
    WIDTH = IMG.get_width()
    HEIGHT = IMG.get_height()
    X_DISTANCE_BETWEEN_SHIPS = WIDTH + 20
    Y_DISTANCE_BETWEEN_SHIPS = HEIGHT
    OFFSET_X = - 100
    OFFSET_Y = 10

    # movements
    LIST_OF_ANGLES = [0, pi/2, pi, pi/2]
    COUNTER = 0
    ANGLE = LIST_OF_ANGLES[COUNTER]

    DISTANCE = 0
    MAX_DISTANCE_X = 80
    MAX_DISTANCE_Y = 20
    LIST_MAX_DISTANCE = [MAX_DISTANCE_X, MAX_DISTANCE_Y]
    DISTANCE_COUNTER = 0
    VELOCITY = 1 / 8
    V_X = VELOCITY * cos(ANGLE)
    V_Y = VELOCITY * sin(ANGLE)

    @staticmethod
    def update_direction():
        EnemySpaceship.DISTANCE += hypot(EnemySpaceship.V_X, EnemySpaceship.V_Y)
        if EnemySpaceship.DISTANCE >= EnemySpaceship.LIST_MAX_DISTANCE[EnemySpaceship.DISTANCE_COUNTER]:
            EnemySpaceship.DISTANCE = 0

            if EnemySpaceship.COUNTER >= len(EnemySpaceship.LIST_OF_ANGLES) - 1:
                EnemySpaceship.COUNTER = 0
            else:
                EnemySpaceship.COUNTER += 1

            EnemySpaceship.ANGLE = EnemySpaceship.LIST_OF_ANGLES[EnemySpaceship.COUNTER]
            EnemySpaceship.V_X = EnemySpaceship.VELOCITY * cos(EnemySpaceship.ANGLE)
            EnemySpaceship.V_Y = EnemySpaceship.VELOCITY * sin(EnemySpaceship.ANGLE)

            # update distance counter
            if EnemySpaceship.DISTANCE_COUNTER == 0:
                EnemySpaceship.DISTANCE_COUNTER = 1
            else:
                EnemySpaceship.DISTANCE_COUNTER = 0

    def __init__(self, index_x, index_y):
        self.index_x = index_x
        self.index_y = index_y
        self.x = EnemySpaceship.X_DISTANCE_BETWEEN_SHIPS * self.index_x + EnemySpaceship.OFFSET_X
        self.y = EnemySpaceship.Y_DISTANCE_BETWEEN_SHIPS * self.index_y + EnemySpaceship.OFFSET_Y

        self.color = (30, 30, 80)

        self.sprite = pygame.sprite.Sprite(EnemySpaceship.ALL_SPRITES)
        self.sprite.image = EnemySpaceship.IMG
        self.sprite.rect = self.sprite.image.get_rect()

    def draw(self):
        pass

    def move(self):
        self.x += EnemySpaceship.V_X
        self.y += EnemySpaceship.V_Y

        self.sprite.rect.x = int(self.x)
        self.sprite.rect.y = int(self.y)


enemies = []
for x in range(16):
    for y in range(8):
        enemies.append(EnemySpaceship(x, y))


if __name__ == '__main__':
    main()
