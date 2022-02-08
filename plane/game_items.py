import pygame,time,random
#定义全局变量
SCREEN_RECT=pygame.Rect(0,0,480,600)
FRAME_INTERVAL=10
HERD_BOMB_COUNT=3
HERD_DEFAULT_MID_BOTTOM=(SCREEN_RECT.centerx,SCREEN_RECT.bottom-10)
HERD_DEAD_EVENT=pygame.USEREVENT#牺牲事件
HERD_DEAD_OFF_EVENT=pygame.USEREVENT+1#牺牲事件
HERO_FIRE_EVENT=pygame.USEREVENT+2 #发射子弹
THROW_SUPPLY_ENENT=pygame.USEREVENT+3
BULLET_ENHANCHE_OFF_EVENT=pygame.USEREVENT+4


class GameSprite(pygame.sprite.Sprite):
    res_path='./img/'
    def __init__(self,image_name,speed,*group):
        '''初始化精灵对象 调用父类方法'''
        super(GameSprite,self).__init__(*group)
        #创建图片
        self.image=pygame.image.load(self.res_path+image_name)

        #获取举行
        self.rect=self.image.get_rect()
        #设置速度
        self.speed=speed
        #生成描边属性，提高碰撞执行效率
        self.mask = pygame.mask.from_surface(self.image)

    def update(self, *args):
        #更新元素数据
        self.rect.y+=self.speed

class BackGroud(GameSprite):
    def __init__(self, is_alt,*group):
        '''如果is_alt 为true， 显示窗口上方，否则显示窗口内部'''
        super(BackGroud, self).__init__('maps/img_bg_level_1.jpg',1,*group)

        if is_alt:
            self.rect.y = -self.rect.h



    def update(self, *args):
        super(BackGroud, self).update(*args)
        #判断，如果图片已经滚动到底部，则立即回到顶部
        if self.rect.y>self.rect.h:
            self.rect.y=- self.rect.y


class StatusButton(GameSprite):
    def __init__(self,image_names,*groups):

        super(StatusButton, self).__init__(image_names[0],0,*groups)
        #准备用于切换显示的2个图片
        self.images=[pygame.image.load(self.res_path+name) for name in image_names]

    def switch_status(self,is_pause):
        '''根据是否暂停，切换要使用的图片对象'''
        self.image=self.images[1 if is_pause else 0]




class Label(pygame.sprite.Sprite):
    '''标签'''
    pygame.init()
    font_path='./font/font.ttf'
    def __init__(self,text,size,color,*groups):
        super(Label,self).__init__(*groups)
        #字体对象
        self.font= pygame.font.Font(self.font_path,size)
        self.color=color
        #精灵属性
        self.image=self.font.render(text,True,self.color)
        self.rect=self.image.get_rect()

    def set_text(self,text):
        '''更新显示文本内容'''
        self.image=self.font.render(text,True,self.color)
        self.rect=self.image.get_rect()

class Plane(GameSprite):
    def __init__(self, narmal_names, speed, hp, value, wav_name, hurt_name, destory_name, *groups):
        super(Plane, self).__init__(narmal_names[0], speed, *groups)
       #飞机基本属性
        self.hp=hp
        self.max_hp=hp#初始生命值
        self.value=value
        self.wav_name=wav_name#音效名

        #飞机播放图片
        '''飞机类的初始化'''
        self.narmal_images = [pygame.image.load(self.res_path+name) for name in narmal_names]
        self.normal_index=0
        self.hurt_image=pygame.image.load(self.res_path+hurt_name)
        self.destory_images=[pygame.image.load(self.res_path+name) for name in destory_name]# 摧毁状态的图片列表
        self.destory_index=0


    def update(self, *args):
        ''' 更新状态，准备下一次显示的内容 '''
        #判断是否要更新
        if not args[0]:
            return
        if self.hp == self.max_hp:
            self.image= self.narmal_images[self.normal_index]
            # 计算下次显示的索引
            count = len(self.narmal_images)
            self.normal_index = (self.normal_index+1) % count
        elif self.hp>0:
            #受伤
            self.image=self.hurt_image
        else:
            #死亡
            if self.destory_index<len(self.destory_images):
                self.image=self.destory_images[self.destory_index]
                self.destory_index+=1
            else:
                self.reset_plane()

    def reset_plane(self):
        '''重置飞机'''
        self.hp = self.max_hp
        self.normal_index=0
        self.destory_index=0
        self.image=self.narmal_images[0]


