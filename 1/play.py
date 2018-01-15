import pygame
from sprite import *

class PlayGame(object):
    def __init__(self):
        self.screen                 =   pygame.display.set_mode(SCREEN_RECT.size)
        self.clock                  =   pygame.time.Clock()
        self.test                   =   False
        self.superShoot             =   False
        self.superShoot1            =   False
        self.paused                 =   False
        self.createSprite()         #   创造精灵
        pygame.display.set_caption('飞机大战')
        pygame.time.set_timer(CREATE_EVENT,1000)

    def playgame(self):
        while True:
            self.clock.tick(60)
            self.eventListener()    #   事件监听
            self.checkCollide()     #   事件碰撞
            self.updateSprite()     #   更新精灵
            pygame.display.update()

    def startGame(self):
        enemyList[1]                =   'imagine/enemy0.png'
        enemyList[2]                =   'imagine/enemy1.png'
        enemyList[3]                =   'imagine/enemy2.png'
        enemyList[4]                =   'imagine/prop_type_1.png'
        a                           =   random.randint(0,100)
        if a > 97 :
            self.enemy              =   Enemy(enemyList[4])
            self.suBullet.add(self.enemy)
            self.enemy.shoot()
        elif a > 80: 
            self.enemy              =   Enemy(enemyList[3])
            self.bloodL             =   0
            self.enemyGroupL.add(self.enemy)
            self.enemy.shoot()
        elif a > 40: 
            self.enemy              =   Enemy(enemyList[2])
            self.bloodM             =   0
            self.enemyGroupM.add(self.enemy)
            self.enemy.shoot()
        elif a > 0: 
            self.enemy              =   Enemy(enemyList[1])
            self.bloodS             =   0
            self.enemyGroupS.add(self.enemy)
            self.enemy.shoot()

    def createSprite(self):
        bg1                         =   BackGround('imagine/background.png')
        bg2                         =   BackGround('imagine/background.png')
        self.start                  =   Start('imagine/start.png')
        self.pause                  =   Pause('imagine/quit_nor.png')
        self.hero                   =   Hero('imagine/hero1.png')
        self.hero1                  =   Hero('imagine/hero1.png')
        bg2.rect.y                  =   -bg1.rect.height
        self.bgGroup                =   pygame.sprite.Group(bg1,bg2)
        self.start1                 =   pygame.sprite.Group(self.start,self.pause)
        self.heroGroup              =   pygame.sprite.Group()
        self.enemyGroupS            =   pygame.sprite.Group()
        self.enemyGroupM            =   pygame.sprite.Group()
        self.enemyGroupL            =   pygame.sprite.Group()
        self.suBullet               =   pygame.sprite.Group()
        self.enemyBullet            =   pygame.sprite.Group()

    def updateSprite(self):
        for group in [
                self.bgGroup,
                self.start1,
                self.enemyGroupS,
                self.heroGroup,
                self.hero.bullet,
                self.hero1.bullet,
                self.enemyGroupM,
                self.enemyGroupL,
                self.suBullet,
                self.enemyBullet
                ]:
            group.update()
            group.draw(self.screen)

    def eventListener(self):
        key_pressed = pygame.key.get_pressed()
        for event in pygame.event.get():
            print(event)
            if self.test == True and event.type == CREATE_EVENT:    #  响应回车键
                self.heroGroup.add(self.hero,self.hero1)     #  创造两个英雄
                self.start1.remove(self.start)     #  移除图片按钮
                self.start1.remove(self.pause)
                self.startGame()            #  跳到创建敌机
                self.updateSprite()       #  更新精灵组
            if event.type == pygame.QUIT or key_pressed[27]:
                self.gameOver()
            elif key_pressed[13]:
                self.test           =   True
            elif key_pressed[32]:
                if self.paused:
                    pygame.time.set_timer(CREATE_EVENT, 0)
                    #pygame.mixer.pause()
                    
                else:
                    pygame.time.set_timer(CREATE_EVENT, 1000)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.hero.speed =   5
                if event.key == pygame.K_LEFT:
                    self.hero.speed =   -5
                if event.key == pygame.K_a:
                    self.hero1.speed=   -5
                elif event.key == pygame.K_d:
                    self.hero1.speed=   5
                elif event.key == pygame.K_j:
                    if self.superShoot1 == False:
                        self.hero1.shoot()
                    else:
                        self.hero1.shot()
                if event.key == pygame.K_KP0:
                    if self.superShoot == False:
                        self.hero.shoot()
                    else:
                        self.hero.shot()
            elif event.type == pygame.KEYUP:
                self.hero.speed = 0
                self.hero1.speed = 0
                    #pygame.mixer.unpause()
       #     if event.type == pygame.KEYDOWN:
       #         if event.key == pygame.K_KP0:
       #             if self.superShoot1 == False:
       #                 self.hero1.shoot()
       #             else:
       #                 self.hero1.shot()
       #         if event.key == pygame.K_j:
       #             if self.superShoot == False:
       #                 self.hero.shoot()
       #             else:
       #                 self.hero.shot()
       #     #elif event.type == pygame.KEYUP:
       #      #   self.hero.speed = 0
       #      #   self.hero1.speed = 0
       # key_pressed = pygame.key.get_pressed()
       # if key_pressed[100]:
       #     self.hero.speed = 5
       # elif key_pressed[97]:
       #     self.hero.speed = -5
       # else:
       #    self.hero.speed = 0
       # elif key_pressed[106]:
       #     if self.superShoot == False:
       #         self.hero.shoot()
       #     else:
       #         self.hero.shot()
       # elif key_pressed[100]:
       #     if self.superShoot == False:
       #         self.hero1.shoot()
       #     else:
       #         self.hero1.shot()
       # if key_pressed[pygame.K_RIGHT]:
       #     self.hero1.speed = 5
       # elif key_pressed[pygame.K_LEFT]:
       #     self.hero1.speed = -5
       # else:
       #     self.hero1.speed = 0

    
    def checkCollide(self):
        pygame.sprite.groupcollide(
                self.hero.bullet,
                self.enemyGroupS,
                True,
                True
                )
        pygame.sprite.groupcollide(
                self.hero.bullet,
                self.enemyGroupM,
                True,
                True
                )
        pygame.sprite.groupcollide(
                self.hero.bullet,
                self.enemyGroupL,
                True,
                True
                )
        pygame.sprite.groupcollide(
                self.hero1.bullet,
                self.enemyGroupS,
                True,
                True
                )
        pygame.sprite.groupcollide(
                self.hero1.bullet,
                self.enemyGroupM,
                True,
                True
                )
        pygame.sprite.groupcollide(
                self.hero1.bullet,
                self.enemyGroupL,
                True,
                True
                )
        superBullet                 =   pygame.sprite.spritecollide(
                self.hero,
                self.suBullet,
                True
                )
        superBullet1                =   pygame.sprite.spritecollide(
                self.hero1,
                self.suBullet,
                True
                )
        collide1Hero                =   pygame.sprite.spritecollide(
                self.hero,
                self.enemyGroupS,
                True
                )
        collide2Hero                =   pygame.sprite.spritecollide(
                self.hero,
                self.enemyGroupM,
                True
                )
        collide3Hero                =   pygame.sprite.spritecollide(
                self.hero,
                self.enemyGroupL,
                True
                )
        collide1Hero1               =   pygame.sprite.spritecollide(
                self.hero1,
                self.enemyGroupS,
                True
                )
        collide2Hero1               =   pygame.sprite.spritecollide(
                self.hero1,
                self.enemyGroupM,
                True
                )
        collide3Hero1               =   pygame.sprite.spritecollide(
                self.hero1,
                self.enemyGroupL,
                True
                )
        if len(superBullet) > 0:
            self.superShoot         =   True
        if len(superBullet1) > 0:
            self.superShoot1        =   True
        if len(collide1Hero) > 0 or len(collide2Hero) > 0 or len(collide3Hero) > 0:
            self.hero.kill()
            self.heroGroup.remove(self.hero)
        if len(collide1Hero1) > 0 or len(collide2Hero1) > 0 or len(collide3Hero1) > 0:
            self.hero1.kill()
            self.heroGroup.remove(self.hero1)
            
        pass
        #  pygame.sprite.spritecollideany(ship, aliens)
       # if pygame.sprite.spritecollideany(self.egg,self.enemyGroupS):
       #     self.bloodS +=  1
       #     #print(self.bloodS)
       # elif pygame.sprite.spritecollideany(self.hero,self.enemyGroupM,False):
       #     self.bloodM +=  1
       # elif pygame.sprite.spritecollideany(self.hero,self.enemyGroupL,False):
       #     self.bloodL +=  1
       # if self.enemy.bloodS == 3:
       #     pygame.sprite.groupcollide(self.hero.bullet,self.enemyGroupS,True,True)
       # if self.bloodS == 6:
       #     pygame.sprite.groupcollide(self.hero.bullet,self.enemyGroupM,True,True)
       # if self.bloodS == 9:
       #     pygame.sprite.groupcollide(self.hero.bullet,self.enemyGroupL,True,True)

    @staticmethod
    def gameOver():
        pygame.quit()
        exit()
if __name__ == '__main__':
    game = PlayGame()
    game.playgame()
