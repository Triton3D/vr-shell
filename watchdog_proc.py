import psutil
from datetime import datetime,date,time
import time
import psycopg2

DB_NAME='postgres'
USER_NAM='postgres'
PASSWORD='QwertyS123!'
HOST_ADR='92.43.187.233'
PORT_NUMB='5432'

def CheckProcStatus(proc_name='explorer.exe'):
    for process in psutil.process_iter():
        if process.name() == proc_name:
            return True

def CheckInternetConnection():
    cmd = 'ping ya.ru'
    import subprocess
    PIPE = subprocess.PIPE
    p = subprocess.Popen(cmd, shell=True, stdin=PIPE, stdout=PIPE,
            stderr=subprocess.STDOUT)
    buf = p.stdout.read()
    return 'TTL' in str(buf)
#def WriteToDB(db)

proc_start=False
proc_none=False
proc_run=False
pattern=('notepad.exe','calc.exe','mspaint.exe')
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
        con = psycopg2.connect(database=DB_NAME,user=USER_NAM,password=PASSWORD,host=HOST_ADR,port=PORT_NUMB)   #Connect to DB
        with con:
            cur=con.cursor()
            cur.execute("CREATE TABLE IF NOT EXISTS Processes(Name text,StartTime timestamp without time zone,StopTime timestamp without time zone,Duration time without time zone)")
            cur.execute("INSERT INTO Processes VALUES('"+proc_name+"','"+start_time+"','"+stop_time+"','"+duration+"')")
        con.close()
    elif not proc_start and not proc_none:                   #Waiting for the process
        print("Waiting for the process!")
        proc_none=True
   # print("End: "+str(datetime.now()))

