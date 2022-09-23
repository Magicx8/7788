#sprite
import pygame
import random

FPS=60 #NMSL
WIDTH=500
HEIGHT=600

WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)

#遊戲初始化and視窗
pygame.init() #初始化
screen=pygame.display.set_mode((WIDTH,HEIGHT)) #視窗
pygame.display.set_caption("遊戲測試") #標題
clock=pygame.time.Clock()#限制更新速度

class Player(pygame.sprite.Sprite): #玩家屬性
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((50,40))
        self.image.fill(GREEN)
        self.rect=self.image.get_rect()
        self.rect.centerx=(WIDTH/2)
        self.rect.bottom=(HEIGHT-10)
        self.speedx=8
    
    def update(self): #玩家屬性更新值
        key_pressed=pygame.key.get_pressed()
        if key_pressed[pygame.K_RIGHT]:
            self.rect.x +=self.speedx
        if key_pressed[pygame.K_LEFT]:
            self.rect.x -=self.speedx
            
        if self.rect.right>WIDTH: #邊界限制
            self.rect.right=WIDTH
        if self.rect.left<0:
            self.rect.left=0
            
class Rock(pygame.sprite.Sprite): #石頭屬性
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.Surface((30,40))
        self.image.fill(RED)
        self.rect=self.image.get_rect()
        self.rect.x=random.randrange(0,WIDTH-self.rect.width)
        self.rect.y=random.randrange(-100,-40)
        self.speedy=random.randrange(2,10)
        self.speedx=random.randrange(-3,3)
    
    def update(self): #石頭屬性更新值
        self.rect.y +=self.speedy
        self.rect.x +=self.speedx
        if self.rect.top>HEIGHT or self.rect.left>WIDTH or self.rect.right<0:
         self.rect.x=random.randrange(0,WIDTH-self.rect.width)
         self.rect.y=random.randrange(-100,-40)
         self.speedy=random.randrange(2,10)
         self.speedx=random.randrange(-3,3)
        
all_sprites=pygame.sprite.Group() #物件群組
player=Player()
all_sprites.add(player)
for i in range(8):#每次刷新8顆
    r=Rock()
    all_sprites.add(r)

#遊戲迴圈
running=True
while running:
    clock.tick(FPS) #幀數
    #取得輸入
    for event in pygame.event.get(): #回傳列表所有事件
        if event.type==pygame.QUIT:
            running=False
            
        #更新遊戲
    all_sprites.update() #執行群族裡每一個物件函式            
        #畫面顯示
    screen.fill(WHITE) #背景顏色
    all_sprites.draw(screen) #物件
    pygame.display.update() #畫面更新
    
pygame.quit()