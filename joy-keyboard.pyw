import pygame
import keyboard
import time

def main():
 pygame.init()
 pygame.joystick.init()
 x=0


 while 1:
    if pygame.joystick.get_count()>0:
        pygame.joystick.Joystick(0).init()
        for event in pygame.event.get():
           if event.type==pygame.JOYBUTTONDOWN:
              if event.button==6:
                 x=x+1
              if event.button!=6:
                 x=0 
        if x==3:
             win32api.keybd_event(win32con.VK_LMENU,0,0) 
             win32api.keybd_event(win32con.VK_F4,0,0)
             x=0
if __name__ == "__main__":
    main()


