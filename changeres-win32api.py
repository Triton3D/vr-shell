import win32api
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
   
MaxRes=win32api.EnumDisplaySettings(None,len(VideoModes)-5)
LST=list(VideoModes)
print(LST)
##try:
##    win32api.ChangeDisplaySettings(MaxRes,0)
##    print("Установлено максимально допустимое разрешение!")
##except:
##    print("Error")
