import pygame
from plane.game_items import  *
class HUBPanel(object):
    '''所有面板精灵控制类'''
    margin=10
    white=(255,255,255)
    gray =(64,64,64)

    reward_score = 100000
    level2_score = 10000
    level3_score = 50000
    record_filename = 'record.txt'
    def __init__(self,display_group):
        #基本信息
        self.score=0 #分数
        self.lives_count=3
        self.level=1 #级别
        self.best_score = 0

        #图片精灵
        self.status_sprite=StatusButton(('ui/back.png','bullet/bullet_5.png'),display_group)
        self.status_sprite.rect.topleft=(self.margin,self.margin)
        self.bomb_sprite=GameSprite('bullet/bullet_4.png',0,display_group)
        self.bomb_sprite.rect.x=self.margin
        self.bomb_sprite.rect.y = SCREEN_RECT.bottom-self.margin
        # 生命.
        self.live_sprite=GameSprite('ui/life.png',0,display_group)
        self.live_sprite.rect.right=SCREEN_RECT.right-self.margin
        self.live_sprite.rect.y = SCREEN_RECT.bottom-self.margin
        #分数标签
        self.score_label=Label('%d' % self.score, 32,self.gray,display_group)
        self.score_label.rect.midleft=(self.status_sprite.rect.right+self.margin,self.status_sprite.rect.centery)
        #炸弹计数
        self.bomb_label=Label('X 3',16,self.white,display_group)
        self.bomb_label.rect.midleft=(self.bomb_sprite.rect.left+self.margin*5,self.bomb_sprite.rect.centery)

        #生命计数
        self.lives_label=Label('X %d' % self.lives_count,16,self.white,display_group)
        self.lives_label.rect.midright=(SCREEN_RECT.right+self.margin*2,self.bomb_sprite.rect.centery)

        # #生命精灵
        # self.lives_sprite=GameSprite('',0,display_group)
        # self.lives_sprite.rect.right=SCREEN_RECT.right-self.margin
        # self.lives_sprite.rect.bottom=SCREEN_RECT.bottom-self.margin

        # 最好成绩
        self.best_score_label = Label('Best:%d' % self.best_score, 36, self.white)
        self.best_score_label.rect.center = SCREEN_RECT.center
        #状态
        self.status_label=Label('Game Paused!',48,self.white)
        self.status_label.rect.midbottom=(self.best_score_label.rect.centerx,self.best_score_label.rect.y-2*self.margin)

        #提示
        self.tip_label=Label('press xxxx',36,self.white)
        self.tip_label.rect.midtop=(self.best_score_label.rect.centerx,self.best_score_label.rect.bottom+8*self.margin)
        #从文件中获取最好成绩
        self.load_best_score()
        print('初始化',self.best_score)
    def show_bomb(self,count):
        self.bomb_label.set_text('X %d'%count)
        self.bomb_label.rect.midleft=(self.bomb_sprite.rect.left+self.margin*5,self.bomb_sprite.rect.centery)

    def show_lives(self):
       #生命
        self.lives_label.set_text('X %d'% self.lives_count)
        self.lives_label.rect.midright=(SCREEN_RECT.right+self.margin*2,self.bomb_sprite.rect.centery)

    # 分数
    def increase_score(self, enemy_score):
        #计数最新得分
        score = self.score + enemy_score
        #判断是否增加生命
        if score // self.reward_score != self.score // self.reward_score:
            self.lives_count += 1
        self.show_lives()

        self.score = score

        #、更新最好成绩
        self.best_score=score if score > self.best_score else self.best_score


        #计算最新关卡等级
        if score < self.level2_score:
            level=1
        elif score <self.level3_score:
            level=2
        else:
            level=3

        is_upgrade=level != self.level
        self.level=level

        self.score_label.set_text('%d' % score)
        self.score_label.rect.midleft=(self.status_sprite.rect.right+self.margin,self.status_sprite.rect.centery)
        return is_upgrade

    def save_best_score(self):
        '''保存最好成绩'''
        file=open(self.record_filename,'w')

        file.write('%d'%self.best_score)
        file.close()
    def load_best_score(self):
        file=open(self.record_filename,'r')
        content=file.read()
        file.close()
        self.best_score=int(content)

    def panel_pause(self,is_game_over,display_group):
        '''停止，显示信息，is_game_over=true,结束,否则暂停'''
        #判断是否已经显示内容
        if display_group.has(self.best_score,self.status_label,self.tip_label):#has 包含
            return

        #根据有限状态生成提示信息
        status = 'Game Over!' if is_game_over else 'Game Paused!'
        tip = 'Press spacebar to'
        tip+='play again.' if is_game_over else 'continue.'
        #修改标签精灵文本内容
        self.best_score_label.set_text('Best:%d'%self.best_score)
        self.status_label.set_text(status)
        self.tip_label.set_text(tip)

        #修正标签精灵位置
        self.best_score_label.rect.center = SCREEN_RECT.center
        # 状态
        self.status_label.rect.midbottom = (
        self.best_score_label.rect.centerx, self.best_score_label.rect.y - 2 * self.margin)
        # 提示
        self.tip_label.rect.midtop = (
        self.best_score_label.rect.centerx, self.best_score_label.rect.bottom + 8 * self.margin)
        #将标签精灵添加到精灵组
        display_group.add(self.best_score_label,self.status_label,self.tip_label)

        #修改状态按钮
        self.status_sprite.switch_status(True)


    def panel_resume(self,display_group):
        '''取消停止状态'''
        display_group.remove(self.best_score_label,self.status_label,self.tip_label)
        self.status_sprite.switch_status(False)

    def reset_panel(self):
        '''重置面板数据'''
        self.score = 0
        self.lives_count = 3
        # 重置精灵数据
        self.increase_score(0)
        self.show_bomb(3)
        self.show_lives()






















