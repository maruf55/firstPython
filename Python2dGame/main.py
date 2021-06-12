import pygame
import random
import math
from pygame import mixer

pygame.init()  # initialize the pyGame

screen = pygame.display.set_mode((800, 600))  # create window
running = True

background = pygame.image.load("icons\\animatedSpace.jpg")
background = pygame.transform.scale(background, (800, 600))
bullet_image = pygame.image.load("icons\\bullet.png")

score_val = 0
font = pygame.font.Font('dragon.otf', 35)
textX = 10
textY = 10

pygame.display.set_caption('UFO Game')  # adding caption
icon = pygame.image.load("icons\\joystick.png")  # adding icon in window
pygame.display.set_icon(icon)

# player
playerImage = pygame.image.load("icons\\spaceship.png")  # player Image
playerX = 350
playerY = 500
playerX_change = 0
# playerY_change = 0

# enemy
enemyImage = []
enemyX = []
enemyY = []
enemyX_change = []
enemyY_change = []
numberOfEnemy = 8
for i in range(numberOfEnemy):
    enemyImage.append(pygame.image.load("icons\\monster.png"))  # enemy image
    enemyX.append(random.randint(0, 735))
    enemyY.append(random.randint(30, 150))
    enemyX_change.append(1)
    enemyY_change.append(30)

# Bullet
bulletX = 350
bulletY = 480
# bulletX_change = 0
bulletY_change = 4
bullet_state = "ready"


def player(x, y):
    screen.blit(playerImage, (x, y))  # position of player on the screen


def showscore(x, y):
    score = font.render("Score: " + str(score_val), True, (192, 192, 192))
    screen.blit(score, (x, y))


def enemy(x, y, i):
    screen.blit(enemyImage[i], (x, y))  # position of enemy on the screen


def bullet_fire(x, y):
    global bullet_state
    bullet_state = 'fire'
    screen.blit(bullet_image, (x + 20, y + 10))


def iscollision(enemyX, enemyY, bulletX, bulletY):
    distance = math.sqrt((math.pow(enemyX - bulletX, 2) + math.pow(enemyY - bulletY, 2)))
    if distance < 28:
        return True
    else:
        return False


game_over_font = pygame.font.Font("dragon.otf", 90)


def gameover():
    game = game_over_font.render("GAME OVER", True, (0, 255, 0))
    screen.blit(game, (185, 250))


while running:  # game loop
    # filling the screen with a RGB color
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                playerX_change = -4
            elif event.key == pygame.K_d:
                playerX_change = 4
            if event.key == pygame.K_SPACE:
                if bullet_state == 'ready':
                    bulletX = playerX
                    bullet_fire(bulletX, bulletY)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a or event.key == pygame.K_d:
                playerX_change = 0

    # player boundaries check
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    if playerX >= 736:
        playerX = 736

    # enemy boundaries check
    for i in range(numberOfEnemy):
        if enemyY[i] > 450:
            for j in range(numberOfEnemy):
                enemyY[j] = 2000
            gameover()
            break

        enemyX[i] += enemyX_change[i]
        if enemyX[i] <= 0:
            enemyX_change[i] = 1
            enemyY[i] += enemyY_change[i]
        elif enemyX[i] >= 736:
            enemyX_change[i] = -1
            enemyY[i] += enemyY_change[i]
        collision = iscollision(enemyX[i], enemyY[i], bulletX, bulletY)
        if collision:
            bulletY = 480
            bullet_state = 'ready'
            score_val += 1
            enemyX[i] = random.randint(0, 735)
            enemyY[i] = random.randint(30, 150)
        enemy(enemyX[i], enemyY[i], i)
    if bulletY <= 0:
        bulletY = 480
        bullet_state = 'ready'

    if bullet_state == 'fire':
        bullet_fire(bulletX, bulletY)
        bulletY -= bulletY_change

    player(playerX, playerY)
    showscore(textX, textY)
    pygame.display.update()
