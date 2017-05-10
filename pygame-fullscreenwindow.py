import pygame as pg
import sys
pg.init()
VideoModes=pg.display.list_modes()
intWidth=int(str(VideoModes[0])[1:-1:1].split(',')[0])
intHeight=int(str(VideoModes[0])[1:-1:1].split(',')[1])
screen=pg.display.set_mode(VideoModes[0],pg.FULLSCREEN,24)
pg.draw.rect(screen,(255,255,255),(0,0,intWidth,intHeight))
pg.display.update()
while True:
     for event in pg.event.get():
          if event.type==pg.QUIT:
              pg.quit()
              sys.exit()
              pygame.display.update()
          #screen.fill((255,255,255))
          if (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
              screen=pg.display.set_mode(VideoModes[5],0,24)
input("Нажмите любую клавишу")

