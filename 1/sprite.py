import pygame
import random

SCREEN_RECT                       =  pygame.Rect(0,0,480,700)
CREATE_EVENT                      =  pygame.USEREVENT
ENEMY_EVENT                       =  pygame.USEREVENT + 1
enemyList                         =  {}

class GameSprite(pygame.sprite.Sprite):
    
    def __init__(self,imageName,speed = 1):
        super().__init__()
        self.image                =  pygame.image.load(imageName)
        self.rect                 =  self.image.get_rect()
        self.speed                =  speed

    def update(self):
        self.rect.y              +=  self.speed


class Start(pygame.sprite.Sprite):
    def __init__(self,imageName):
        super().__init__()
        self.image                =  pygame.image.load(imageName)
        self.rect                 =  self.image.get_rect()
        self.rect.top             =  SCREEN_RECT.height/2*1/3 + SCREEN_RECT.height/2
        self.rect.centerx         =  SCREEN_RECT.centerx


class Pause(pygame.sprite.Sprite):
    def __init__(self,imageName):
        super().__init__()
        self.image                =  pygame.image.load(imageName)
        self.rect                 =  self.image.get_rect()
        self.rect.top             =  SCREEN_RECT.height/2*2/3 + SCREEN_RECT.height/2
        self.rect.centerx         =  SCREEN_RECT.centerx


class BackGround(GameSprite):
    
    def update(self):
        super().update()
        self.bullets              =  Bullet('imagine/bullet1.png')
        self.bullets.rect.centerx =  self.rect.centerx
        self.bullets.rect.top     =  self.rect.bottom + 5 
        if self.rect.y           >=  SCREEN_RECT.height:
            self.rect.y           =  -self.rect.height


class Enemy(GameSprite):
    def __init__(self,imageName):
        super().__init__(imageName)
        self.speed                =  random.randint(1,3)
        self.rect.bottom          =  0
        self.rect.x               =  random.randint(0,SCREEN_RECT.width - self.rect.width)
        # self.enemyBullet          =  pygame.sprite.Group()
        
    
    def update(self):
        super().update()
        if self.rect.y >= SCREEN_RECT.height:
            self.kill()
    def shoot(self):
        pass
        #self.bullets              =  Bullet('imagine/bullet1.png')
        #self.bullets.rect.centerx =  self.rect.centerx
        #self.bullets.rect.top     =  self.rect.bottom + 5 
        # self.enemyBullet.add(self.bullets)


class Hero(GameSprite):
    def __init__(self,imageName):
        super().__init__(imageName,0)
        self.rect                 =  self.image.get_rect()
        self.rect.bottom          =  SCREEN_RECT.bottom
        self.rect.centerx         =  SCREEN_RECT.centerx
        self.bullet               =  pygame.sprite.Group()

    def update(self):
        self.rect.x              +=  self.speed
        if self.rect.x           <=  0:
            self.rect.x           =  0
        elif self.rect.x         >=  SCREEN_RECT.width - self.rect.width:
            self.rect.x           =  SCREEN_RECT.width - self.rect.width

    def shoot(self):
        self.egg                  =  Bullet('imagine/bullet.png')
        self.egg1                 =  Bullet('imagine/bullet.png')
        self.egg.rect.centerx     =  self.rect.left + 16
        self.egg1.rect.centerx    =  self.rect.right - 16
        self.egg.rect.bottom      =  self.rect.bottom - 63
        self.egg1.rect.bottom     =  self.rect.bottom - 63
        self.bullet.add(self.egg,self.egg1)

    def shot(self):
        self.amraam               =  Bullet('imagine/bomb.png') 
        self.amraam.rect.centerx  =  self.rect.centerx
        self.amraam.rect.bottom   =  self.rect.bottom - 120
        self.bullet.add(self.amraam)
        
        
class Bullet(GameSprite):
    def __init__(self,imageName):
        super().__init__(imageName,-2)
    
    def update(self):
        super().update()
        if self.rect.bottom < 0:
            self.kill()