class Enemy(Plane):
    '''敌人飞机'''
    def __init__(self,kind, max_speed,*groups):
        '''初始化敌人飞机'''
        self.kind = kind
        self.max_speed = max_speed
        print('max----speed---->',max_speed)
        if kind ==0:
            #小敌机
            super(Enemy,self).__init__(
                ['/enemy/a1_1.png'],2,3,1000,'/sound/enemy1_down.wav','/enemy/a1_1.png',['/boom/boom_1.png','/boom/boom_2.png'],*groups
            )
        if kind ==1:
            #中敌机
            super(Enemy, self).__init__(
                ['/enemy/a2_1.png'], 2, 6, 6000, '/sound/enemy2_down.wav', '/enemy/a2_1.png',
                ['/boom/boom_1.png', '/boom/boom_2.png'], *groups
            )
        if kind == 2:
            #中敌机
            super(Enemy, self).__init__(
                ['/enemy/boss_1.png'], 2, 15, 15000, '/sound/enemy2_down.wav', '/enemy/boss_1.png',
                ['/boom/boom_1.png', '/boom/boom_2.png'], *groups
            )
        #初始化飞机时，让飞机随机选择位置显示
        self.reset_plane()



    def reset_plane(self):
        '''重置敌机'''
        super(Enemy,self).reset_plane()
        #敌人飞机数据重置
        x= random.randint(0,SCREEN_RECT.w-self.rect.w)
        y=random.randint(0,SCREEN_RECT.h-self.rect.h)-SCREEN_RECT.h
        self.rect.topleft=(x,y)

        #重置速度
        self.speed=random.randint(2,self.max_speed)

    def update(self, *args):
        super(Enemy,self).update(*args)
        #根据血量判断是否还在移动
        if self.hp>0:
            self.rect.y+=self.speed
        #如果移动后，已经到了屏幕之外，需要重置飞机
        if self.rect.y>=SCREEN_RECT.h:
            self.reset_plane()

class Hero(Plane):
    '''初始化英雄飞机'''
    def __init__(self,*groups):
        self.is_power= False
        self.bomb_count=HERD_BOMB_COUNT
        self.bullets_kind=0 #子弹类型
        self.bullets_group=pygame.sprite.Group()#子弹精灵组
        super(Hero,self).__init__(['hero/hero_%s.png' % i for i in range(1, 3)], 5,1,0,'/sound/boom.wav', '/hero/hero_3.png',['/boom/boom_1.png'], *groups)

        self.rect.midbottom=HERD_DEFAULT_MID_BOTTOM# 创建号飞机之后，设置飞机位置为底部中间

        #发射子弹
        pygame.time.set_timer(HERO_FIRE_EVENT,200)#创建玩家飞机后，每0。2s激活一次
    def update(self, *args):
        '''args[0]:是否更新下一帧动画，args[1]水平移动，args[2]上下'''
        super(Hero,self).update(*args)
        if len(args)!=3 or self.hp<=0:
            return

        self.rect.x+=args[1]*self.speed
        #屏幕边缘位置修正
        self.rect.x=0 if self.rect.x<0 else self.rect.x
        if self.rect.right> SCREEN_RECT.right:
            self.rect.right=SCREEN_RECT.right

        self.rect.y+=args[2]*self.speed
        self.rect.y=0 if self.rect.y<0 else self.rect.y
        if self.rect.bottom> SCREEN_RECT.bottom:
            self.rect.bottom=SCREEN_RECT.bottom

    def blowup(self,enemies_group):
        '''炸毁敌机 并返回得到的总分值'''
        #判断是否可以发起引爆
        if self.bomb_count<=0 or self.hp<=0:
            return 0

        #引爆所有敌机并且累计得分
        self.bomb_count-=1
        score=0
        count=0
        for enemy in enemies_group.sprites():
           if enemy.rect.bottom > 0:
               score+=enemy.value
               enemy.hp=0
               count+=1
           print("炸毁了%d飞机，得了%d分"%(count,score))
        return score

    def reset_plane(self):
        '''重置玩家飞机'''
        super(Hero,self).reset_plane()
        self.is_power=True
        self.bomb_count=HERD_BOMB_COUNT
        self.bullets_kind=0

        #发布事件，让主逻辑更新面板
        pygame.event.post(pygame.event.Event(HERD_DEAD_EVENT))

        #发布定时事件 取消
        pygame.time.set_timer(HERD_DEAD_OFF_EVENT,3000)

    def fire(self,display_group):
        '''发射一轮子弹'''
        groups = (display_group,self.bullets_group)
        for i in range(3):
            bullet1=Bullet(self.bullets_kind,*groups)

            y=self.rect.y-i*15

            if self.bullets_kind==0:
                bullet1.rect.midbottom=(self.rect.centerx,y)
            else:
                bullet2 = Bullet(self.bullets_kind, *groups)
                bullet1.rect.midbottom=(self.rect.centerx-20,y)
                print('bullet-------2--->',self.bullets_kind)
                bullet2.rect.midbottom=(self.rect.centerx+20,y)



class Bullet(GameSprite):
    '''子弹'''
    def __init__(self,kind,*group):
        image_name='/bullet/bullet_1.png' if kind == 0 else '/bullet/bullet_5.png'

        super(Bullet,self).__init__(image_name,-12,*group)
        self.damage=1#杀伤力

    def updete(self,*args):
        super(Bullet,self).update(*args)
        #飞出屏幕之外需要销毁子弹
        if self.rect.bottom<0:
            self.kill()

class Supply(GameSprite):
    def __init__(self,kind,*group):
        '''初始化道具属性'''
        image_name='/bullet/bullet_2.png' if kind == 0 else '/bullet/bullet_1.png'
        super(Supply,self).__init__(image_name,5,*group)
        self.kind = kind
        self.wav_name = '/sound/bullet~1.wav' if kind==0 else '/sound/bullet~1.wav'#音效
        # self.rect.bottom=SCREEN_RECT.h #道具初始位置
    def update(self, *args):
        '''道具位置'''
        if self.rect.y>SCREEN_RECT.h:
            return
        super(Supply,self).update(*args)

    def throw_supply(self):
        '''投放道具'''
        self.rect.bottom=0
        self.rect.x=random.randint(0,SCREEN_RECT.w-self.rect.w)



















