#My First Py Game which is like classic Snake game.
#Give a red Boundary if possible I am going to eat food its too late....

import pygame
import random
pygame.init()

win = pygame.display.set_mode((1300,700))
pygame.display.set_caption("My First Game")

Black = (0,0,0)
Green = (0,255,0)
Red = (255,0,0)
White = (255,255,255)
Blue = (0,0,255)
count=0

x=50
y=50
width=50
height=50
SnakeWidth=50
SnakeHeight=50
vel=25

first=True
if first:
    fx=150
    fy=150

font = pygame.font.Font(None, 36)
GameOver=False

MoveRight=True
MoveLeft=False
MoveTop=False
MoveBot=False

run=True
win.fill(White)
instruct=font.render("! ! !   Snake   ! ! !",True,Red)
win.blit(instruct,[250,0])
instruct=font.render("Instructions : Do not Clash with Boundaries  - Try to eat food from Left or Right",True,Blue)
win.blit(instruct,[250,50])
instruct=font.render("Note : The Snake sometimes won't eat food!!! don't worry it will. Try your best to feed it LOL...(That's a BUG)",True,Blue)
win.blit(instruct,[250,80])
pygame.display.update()
pygame.time.delay(5000)


    
while run:
    pygame.time.delay(100)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT] and x>0:
        x-=vel
        MoveRight=False
        MoveLeft=True
        MoveTop=False
        MoveBot=False

    if keys[pygame.K_RIGHT] and x<1250:
        x+=vel
        MoveRight=True
        MoveLeft=False
        MoveTop=False
        MoveBot=False

    if keys[pygame.K_UP] and y>0:
        y-=vel
        MoveRight=False
        MoveLeft=False
        MoveTop=True
        MoveBot=False

    if keys[pygame.K_DOWN] and y<650:
        y+=vel
        MoveRight=False
        MoveLeft=False
        MoveTop=False
        MoveBot=True

    if MoveRight and x<1250:
        x+=vel
    elif MoveLeft and x>0:
        x-=vel
    elif MoveTop and y>0:
        y-=vel
    elif MoveBot and y<650:
        y+=vel
    win.fill(White)

    def foodx():
        fx = random.randint(50,1200)
        return fx

    def foody():
        fy = random.randint(50,600)
        return fy



    if x==0 or x==1250 or y==0 or y==650:
        GameOver=True

    if GameOver:
        win.fill(White)
        text=font.render("Game Over",True,Blue)
        win.blit(text,[650,350])
        text=font.render("Score is:",True,Blue)
        win.blit(text,[100,30])
        text=font.render(str(count),True,Blue)
        win.blit(text,[100,70])
        pygame.display.update()
        pygame.time.delay(2000)
        pygame.quit()
        exit()
    if((x in range(fx,fx+50) or x in range(fx,fx-50)) and (y in range(fy,fy+50) or y in range(fy,fy-50))):
        fx=foodx()
        fy=foody()
        count+=1
        first=False
        SnakeWidth+=25
    f1=pygame.draw.rect(win, Green, (fx,fy,width,height))
    f1=pygame.display.update()
    pl=pygame.draw.rect(win, Red, (x,y,SnakeWidth,SnakeHeight))
    pl=pygame.display.update()
    e1=pygame.draw.circle(win,Black,(x+10,y+10),(5))
    e1=pygame.display.update()
    e2=pygame.draw.circle(win,Black,(x+10,y+30),(5))
    e2=pygame.display.update()
    if first:
        f1=pygame.draw.rect(win, Green, (fx,fy,width,height))
        f1=pygame.display.update()
        first=False
    text=font.render("Score is:",True,Blue)
    win.blit(text,[100,30])
    text=font.render(str(count),True,Blue)
    win.blit(text,[100,70])
    pygame.display.update()
    
    
pygame.quit()
