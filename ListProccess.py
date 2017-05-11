import subprocess
import sqlite3 as lite
import sys
pattern=['AEADISRV.EXE','firefox.exe']
row_headers=['HandleCount','Name','Priority','ProcessId','ThreadCount','WorkingSetSize','\\r\\r\\n']
row_dimensions=[]
list_processes_str=[]
list_to_db=[]
out = subprocess.Popen('wmic /node:localhost process list brief', shell=True, stdout=subprocess.PIPE)
list_processes=out.stdout.readlines()
for i in range(len(row_headers)-1,-1,-1):
    name=row_headers[i]
    start_pos=str(list_processes[0]).find(row_headers[i])
    try:
        end_pos=str(list_processes[0]).find(row_headers[i+1])-1
    except:
        end_pos=len(list_processes[0])
    entry=(i,name,start_pos,end_pos)
    row_dimensions.append(entry)
row_dimensions.reverse()
row_dimensions=row_dimensions[:len(row_headers)-1]   
#print(row_dimensions)

for item in list_processes:
    cur_col=[]
    for i in range(0,len(row_dimensions),1):
        content=str(item)[int(row_dimensions[i][2]):int(row_dimensions[i][3])].replace(' ','') 
        cur_col.append(content)
    list_processes_str.append(cur_col)
con = lite.connect('sqlite\\test.db')
##
with con:
    cur=con.cursor()
    cur.execute("DROP TABLE IF EXISTS Processes")
    cur.execute("CREATE TABLE Processes(Name TEXT,WorkingSetSize INT)")
    for item in list_processes_str:
        list_to_db=[]
        if item[1] in pattern:
              cur.execute("INSERT INTO Processes VALUES('"+item[1]+"',"+item[5]+")")
##            cur.execute("INSERT INTO Processes VALUES("+item[1]+","+item[5]+")")
                            
## cur.execute("INSERT INTO Cars VALUES(1,'Audi',52642)")
            
          #   print(item[1])
    ##       if .=='explorer.exe':
##               print(item[1]+","+item[5])
#              print(type(item[1]+","+item[5]))
##               list_to_db.append(item[1])
##               list_to_db.append(item[5])
####               print(list_to_db)
##               
##               print("Data has been writen to db: "+item[1]+","+item[5])
####               list_to_db.append(item[1]+","+item[5]) 
##           
11
