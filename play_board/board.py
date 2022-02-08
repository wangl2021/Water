import pygame,sys
from pygame.locals import *
# 设置大小
pygame.init()
#初始化音频
pygame.mixer.init()
#加载音频
# pygame.mixer.music.load('')
#播放次数 -1循环播放
# pygame.mixer.music.play()
#开始线程播放音乐
# running=True


# 创建窗体
ct = pygame.display.set_mode((512,680))
pygame.display.set_caption('1122')
groudimg=pygame.image.load('img/a.jpg')
feiji=pygame.image.load('img/85.png')
x = 245
y=480

while True:
    ct.blit(groudimg,(0,0))
    ct.blit(feiji,(x,y))
    all = pygame.event.get()
    for one in all:
        if one.type == QUIT:
            pygame.quit()
            sys.exit()
        #判断如果该时间是鼠标移动事件
        if one.type == pygame.MOUSEMOTION:
            #获取鼠标移动到位置的坐标
            x,y=one.pos
            print(x,y)
    #更新视图界面
    pygame.display.update()














