import psutil
from datetime import datetime,date,time
import time
def CheckProcStatus(proc_name='explorer.exe'):
    for process in psutil.process_iter():
        if process.name() == proc_name:
            #print("Proccess {} is running!".format(proc_name))
            return True

def GetTime():
    time_list=list(time.localtime())[0:6]
    time_string=""
    time_string=str(time_list[0])+"/"+str(time_list[1])+"/"+str(time_list[2])+"; "+ \
                 str(time_list[3])+":"+str(time_list[4])+":"+str(time_list[5])
    return time_string

##CheckProcStatus()
flag=False
flag2=False
while True:
    time.sleep(1)
##    print(GetTime())
    if CheckProcStatus('notepad.exe') and flag==False:
        start_time=datetime.now()
        print("Notepad has been started at " + str(start_time))
       
        flag=True
        
    elif flag==True and not CheckProcStatus('notepad.exe'):
        flag=False
        flag2=False
        stop_time=datetime.now()
        duration=stop_time-start_time
        print("Notepad has been stopped at " + str(stop_time)+" Duration: "+str(duration))
        
        
    elif flag==False and flag2==False:
        print("Waiting")
        flag2=True
    
print(GetTime())
