
from pygame import *
from random import randint

window = display.set_mode((700,500))
display.set_caption("Pingpong game")
background = transform.scale(image.load("table.jpg"),(700,500))
mixer.init()    
mixer.music.load('space.ogg')
mixer.music.play()
mixer.music.set_volume(0.3)


class GameSprite(sprite.Sprite):
    def __init__(self, player_image, player_x, player_y, player_speed,size_x,size_y):
        super().__init__()
        self.image = transform.scale(image.load(player_image),(size_x,size_y))
        self.rect = self.image.get_rect()
        self.speed = player_speed
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x,self.rect.y))

poos = sprite.Group()

class Player1(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= 10
        if keys[K_s] and self.rect.y < 400:
            self.rect.y += 10

class Player2(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= 10
        if keys[K_DOWN] and self.rect.y < 400:
            self.rect.y += 10

class Poo(GameSprite):
    def update(self):
        pass



kin1 = Player1("fyb.png",0,200,75,100,100)
kin2 = Player2("fyb.png",600,200,75,100,100)
Poos = Poo('POO.png',300,200, randint(5,12),50,50)
speed_x = 3
speed_y = 3

game = True
finish = False
font.init()
font1 = font.SysFont('Arial', 35)
lose1 = font1.render("PLAYER 1 LOSE AWWWWW", True, (180, 0, 0))
font2 = font.SysFont('Arial', 35)
lose2 = font1.render("PLAYER 2 LOSE HAHAHA", True, (180, 0, 0))

while game: 
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == False:
        window.blit(background,(0,0))
        if sprite.collide_rect(kin1, Poos):
            speed_x = randint(-20,-10)
            speed_x *= -1
        if sprite.collide_rect(kin2, Poos):
            speed_x = randint(10,20)
            speed_x *= -1
        Poos.rect.x += speed_x
        Poos.rect.y += speed_y
        if Poos.rect.y > 450 or Poos.rect.y < 0:
            speed_y *= -1
        if Poos.rect.x < -100   :
            finish = True
            window.blit(lose1, (200,200))
        if Poos.rect.x > 700:
            finish = True
            window.blit(lose2, (200,200))
        #window.blit(background,(0,0))
        kin1.reset()
        kin1.update()
        kin2.reset()
        kin2.update()
        Poos.reset()
        Poos.update()
        time.delay(15)
        display.update( )
