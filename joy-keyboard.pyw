import pygame
import keyboard
import time
import subprocess

def main():
    pygame.init()
    
    x=0
    joy_is_conected=False
    joy_waiting=False
    with subprocess.Popen(["C:\Program Files\Oculus\Support\oculus-client\OculusClient.exe"], stdout=subprocess.PIPE) as proc:
       while True:
            pygame.joystick.init()
            joy_count=pygame.joystick.get_count()
            
            if joy_count>0:
                if not joy_is_conected:
                    print("Геймпад подключен!")
                    joy_is_conected=True
                    joy_waiting=False
                    
            elif joy_count==0 and joy_waiting==False:    
                print("Подключите геймпад!")
                joy_waiting=True
                pygame.joystick.quit()
                
            if joy_is_conected:
                pygame.joystick.Joystick(0).init()
                for event in pygame.event.get():
                    if event.type==pygame.JOYBUTTONDOWN:
                        #print(event.button)
                        if event.button==6:
                            x=x+1
                            print("back")
                            # keyboard.send('alt+tab')
                            # time.sleep(1)
                            keyboard.send('alt+F4')
                    #     if :
                    #         x=x+1
                    #     if event.button!=6:
                    #         x=0 
                    # if x==3:
                    #     keyboard.send("alt+F4")
                    #     x=0
                pygame.joystick.Joystick(0).quit()
            time.sleep(3)
      
if __name__ == "__main__":
    main()


