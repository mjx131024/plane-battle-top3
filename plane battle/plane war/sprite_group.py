import pygame
import random

MAIN_INTERFACE = pygame.Rect(0, 0, 480, 700)

CREATE_ENEMY_EVENT = pygame.USEREVENT


class SpriteGroup(pygame.sprite.Sprite):

    def __init__(self, image_name, speed = 1):
        super().__init__()

        self.image = pygame.image.load(image_name)

        self.rect = self.image.get_rect()

        self.speed = speed

    def update(self):
        self.rect.y += self.speed


class Background(SpriteGroup):
    def __init__(self, is_alt=False):
        super().__init__(r'C:\Users\mjx131024\Desktop\plane war\images\background.png')

        if is_alt:
            self.rect.y = -self.rect.height

    def update(self):
        if self.rect.y >= MAIN_INTERFACE.height:
            self.rect.y = -self.rect.height

        super().update()


class Enemy(SpriteGroup):
    def __init__(self):
        number = random.randint(0, 2)
        if number == 0:
            file_name = r'C:\Users\mjx131024\Desktop\plane war\images\fdu.jpg'
        elif number == 1:
            file_name = r'C:\Users\mjx131024\Desktop\plane war\images\zju.jpg'
        elif number == 2:
            file_name = r'C:\Users\mjx131024\Desktop\plane war\images\zhongke.jpg'
        super().__init__(file_name)
        print('创建敌机')
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        # 1.随机初始位置
        self.rect.y = -self.rect.height
        aval = MAIN_INTERFACE.width - self.rect.width - 20
        self.rect.x = random.randint(20, aval)
        # 2.随机速度
        self.speed = random.randint(1, 5)

    def update(self):
        super().update()

        if self.rect.y >= MAIN_INTERFACE.height:
            print('删除敌机')
            self.kill()


class Hero(SpriteGroup):
    def __init__(self):
        super().__init__(r'C:\Users\mjx131024\Desktop\plane war\images\sjtu.jpg', 0)
        self.image = pygame.transform.scale(self.image, (102, 126))
        self.rect = self.image.get_rect()
        self.rect.bottom = MAIN_INTERFACE.height - 120
        self.rect.centerx = MAIN_INTERFACE.centerx

        self.bullets = pygame.sprite.Group()

    def update(self):
        super().update()
        rightline = MAIN_INTERFACE.width - self.rect.width
        if self.rect.x < 0:
            self.rect.x = 0
        if self.rect.x > rightline:
            self.rect.x = rightline

    def fire(self):
        for i in range(3):
            bullet = Bullet()
            bullet.rect.bottom = self.rect.y - 20 * i
            bullet.rect.centerx = self.rect.centerx
            self.bullets.add(bullet)


class Bullet(SpriteGroup):
    def __init__(self):
        super().__init__(r'C:\Users\mjx131024\Desktop\plane war\images\bullet1.png', -4)

    def update(self):
        super().update()

        if self.rect.bottom <= 0:
            self.kill()
