from pygame import *
import pygame
from random import randrange

init()
mixer.init()
window = display.set_mode((500, 500))
colors = (0, 0, 0)
window.fill(colors)
clock = time.Clock()
mixer.music.load('t3.mp3')
mixer.music.play(-1)

ARIAL_50 = font.SysFont('Courier New', 50)
menu_lan = image.load('pip.jpg')
poi = 500
piu = 20
colors = (255, 255, 255)
#----------------------------------------------------------------------------------------------------------------------------------------------------------

class Menu:
    def __init__(self):
        self._option_surfaces = []
        self._callbacks = []
        self._current_option_index = 0
    
    def append_option(self, option, callback):
        self._option_surfaces.append(ARIAL_50.render(option, True, (255, 255, 255)))
        self._callbacks.append(callback)
    
    def switch(self, direction):
        self._current_option_index = max(0, min(self._current_option_index + direction, len(self._option_surfaces) - 1))

    def select(self):
        self._callbacks[self._current_option_index]()

    def draws(self, surf, x, y, option_y_padding):
          for i, option in enumerate(self._option_surfaces):
            option_rect = option.get_rect()
            option_rect.topleft = (x, y + i * option_y_padding)
            if i == self._current_option_index:
                draw.rect(surf, (0,100, 0), option_rect)
            surf.blit(option, option_rect)
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def io():
    x, y = randrange(0, poi, piu), randrange(0, poi, piu)
    appel = randrange(0, poi, piu), randrange(0, poi, piu)
    dirs = {'W': True, 'S': True, 'A': True, 'D': True, }
    length = 1
    snake = [(x, y)]
    dx, dy = 0, 0
    fps = 5



    clock = pygame.time.Clock()

    while True:
        window.blit(menu_lan, (0,0))
        [(pygame.draw.rect(window, pygame.Color('green'), (i, j, piu - 2 , piu - 2))) for i, j in snake]
        pygame.draw.rect(window, pygame.Color('red'), (*appel, piu, piu))

        x += dx * piu
        y += dy * piu

        snake.append((x, y))
        snake = snake[-length:]

        if snake[-1] == appel:
            appel = randrange(0, poi, piu), randrange(0, poi, piu)
            length += 1
            fps += 1
        
        if x < 0 or x > poi - piu or y < 0 or y > poi - piu:
            pren()
        if len(snake) != len(set(snake)):
            pren()

        pygame.display.flip()
        clock.tick(fps)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        key = pygame.key.get_pressed()
        if key[pygame.K_w] and dirs['W']:
            dx, dy = 0, -1
            dirs = {'W': True, 'S': False, 'A': True, 'D': True, }
        if key[pygame.K_s] and dirs['S']:
            dx, dy = 0, 1
            dirs = {'W': False, 'S': True, 'A': True, 'D': True, }
        if key[pygame.K_a] and dirs['A']:
            dx, dy = -1, 0
            dirs = {'W': True, 'S': True, 'A': True, 'D': False, }
        if key[pygame.K_d] and dirs['D']:
            dx, dy = 1, 0
            dirs = {'W': True, 'S': True, 'A': False, 'D': True, }

def pren():
    menu = Menu()
    menu.append_option('ВЫ ПРОИГРАЛИ', games)
    menu.append_option('< - Назад', games)
    menu.switch(1)
    sow = True
    while sow:
        for e in event.get():
            if e.key == K_SPACE or e.key == K_RETURN:
                menu.select()
        
        window.blit(menu_lan, (0,0))
        menu.draws(window, 80, 100, 75)
        display.update()

        clock.tick(60)
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
class Area ():
    def __init__(self, x=0, y=0, width = 10, height= 10, color = None ):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = colors
        if color:
            self.fill_color = color
    def show(self):
        pygame.draw.rect(window, self.fill_color, self.rect)
    def sred(self, rect):
        return self.rect.colliderect(rect)

class Picture(Area):
    def __init__(self, fillename, x=0, y=0, width = 10, height = 10, colors = None):
        Area.__init__(self, x=x, y=y, width=width,height=height, color = colors)
        self.image = pygame.image.load(fillename)
    def izon(self, fillename):
        self.image = pygame.image.load(fillename)
    def draw(self):
        window.blit(self.image, (self.rect.x, self.rect. y))
def poin(i):
    i.draw()

monsters = []



