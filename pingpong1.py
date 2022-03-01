
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
        if self.rect.y > 0  and self.rect.y < 400:
            self.rect.y -= self.speed
        if self.rect.x > 0  and self.rect.x < 600:
            self.rect.x -= self.speed



kin1 = Player1("fyb.png",0,20,75,100,100)
kin2 = Player2("fyb.png",600,200,75,100,100)
Poos = Poo('POO.png',300,200, randint(5,12),100,100)


game = True
finish = False

while game: 
    for e in event.get():
        if e.type == QUIT:
            game = False
    if finish == False:
        window.blit(background,(0,0))
        if sprite.collide_rect(kin1, Poos):
            Poos.speed = Poos.speed * -1
        if sprite.collide_rect(kin2, Poos):
            Poos.speed = Poos.speed * -1
    window.blit(background,(0,0))
    kin1.reset()
    kin1.update()
    kin2.reset()
    kin2.update()
    Poos.reset()
    Poos.update()
    time.delay(15)
    display.update( )
