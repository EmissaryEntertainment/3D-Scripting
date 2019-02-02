#
# scriptedfun.com
#
# Screencast #1
# Barebones Pygame Application
#
import os, pygame
from pygame.locals import *

SCREENRECT = Rect(0, 0, 640, 480)

def paddleimage(spritesheet):
    paddle = pygame.Surface((55,11)).convert()
    # left half
    paddle.blit(spritesheet.imgat((234,174,21,13)),(0,0))
    # right half
    paddle.blit(spritesheet.imgat((259,174,22,11)),(22,0))
    paddle.set_colorkey(paddle.get_at((0,0)), RLEACCEL)
    return paddle

class Spritesheet:
    def __init__(self, filename):
        self.sheet = pygame.image.load(os.path.join("C:/School/11th Quarter/3D Scripting/3D-Scripting/Final_Project_PyGame/Practice_projects/Arkinoid/data", filename)).convert()
    def imgat(self, rect, colorkey = None):
        rect = Rect(rect)
        image = pygame.Surface(rect.size).convert()
        image.blit(self.sheet, (0,0), rect)
        if colorkey is not None:
            if colorkey is -1:
                colorkey = image.get_at((0,0))
            image.set_colorkey(colorkey, RLEACCEL)
        return image
    def imgsat(self, rects, colorkey = None):
        imgs = []
        for rect in rects:
            imgs.append(self.imgat(rect, colorkey))
        return imgs

class Arena:
    tileside = 31
    numxtiles = 12
    numytiles = 14
    topx = (SCREENRECT.width - SCREENRECT.width/tileside*tileside)/2
    topy = (SCREENRECT.height - SCREENRECT.height/tileside*tileside)/2
    rect = Rect(topx + tileside,topy + tileside,tileside*numxtiles,tileside*numytiles)
    def __init__(self):
        self.background = pygame.Surface(SCREENRECT.size).convert()
    def drawtile(self,tile,x,y):
        self.background.blit(tile, (self.topx + self.tileside*x,self.topy + self.tileside*y))
    def make_background(self,tilenum):
        for x in range(0,self.numxtiles - 1):
            for y in range(0,self.numytiles - 1):
                self.drawtile(self.tiles[tilenum], x+1, y+1)
    def make_left_border(self,tilenum):
        for x in range(self.numxtiles - 11):
            for y in range(self.numytiles - 1):
                self.drawtile(self.tiles[tilenum], x+1, y+1)
    def make_right_border(self,tilenum):
        for x in range(11,self.numxtiles):
            for y in range(self.numytiles - 1):
                self.drawtile(self.tiles[tilenum], x+1, y+1)
    def make_top_border(self,tilenum):
        for x in range(self.numxtiles - 1):
            for y in range(self.numytiles - 13):
                self.drawtile(self.tiles[tilenum], x+1, y+1)
    def make_bottom_border(self,tilenum):
        for x in range(self.numxtiles - 1):
            for y in range(13,self.numytiles):
                self.drawtile(self.tiles[tilenum], x+1, y+1)

class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self,self.containers)
        self.rect = self.image.get_rect()
        self.rect.bottom = self.arena.rect.bottom - self.arena.tileside
    def update(self):
        self.rect.centerx = pygame.mouse.get_pos()[0]
        self.rect.clamp_ip(self.arena.rect)

def main():
    pygame.init()

    screen = pygame.display.set_mode(SCREENRECT.size)

    spritesheet = Spritesheet("arinoid_master.bmp")

    Arena.tiles = spritesheet.imgsat([(129,321,31,31), #purple - 0
                                      (161,321,31,31), # dark blue - 1
                                      (129,353,31,31), # red - 2
                                      (161,353,31,31), # green - 3
                                      (129,385,31,31), # blue - 4
                                      (150,257,9,29), # vert pipe L - 5
                                      (194,258,29,29), # vert pipe R - 6
                                      (194,290,29,14)]) # horz pipe - 7

    Paddle.image = paddleimage(spritesheet)

    # make background
    arena = Arena()
    arena.make_background(4) # can use this to change background color
    arena.make_left_border(5)
    arena.make_right_border(6)
    arena.make_top_border(7)
    arena.make_bottom_border(7)
    screen.blit(arena.background, (0, 0))
    pygame.display.update()

    Paddle.arena = arena

    # keep track of sprites
    all = pygame.sprite.RenderUpdates()

    Paddle.containers = all

    # keep track of time
    clock = pygame.time.Clock()

    paddle = Paddle()

    # game loop
    while 1:
        # get input
        for event in pygame.event.get():
            if event.type == QUIT   \
               or (event.type == KEYDOWN and    \
                   event.key == K_ESCAPE):
                return

        # clear sprites
        all.clear(screen, arena.background)

        # update sprites
        all.update()

        # redraw sprites
        dirty = all.draw(screen)
        pygame.display.update(dirty)

        # maintain frame rate
        clock.tick(30)
if __name__ == '__main__': main()