def hh():
    def opinee(m_x, m_y, u, ie, oo):
        for i in range(u):
            monster = Picture(oo, m_x, m_y, 30, 15)
            ie.append(monster)
            m_x += 30
    ball = Picture("ba.png", 200, 200, 5, 5)
    platform = Picture("pla.png", 150, 440, 100, 30)

    monsters = []
    monsters1 = []
    monsters2 = []
    monsters3 = []
    m_x = 5

    speed_x = -8
    speed_y = -8

    window.fill(colors)

    monster = Picture("lop.png", 0, 0)
    monster1 = Picture("lop.png", 490, 0)
    opinee(10, 60, 16, monsters3, "enem.png")
    opinee(10, 75, 16, monsters2, "e.png")
    opinee(10, 90, 16, monsters1, "en.png")
    opinee(10, 105, 16, monsters, "ene.png")

    move_right = False
    move_left  = False
    o = True
    while o:
        window.fill(colors)
        ball.show()
        platform.show()
        monster.show()
        monster1.show()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d or event.key == K_RIGHT:
                    move_right = True
                elif event.key == pygame.K_a or event.key == K_LEFT:
                    move_left = True 
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d or event.key == K_RIGHT:
                    move_right = False
                elif event.key == pygame.K_a or event.key == K_LEFT:
                    move_left = False

        if move_right and platform.rect.x < 390 :
            platform.rect.x += 10
        if move_left and platform.rect.x > 10:
            platform.rect.x -= 10

        if ball.rect.x < 15:
            speed_x *= -1
        if ball.rect.x > 480:
            speed_x *= -1
        if ball.rect.y < 0:
            speed_y *= -1
        if ball.rect.y > 490:
            rr1()
        if platform.sred(ball.rect) == True:
            speed_y *= -1

        ball.rect.x += speed_x
        ball.rect.y += speed_y
        ball.draw()
        platform.draw()
        monster.draw()
        monster1.draw()
        for n in monsters:
            n.show()
            n.draw()
            if n.sred(ball.rect) == True:
                speed_y *= -1
                n.show()
                monsters.remove(n)
        
        for p in monsters1:
            p.show()
            p.draw()
            if p.sred(ball.rect) == True:
                speed_y *= -1
                p.show()
                p.izon("ene.png")
                monsters.append(p)
                monsters1.remove(p)

        for p in monsters2:
            p.show()
            p.draw()
            if p.sred(ball.rect) == True:
                speed_y *= -1
                p.show()
                p.izon("en.png")
                monsters1.append(p)
                monsters2.remove(p)

        for p in monsters3:
            p.show()
            p.draw()
            if p.sred(ball.rect) == True:
                speed_y *= -1
                p.show()
                p.izon("e.png")
                monsters2.append(p)
                monsters3.remove(p)
        
        display.update()

        clock.tick(60)
        
        if len(monsters) == 0 :
            rr()
        ball.draw()
        clock.tick(60)
 

def rr1():
    menu = Menu()
    menu.append_option('ВЫ ПРОИГРАЛИ', games)
    menu.append_option('< - Назад', games)
    menu.switch(1)
    sow = True
    while sow:
        for e in event.get():
            if e.key == K_SPACE or e.key == K_RETURN:
                menu.select()
        
        window.blit(menu_lan, (0,0))
        menu.draws(window, 80, 100, 75)
        display.update()

        clock.tick(60)

def rr():
    menu = Menu()
    menu.append_option('ВЫ ВЫИГРАЛИ', games)
    menu.append_option('< - Назад', games)
    menu.switch(1)
    sow = True
    while sow:
        for e in event.get():
            if e.key == K_SPACE or e.key == K_RETURN:
                menu.select()
        
        window.blit(menu_lan, (0,0))
        menu.draws(window, 80, 100, 75)
        display.update()

        clock.tick(60)    

#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def gettr(u):
    sow = True
    while sow:
        for e in event.get():
            if e.type == QUIT:
                start = False
            elif e.type == KEYDOWN:
                if e.key == K_w or e.key == K_UP:
                    u.switch(-1)
                if e.key == K_s or e.key == K_DOWN:
                    u.switch(1)
                if e.key == K_SPACE:
                    u.select()
                if e.key == K_RETURN or e.key == K_KP_ENTER:
                    u.select()
        window.blit(menu_lan, (0,0))
        u.draws(window, 150, 100, 75)
        display.update()

        clock.tick(60)

def tex():


    window.blit(menu_lan, (0,0))
    ter = Menu()
    ter.append_option('< Назад', aut)
    ter.append_option('Музыка', muzik)
    
    gettr(ter)

