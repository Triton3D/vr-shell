import psutil




def CheckProcStatus(proc_name):
    for process in psutil.process_iter():
        if process.name()  == proc_name:
            print(True)
        else:
            print("Proccess {} is not running!".format(proc_name))
            return False    
##    for process in psutil.process_iter():
##        if process.name() == proc_name:
##            print("Proccess {} is running!".format(proc_name))
##            return True
##        else:
##            print("Proccess {} is not running!".format(proc_name))
##            return False
CheckProcStatus("explorer.exe")
