import psutil
import time
def CheckProcStatus(proc_name='explorer.exe'):
    for process in psutil.process_iter():
        if process.name() == proc_name:
            #print("Proccess {} is running!".format(proc_name))
            return True
CheckProcStatus()
flag=False
flag2=False
while True:
    time.sleep(1)
    if CheckProcStatus('notepad.exe') and flag==False:
        print("Notepad has been started ")
        flag=True 
    elif flag==True and not CheckProcStatus('notepad.exe'):
        flag=False
        flag2=False
        print("Notepad has been stopped")
    elif flag==False and flag2==False:
        print("Waiting")
        flag2=True
    
