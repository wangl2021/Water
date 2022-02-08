from plane.game_hub import *
from plane.game_items import *
import random
import pygame

class Game(object):
    def __init__(self):
        self.main_window = pygame.display.set_mode((512,680))
        self.is_game_over = False
        self.is_game_pause = False
        #不使用精灵情况下加载图片
        # self.create_image()
        #游戏状态
        self.is_game_over = False
        self.is_game_pause = False

        #精灵组
        self.all_group=pygame.sprite.Group()
        self.enemies_group=pygame.sprite.Group()#敌机分组
        self.supplies_group=pygame.sprite.Group()#道具精灵组

        #游戏精灵
        # BackGroud(False,self.all_group)#背景，速度，所属组==self.all_group.add(BackGroud(False),BackGroud(True))
        # BackGroud(True, self.all_group)  # 背景，速度，所属组
        self.all_group.add(BackGroud(False),BackGroud(True))
        # hero_sprite=GameSprite('hero/hero_1.png', 0, self.all_group)#英雄，速度，所属组
        # self.hero_sprite=Plane(['hero/hero_%s.png' % i for i in range(1, 3)], 0,180,0,'/sound/boom.wav', '/hero/hero_3.png',['/boom/boom_1.png'], self.all_group)#英雄，速度，所属组
        #
        # self.hero_sprite.rect.center=SCREEN_RECT.center

        #控制面板
        self.hub_panel=HUBPanel(self.all_group)
        #创建英雄飞机精灵
        self.hero_sprite=Hero(self.all_group)
        self.hub_panel.show_bomb(self.hero_sprite.bomb_count)
        #初始化敌机
        self.create_enemies()
        #初始化道具
        self.create_supply()
        #测试，让敌机静止
        # for enemy in self.enemies_group.sprites():
        #     enemy.speed=0
        #     enemy.rect.y+=500
        # self.hero_sprite.speed=1



    def reset_game(self):
        self.is_game_over = False
        self.is_game_pause = False

        #重置面板
        self.hub_panel.reset_panel()
        #重置英雄飞机位置
        self.hero_sprite.rect.midbottom=HERD_DEFAULT_MID_BOTTOM
        #销毁所有敌机
        for enemy in self.enemies_group:
            enemy.kill()
        for bullet in self.hero_sprite.bullets_group:
            bullet.kill()

            self.create_enemies()

    def start(self):
        #创建时钟
        clock=pygame.time.Clock()
        #动画帧数计数器
        frame_count=0

        while True:
           #判断是否已死亡
           self.is_game_over=self.hub_panel.lives_count==0
           #处理事件监听
           if self.event_handler():
               #退出之前，要保存最好成绩

               self.hub_panel.save_best_score()
               # event_handler 返回true,
               return
           if self.is_game_over:
               self.hub_panel.panel_pause(True,self.all_group)
               # print('结束，重新开始')
           elif self.is_game_pause:
               self.hub_panel.panel_pause(False,self.all_group)

               # print('暂停')
           else:
               # print('进行中')
               print("升级到%d" % (self.hub_panel.level))

               self.hub_panel.panel_resume(self.all_group)
               # if self.hub_panel.increase_score(1000):
               #     self.create_enemies()
               #     print("升级到%d"%self.hub_panel.level)
               # self.hero_sprite.hp-=1

               #移动
               keys=pygame.key.get_pressed()# 得到一个元组
               move_hor= keys[pygame.K_RIGHT]-keys[pygame.K_LEFT]#水平方向移动基数
               move_var= keys[pygame.K_DOWN]-keys[pygame.K_UP]#水平方向移动基数
               #jiance碰撞
               self.check_collide()

               # if keys[pygame.K_RIGHT]:# 长按
               #     self.hero_sprite.rect.x+=10
               # elif keys[pygame.K_LEFT]:
               #     self.hero_sprite.rect.x -= 10



               frame_count=(frame_count+1) % FRAME_INTERVAL
               self.all_group.update(frame_count==0,move_hor,move_var)



           #绘制内容：
           # self.main_window.blit(self.background_image,self.background_rect)
           # self.main_window.blit(self.hero_image, self.hero_rect)
           self.all_group.draw(self.main_window)

           pygame.display.update()
           #设置频率
           clock.tick(60)

    def event_handler(self):
       for event in pygame.event.get():#获取所有时间
           if event.type == pygame.QUIT:
               return True

           elif event.type==pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
               return True

           elif event.type==pygame.KEYDOWN and event.key==pygame.K_SPACE:
                if self.is_game_over:
                    self.reset_game()
                else:
                    self.is_game_pause = not self.is_game_pause

            #必须在未结束未暂停使用的操作
           if not self.is_game_over and not self.is_game_pause:
               if event.type == pygame.KEYDOWN and event.key == pygame.K_b:
                   #释放一个
                    # self.hub_panel.show_bomb(random.randint(0,100))
                    # self.hub_panel.show_bomb(self.hero_sprite.bomb_count-1)
                   # #生命
                   #  self.hub_panel.lives_count=random.randint(0, 100)
                   #  self.hub_panel.show_lives()

                    #测试
                    # self.hub_panel.lives_count-=1
                    # self.hub_panel.show_lives()
                    #消灭所有敌人
                   #模拟
                    # for enemy in self.enemies_group.sprites():
                    #     enemy.hp=0
                    score=self.hero_sprite.blowup(self.enemies_group)
                    self.hub_panel.show_bomb(self.hero_sprite.bomb_count)
                    if  self.hub_panel.increase_score(score):
                        self.create_enemies()
               elif event.type==HERD_DEAD_EVENT:
                   self.hub_panel.lives_count -= 1
                   self.hub_panel.show_lives()
                   self.hub_panel.show_bomb(self.hero_sprite.bomb_count)
               elif event.type==HERD_DEAD_OFF_EVENT:
                   self.hero_sprite.is_power=False
                   pygame.time.set_timer(HERD_DEAD_OFF_EVENT,0)#设置定时器延时时间为0，可用取消定时器
               elif event.type == HERO_FIRE_EVENT:
                   self.hero_sprite.fire(self.all_group)
               # if event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT:
               #     # if self.hero_sprite.rect.x<=SCREEN_RECT.x:
               #      self.hero_sprite.rect.x+=10
               elif event.type==THROW_SUPPLY_ENENT:
                   #随机抛出一个道具
                   supply= random.choice(self.supplies_group.sprites())
                   print('supply--------->',supply)
                   supply.throw_supply()
               elif event.type == BULLET_ENHANCHE_OFF_EVENT:
                   #玩家使用双排已结束
                   self.hero_sprite.bullets_kind=0
                   pygame.time.set_timer(BULLET_ENHANCHE_OFF_EVENT,0)#取消定时

       return False

    # def create_image(self):
    #     self.background_image=pygame.image.load('img/a.jpg')
    #     self.background_rect=self.background_image.get_rect()
    #     self.hero_image=pygame.image.load('img/feiji.jpg')
    #     self.hero_rect=self.hero_image.get_rect()
    #
    #     self.hero_rect.center == self.background_rect.center

    def create_enemies(self):
        count= len(self.enemies_group.sprites())
        groups=(self.all_group,self.enemies_group)

        #根据不同关卡，创建不同数量敌机
        if self.hub_panel.level == 1 and count == 0:
            for i in range(16):
                Enemy(0,3,*groups)

        elif self.hub_panel.level == 2 and count ==16:
            for enemy in self.enemies_group.sprites():
                enemy.max_speed=3
            for i in range(8):
                Enemy(0,3,*groups)
            for i in range(2):
                Enemy(1,2,*groups)
        elif self.hub_panel.level==3 and count==26:
            #关卡3
            for enemy in self.enemies_group.sprites():
                enemy.max_speed=5 if enemy.kind==0 else 3
            for i in range(8):
                Enemy(0,5,*groups)
            for i in range(2):
                Enemy(1,3,*groups)
            for i in range(2):
                Enemy(2,2,*groups)
        print("升级到%d,第%d量" % (self.hub_panel.level,count))

    def check_collide(self):
        '''检查是否有碰撞'''
        if not self.hero_sprite.is_power:#没有无敌检查碰撞

            collide_enames=pygame.sprite.spritecollide(self.hero_sprite,
                                                       self.enemies_group, False, pygame.sprite.collide_mask)
            # collide_enames= list(filter(lambda x:x.hp>0,collide_enames))
            if collide_enames:
                self.hero_sprite.hp=0
            for enemy in collide_enames:
                enemy.hp=0
            # 子弹和敌机碰撞的分析
            hit_enemies= pygame.sprite.groupcollide(self.enemies_group,self.hero_sprite.bullets_group,False,False,pygame.sprite.collide_mask)
            for enemy in hit_enemies:
                #已被摧毁不需要再处理
                if enemy.hp<=0:
                    continue

                for bullet in hit_enemies[enemy]:
                    bullet.kill()#销毁子弹
                    enemy.hp -=bullet.damage#修改敌机生命
                    if enemy.hp>0:
                        continue#敌机没有被摧毁，继续遍历下一颗子弹
                        #当前这颗子弹已经把敌机摧毁
                    if self.hub_panel.increase_score(enemy.value):
                        self.create_enemies()
                        self.check_collide()
                    #飞机已被摧毁，不需要遍历下一个颗子弹
                    break

        supples=pygame.sprite.spritecollide(self.hero_sprite,self.supplies_group,
                                            False,pygame.sprite.collide_mask)
        if supples:
            supply=supples[0]
            print('110000000000000000---->',supply.kind)
            #根据道具类型产生不同行为
            #移动道具到屏幕之下
            if supply.kind==0:
                self.hero_sprite.bomb_count+=1
                self.hub_panel.show_bomb(self.hero_sprite.bomb_count)
            else:
                self.hero_sprite.bullets_kind=1#修改子弹为双排
                pygame.time.set_timer(BULLET_ENHANCHE_OFF_EVENT,20000)
            supply.rect.y=SCREEN_RECT.h




    def create_supply(self):
        '''初始化道具'''
        Supply(1, self.all_group,self.supplies_group)
        Supply(0, self.all_group,self.supplies_group)
        pygame.time.set_timer(THROW_SUPPLY_ENENT,3000)




if __name__ == '__main__':
    game=Game()
    game.start()

