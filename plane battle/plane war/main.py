#coding=utf-8
import pygame
from sprite_group import *

MAIN_INTERFACE = pygame.Rect(0, 0, 480, 700)
FPS = 60

CREATE_ENEMY_EVENT = pygame.USEREVENT

HERO_FIRE_EVENT = pygame.USEREVENT + 1


class PlaneGame(object):
    def __init__(self):
        print("游戏初始化")
        # 1.加载游戏界面
        self.screen = pygame.display.set_mode(MAIN_INTERFACE.size)

        # 2.设置游戏时钟
        self.clock = pygame.time.Clock()

        # 3.加载精灵类
        self.__sprites_load()
        pygame.init()
        pygame.time.set_timer(CREATE_ENEMY_EVENT, 500)
        pygame.time.set_timer(HERO_FIRE_EVENT, 300)

    def __sprites_load(self):
        bg1 = Background()
        bg2 = Background(True)
        self.hero = Hero()

        self.herogroup = pygame.sprite.Group(self.hero)

        self.bggroup = pygame.sprite.Group(bg1, bg2)

        self.enemygroup = pygame.sprite.Group()

    def start_game(self):
        print("游戏开始...")

        while True:

            # 1.设置刷新频率
            self.clock.tick(FPS)
            # 2.监测事件
            self.__event_handler()
            # 3.检测碰撞
            self.__check_collide()
            # 4.更新精灵组
            self.__update_sprites()
            # 5.更新屏幕
            pygame.display.update()

    def __event_handler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__game_over()
            elif event.type == CREATE_ENEMY_EVENT:
                enemy = Enemy()
                self.enemygroup.add(enemy)
            elif event.type == HERO_FIRE_EVENT:
                self.hero.fire()
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_RIGHT]:
            self.hero.rect.x += 3
        elif keypressed[pygame.K_LEFT]:
            self.hero.rect.x -= 3

    def __check_collide(self):
        pygame.sprite.groupcollide(self.hero.bullets, self.enemygroup, True, True)
        #
        # enemyies = pygame.sprite.spritecollide(self.hero, self.enemygroup, False)
        #
        # if len(enemyies) > 0:
        #     self.hero.kill()
        #     print('游戏结束')
        #     exit()

    @staticmethod
    def __game_over():
        print('游戏结束')

        pygame.quit()
        exit()

    def __update_sprites(self):
        self.bggroup.update()
        self.bggroup.draw(self.screen)
        self.enemygroup.update()
        self.enemygroup.draw(self.screen)
        self.herogroup.update()
        self.herogroup.draw(self.screen)
        self.hero.bullets.update()
        self.hero.bullets.draw(self.screen)

if __name__ == '__main__':
    game = PlaneGame()

    game.start_game()