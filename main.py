#VR Shell
#For virtual station




from tkinter import *
import win32api
import time
##from subprocess import *
import psutil
import os
import pygame
import win32con

#triadic color styles
ColorGreen='#388a32'
ColorBlue='#32388a'
ColorRed='#8a3238'

SHELLEXE='explorer.exe'

def CheckProcStatus(proc_name='explorer.exe'):
    for process in psutil.process_iter():
        if process.name() == proc_name:
            print("Proccess {} is running!".format(proc_name))
            return True
def ChangeDisplayMode():
    
    VideoModes={}
    Displays=win32api.EnumDisplayMonitors()
    n=0
    while True:
        try:
            VideoModes[n]=win32api.EnumDisplaySettings(None,n)
            n+=1
        except:
            break                                        
    #print(len(VideoModes))
    MaxRes=win32api.EnumDisplaySettings(None,len(VideoModes)-1)
    try:
        win32api.ChangeDisplaySettings(MaxRes,0)
        print("Установлено максимально допустимое разрешение!")
    except:
        print("Error")
def JoyAdvancedKey():
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
                 
##class Application(Frame):
##    """ VR Shell """
##    def __init__(self,master,mode='AppMode'):
##        """ Init WIndow """
##        super(Application.self).__init__(master)
##        if mode=='AppMode':
##            
##        #self.shellordesktop()
##        #self.videomode()
##        self.grid()
##     def    
       # self.widgets()
    #def videomode(self)    
##def SetMaxCompatibleVideoMode(): 
##    VideoModes={}
##    Displays=win32api.EnumDisplayMonitors()
##    n=0
##    while True:
##        try:
##            VideoModes[n]=win32api.EnumDisplaySettings(None,n)
##            n+=1
##        except:
##            break                                        
##    #print(len(VideoModes))
##    MaxRes=win32api.EnumDisplaySettings(None,len(VideoModes)-1)
##    try:
##        win32api.ChangeDisplaySettings(MaxRes,0)
##        print("Установлено максимально допустимое разрешение!")
##    except:
##        print("Не удалось установить разрешение")
##
##def GetTimeString():
##    sLocalTime=str(time.localtime()).split(" ")
##    sHour=sLocalTime[3].split('=')[1].split(',')[0]
##    sMinute=sLocalTime[4].split('=')[1].split(',')[0]
##    sSecond=sLocalTime[5].split('=')[1].split(',')[0]
##    if int(sHour)<10:
##        sHour='0'+sHour
##    if int(sMinute)<10:
##        sMinute='0'+sMinute
##    if int(sSecond)<10:
##        sSecond='0'+sSecond
##    ActualTime=sHour+':'+sMinute+":"+sSecond
##    return ActualTime
##
### create the root window
##SetMaxCompatibleVideoMode()



#main
ChangeDisplayMode()
time.sleep(1)
i=0
root = Tk()



# modify the window
root.title("СВР-01 - Панель управления") #set window's title
root.configure(background=ColorGreen)

ScreenWidth = root.winfo_screenwidth() #get screen width
ScreenHeight = root.winfo_screenheight() #get screen height
if CheckProcStatus():
    WindowWidth = int(ScreenWidth*0.75) #get screen width
    WindowHeight = int(ScreenHeight*0.75)
    root.wm_resizable(False,False)
else:
    WindowWidth = ScreenWidth 
    WindowHeight = ScreenHeight
    root.wm_attributes("-topmost", 1)  #topmost   
    root.overrideredirect(True)   #override redirect 
root.geometry(str(WindowWidth)+"x"+str(WindowHeight)+"+"+str(int(ScreenWidth/2-WindowWidth/2))+"+"+str(int(ScreenHeight/2-WindowHeight/2))) #set window's size


os.startfile('C:\Program Files\Oculus\Support\oculus-client\OculusClient.exe')
JoyAdvancedKey()
# kick off the window's event-loop

root.mainloop()



    
