from tkinter import *
from win32api import *
from time import *


#triadic color styles
ColorGreen='#388a32'
ColorBlue='#32388a'
ColorRed='#8a3238'


def SetMaxCompatibleVideoMode(): 
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
        print("Не удалось установить разрешение")

def GetTimeString():
    sLocalTime=str(time.localtime()).split(" ")
    sHour=sLocalTime[3].split('=')[1].split(',')[0]
    sMinute=sLocalTime[4].split('=')[1].split(',')[0]
    sSecond=sLocalTime[5].split('=')[1].split(',')[0]
    if int(sHour)<10:
        sHour='0'+sHour
    if int(sMinute)<10:
        sMinute='0'+sMinute
    if int(sSecond)<10:
        sSecond='0'+sSecond
    ActualTime=sHour+':'+sMinute+":"+sSecond
    

# create the root window
SetMaxCompatibleVideoMode()
root = Tk()



# modify the window
root.title("СВР-01") #set window's title
root.configure(background=ColorGreen)
ScreenWidth = root.winfo_screenwidth() #get screen width
ScreenHeight = root.winfo_screenheight() #get screen height
root.geometry(str(ScreenWidth)+"x"+str(ScreenHeight)) #set window's size
root.wm_attributes("-topmost", 1) #topmost   
root.overrideredirect(True)     #override redirect 

# kick off the window's event-loop
root.mainloop()



    
