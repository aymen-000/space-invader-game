import pygame as pg #----get pygame as pg ----------
import random
import math
score = 0
#********************************intit pygame*****************
pg.init()
screen = pg.display.set_mode((800, 600))
pg.display.set_caption('Space Invaders ')
image = pg.image.load('spaceship(1).png')
pg.display.set_icon(image)
playerimg = pg.image.load('space-invaders.png')
enemyimg = pg.image.load('space.png')
background = pg.image.load('5438748.jpg')
bulett = pg.image.load('bullet.png')
#******************************variables used in the code *********************
playerx = 370
playery = 480
buletty = playery
bulettx = playerx+14 #*****to make the bullet under the spaceship
bulettychange =0.5 # move bulette by 0.5px
bulett_state = 'ready'
images = ['alien(1).png', 'alien(2).png', 'alien(3).png', 'space.png', 'space.png', 'alien(3).png']
changx = 0
changy = 0
textx =10
texty =10

enemyimg = []
enemyx = []
enemyy = []
movex = []
movey = []
num_of_enemy = 6
#fill the listes above
for i in range(num_of_enemy):
    enemyimg.append(pg.image.load(images[i]))
    enemyx.append(random.randint(0, 736))
    enemyy.append(random.randint(0, 350))
    movex.append(0.3)
    movey.append(40)
# player function : is to draw the image of the spaceship and update it for every movement
def player(x, y):
    screen.blit(playerimg, (x, y))


#enemy function is to draw the enemy image and update it for every movement
def enemy(enemyimg,x,y ):
    screen.blit(enemyimg, (x, y))


# iscollision is to know the distance between the enemy and the bullet
def isCollision(enemyx, enemyy, z, t):
    xdistance   = math.pow(enemyx-z, 2)
    ydistance = math.pow(enemyy-t, 2)
    distance = math.sqrt(xdistance+ydistance)
    if distance <= 27:
        return True
    else:
        return False


# this function is to know the distance between the player and the enemy
def player_enemy(enemyx, enemy, playerx, playery):
    distance = math.sqrt( math.pow(enemy - playery, 2)+math.pow(enemyx-playerx,2))
    if distance <40  :
        return True
    else:
        return False


#this function is to draw the bullete and update it
def bulletready(x, y):
    global bulett_state
    bulett_state='fire'
    screen.blit(bulett, (x+14, y))


runing = True



#**************************************start the game looop *************************
while runing:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pg.event.get():
        if event.type == pg.QUIT:
            runing = False
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                runing = False
            if event.key == pg.K_LEFT:
                changx = -1
            if event.key == pg.K_RIGHT:
                changx = 1
            if event.key == pg.K_SPACE:
                bulletready(playerx, playery)
        if event.type == pg.KEYUP:
            if event.key == pg.K_LEFT or event.key == pg.K_RIGHT:
                changx = 0
    x = playerx #save the old position of player to use it before
    playerx = changx + playerx
    if playerx > 736:
        playerx = 736
    elif playerx <= 0:
        playerx = 0
    for i in range(num_of_enemy):
        enemyy[i] = enemyy[i] + movex[i]
        if enemyy[i] >= 600:
            enemyy[i] = 0
        if bulett_state is 'fire':
            buletty = buletty - bulettychange
            bulletready(x, buletty)
            if isCollision(enemyx[i], enemyy[i], x, buletty):
                score = score + 1
                bulett_state ='ready' #to stop the bullet moving
                buletty = playery
                enemyy[i] = 0
                enemyx[i] = random.randint(0, 800)
                print(score)#just for testing (not important)
        if buletty <= 0:
            buletty = playery
            bulett_state = 'ready'

        if player_enemy(enemyx[i], enemyy[i], playerx, playery):
            print('game over')
            runing = False
        enemy(enemyimg[i],enemyx[i],enemyy[i])
    player(playerx, playery)
    pg.display.update()