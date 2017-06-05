import psutil
from datetime import datetime,date,time
import time
import sqlite3 as lite

def CheckProcStatus(proc_name='explorer.exe'):
    for process in psutil.process_iter():
        if process.name() == proc_name:
            return True
#def WriteToDB(db)

proc_start=False
proc_none=False
proc_run=False
pattern=('notepad.exe','calc.exe','mspaint.exe','cmd.exe')
proc_name=""
while True:
    time.sleep(2)
    #print("Begin: "+str(datetime.now()))
    for proc in pattern:
            if CheckProcStatus(proc):
                proc_name=proc
                break
    proc_run=CheckProcStatus(proc_name)   
    if proc_run and proc_start==False:     #Getting the process start state and start time
        start_time=datetime.now()
        print("Process " +proc_name+ " has been started at " + str(start_time))
        proc_start=True
            
    elif proc_start and not proc_run: #Getting the process stop state and stop time
        proc_start=False
        proc_none=False
        stop_time=datetime.now()
        duration=stop_time-start_time
        #print(str(duration)[:-7])
        print("Process " +proc_name+ " has been stopped at " + str(stop_time)+" Duration: "+str(duration))

        start_time=str(start_time)[:-7]
        stop_time=str(stop_time)[:-7]
        duration=str(duration)[:-7]
        con = lite.connect('sqlite\\processes.db')   #Write to DB
        with con:
            cur=con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Processes(Id INT,Name TEXT,StartTime DATETIME,StopTime DATETIME,Duration DATETIME)")
            cur.execute("INSERT INTO Processes VALUES(1,'"+proc_name+"','"+start_time+"','"+stop_time+"','"+duration+"')")

    elif not proc_start and not proc_none:                   #Waiting for the process
        print("Waiting")
        proc_none=True
   # print("End: "+str(datetime.now()))