def muzik():
    a = 1    
    window.blit(menu_lan, (0,0))
    terr = Menu()
    terr.append_option('< Назад', tex)
    terr.append_option('< Громкость >', muzik)
    mixer.music.set_volume(a)


    sow = True
    while sow:
        for e in event.get():
            if e.type == QUIT:
                start = False
            elif e.type == KEYDOWN:
                if e.key == K_w or e.key == K_UP:
                    terr.switch(-1)
                if e.key == K_s or e.key == K_DOWN:
                    terr.switch(1)
                if e.key == K_a or e.key == K_LEFT:
                    a -= 0.1  
                if e.key == K_d or e.key == K_RIGHT:
                    a += 0.1
                if e.key == K_SPACE or e.key == K_KP_ENTER or e.key == K_RETURN:
                    terr.select()
        
        mixer.music.set_volume(a)
        window.blit(menu_lan, (0,0))
        terr.draws(window, 80, 100, 75)
        display.update()

        clock.tick(60)

def games():
    gamess = Menu()
    gamess.append_option('Змейка', io)
    gamess.append_option('Арканоид', hh)
    gamess.append_option('Платформа', hhrr)
    gamess.append_option('<- Назад', aut)

    gettr(gamess)

def aut():

    menu = Menu()
    menu.append_option('Игры', games)
    menu.append_option('Настройки', tex)
    menu.append_option('Виход', quit)    

    gettr(menu)

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def hhrr():
    ball = Picture("ball.png", 200, 200, 50, 50, (50,205,50))
    platform = Picture("platform.png", 150, 440, 100, 30, (50,205,50))
    platform2 = Picture("platform.png", 150, 60, 100, 30, (50,205,50))


    speed_x = -8
    speed_y = -8

    window.fill((50,205,50))

    move_right = False
    move_left  = False
    move_right2 = False
    move_left2  = False
    f1 = pygame.font.Font(None, 36)
    text1 = f1.render('------------------------------------------------------------------------------------------------',  1, (0, 0, 0))
    text2 = f1.render('Игрок 1', 1, (0, 0, 0))
    text3 = f1.render('Игрок 2', 1, (0, 0, 0))
    o = True
    while o:
        window.fill((50,205,50))
        window.blit(text1, (0,250))
        ball.show()
        platform.show()
        platform2.show()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d :
                    move_right = True
                elif event.key == pygame.K_a :
                    move_left = True 
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_d :
                    move_right = False
                elif event.key == pygame.K_a :
                    move_left = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_RIGHT:
                    move_right2 = True
                elif event.key == K_LEFT:
                    move_left2 = True 
            elif event.type == pygame.KEYUP:
                if event.key == K_RIGHT:
                    move_right2 = False
                elif  event.key == K_LEFT:
                    move_left2 = False

        if move_right and platform.rect.x < 400 :
            platform.rect.x += 10
        if move_left and platform.rect.x > 0:
            platform.rect.x -= 10
        if move_right2 and platform2.rect.x < 400 :
            platform2.rect.x += 10
        if move_left2 and platform2.rect.x > 0:
            platform2.rect.x -= 10

        if ball.rect.x < 0:
            speed_x *= -1
        if ball.rect.x > 450:
            speed_x *= -1
        if ball.rect.y < 0:
            op2()
        if ball.rect.y >460:
            op1()
        if platform.sred(ball.rect) == True:
            speed_y *= -1
        if platform2.sred(ball.rect) == True:
            speed_y *= -1
        

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        ball.draw()
        platform.draw()
        platform2.draw()
        window.blit(text1, (0,250))
        window.blit(text2, (400,470))
        window.blit(text3, (10, 0))
        display.update()

        clock.tick(60)
        
        ball.draw()
        clock.tick(60)

def op1():
    menu = Menu()
    menu.append_option('Победа 2 ', games)
    menu.append_option('< - Назад', games)
    menu.switch(1)
    sow = True
    while sow:
        for e in event.get():
            if e.key == K_SPACE or e.key == K_RETURN:
                menu.select()
        
        window.blit(menu_lan, (0,0))
        menu.draws(window, 80, 100, 75)
        display.update()

        clock.tick(60)

def op2():
    menu = Menu()
    menu.append_option('Победа 1', games)
    menu.append_option('< - Назад', games)
    menu.switch(1)
    sow = True
    while sow:
        for e in event.get():
            if e.key == K_SPACE or e.key == K_RETURN:
                menu.select()
        
        window.blit(menu_lan, (0,0))
        menu.draws(window, 80, 100, 75)
        display.update()

        clock.tick(60)



aut()