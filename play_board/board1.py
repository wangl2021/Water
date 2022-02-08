import pygame,sys
from pygame.locals import *
import time
class Snake(pygame.sprite.Sprite):
    def __init__(self,n1,location):
        # 调父类来初始化子类
        pygame.sprite.Sprite.__init__(self)
        # 加载图片
        self.image = pygame.image.load(n1)
        # 获取图片rect区域
        self.rect = self.image.get_rect()
        # 设置位置
        self.rect.topleft = location
        # self.remove=pygame.sprite.Sprite.remove()


# 设置大小
pygame.init()
screen=pygame.display.set_mode((500, 400))
pygame.display.set_caption("hello")
screen.fill((255,255,255))
groudimg=pygame.image.load('img/a.jpg')
n1=pygame.image.load('img/85.png')
n2=pygame.image.load('img/57.png')
x = 100
y=40
location =(x,y)
snake1 = Snake('img/85.png', location)
x1 = 100
y1=4
location_2 = (x1,y1)
snake2 = Snake('img/57.png', location_2)


while True:
    screen.blit(groudimg, (0, 0))
    screen.blit(snake1.image, snake1.rect)
    screen.blit(snake2.image, snake2.rect)
    all = pygame.event.get()
    snake1 = Snake('img/85.png', location)
    y1=y1+2
    location_2 = (x1, y1)
    snake2 = Snake('img/57.png', location_2)

    crash_result = pygame.sprite.collide_rect(snake1, snake2)
    if crash_result:
        print("peng peng")
        pass
    else:
        print('nono')

    for one in all:
        if one.type == QUIT:
            pygame.quit()
            sys.exit()
        #判断如果该时间是鼠标移动事件
        if one.type == pygame.MOUSEMOTION:
            #获取鼠标移动到位置的坐标
            x,y=one.pos
            location = (x, y)

            print(x,y)
    #更新视图界面
    pygame.time.wait(50)
    pygame.display.update()














