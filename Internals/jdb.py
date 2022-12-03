import threading
from PySide6 import QtSql

########UPDATE THIS STRING WITH EVERY UPDATE###########
version='2.1.0'
#Connecting
class Connection:
  def __init__(self):
    conn = QtSql.QSqlDatabase.addDatabase("QSQLITE", str(threading.current_thread().ident))
    conn.setDatabaseName("./Internals/javier.db")
    conn.open()
    if conn.isOpen() == True:
      print("Connected!")
    else:
      print("An error has occured in the database connection process")
    self.conn = conn
  def buildquery(self):
    query = QtSql.QSqlQuery(self.conn)
    return query
  
pyColumnDict = {}

def buildquery():
  cobj = Connection()
  query = cobj.buildquery()
  return query

#Aliases
def execute(arg: str):
  query = buildquery()
  query.exec_(arg)

#Builds tables
def deploy():
  """
  Creates tables in the javier.db file if they do not already exist. Initializes the Settings table
  """
  execute("create table if not exists ServerList(ID integer PRIMARY KEY AUTOINCREMENT, Name text, IsFavorite integer DEFAULT 0, RAM integer DEFAULT 1, LaunchFlags text DEFAULT '', JavaFilePath text DEFAULT '', JARName text, Port integer, Color text)")
  execute("create table if not exists ServerPaths(ID integer PRIMARY KEY AUTOINCREMENT, Path text)")
  execute("create table if not exists Settings(ID integer PRIMARY KEY AUTOINCREMENT, DefaultJava text, DefaultJRA text, DefaultRAM integer, LastVersion text DEFAULT '"+version+"', CurrentTheme text, DefaultPort integer)")
  #This is a hack solution that breaks the table if the value is > 1
  #however the only way for the table to be > 1 is if someone breaks it on purpose
  count = buildquery() #QtSql.QSqlQuery()
  count.exec_("SELECT ID FROM Settings")
  count.first()
  if not count.isValid(): #practically stolen ! very cool.
  #if count.value(0) != 1:
    execute("INSERT INTO Settings DEFAULT VALUES")

#Function to check if DB structure needs to be updated after
#Javier is updated. The DB structure is still being decided
#so the tableCheck will always fail right now
def tableCheck(name: str, returnType=0):
  """
  Ensures that tables have all of the columns required.

  Returns True if the check passes, returns a dict containing the names of the missing columns and their data types if the check fails.

  The return type is 0 by default. If set to 1 the function will return False if the check fails instead of a dict.
  """
  dbColumnList = []
  pyColumnList = list(pyColumnDict.keys())
  dbColumnObj = execute("SELECT * from "+name)
  for i in dbColumnObj.description:
    dbColumnList.append(i[0])
  if dbColumnList == pyColumnList:
    return True
  else:
    if returnType == 1:
      return False
    missingColumns = []
    for i in pyColumnList:
      if i not in dbColumnList:
        missingColumns.append(i)
    return tuple(missingColumns)

#Adds missing columns to a table
def repairTable(table, missingColumns):
  for i in missingColumns:
    typ = pyColumnDict[i]
    execute("ALTER TABLE "+table+" ADD "+i+" "+typ)

#Adds a new row of servers
def addServer(name):
  """
  Adds a new row in the ServerList table.
  """
  execute("INSERT INTO ServerList (name) values ('"+name+"')")
  

#Updates a cell of a given type from a server
def updateServerValue(name, obj, val):
  """
  Updates a value in the ServerList table. 
  
  "name" is the name of the server, "obj" is the name of the value being edited, and "val" is the new value. 
  """
  execute("UPDATE ServerList SET "+str(obj)+" = '"+str(val)+"' WHERE Name = '"+str(name)+"'")
  

#Updates a cell of a given type from a setting
def updateSettingValue(obj, val):
  """
  Updates a value in the Settings table. 
  
  "obj" is the name of the value being edited, and "val" is the new value. 
  """
  if val == None:
    execute("UPDATE Settings SET "+str(obj)+" = NULL")
  else:
    execute("UPDATE Settings SET "+str(obj)+" = '"+str(val)+"'")
  

def addServerPath(path: str):
  """
  Adds a new path to the ServerPaths table.
  """
  execute("INSERT INTO ServerPaths(Path) VALUES('"+path+"')")
  

def delServerPath(path: str):
  """
  Removes a path from ServerPaths by name.
  """
  execute("DELETE FROM ServerPaths WHERE Path='"+path+"'")
  

#Reads all data on a given server
def readServer(name):
  """
  Checks to see if a server exists
  """
  query = buildquery()
  query.setForwardOnly(True)
  query.exec_("SELECT ID FROM ServerList WHERE Name = '"+str(name)+"'")
  query.first()
  if query.isValid():
    return True
  else:
    return False

#Here lies the flatten function, may it Rest in Peace

#Selects and reads a cell by name
def readServerValue(name, obj):
  """
  Reads a specific cell from the ServerList table. 
  
  Returns a single variable. 
  
  "name" is the name of the server and "obj" is the value to read.
  """
  query = buildquery()
  query.setForwardOnly(True)
  query.exec_("SELECT "+str(obj)+" FROM ServerList WHERE Name='"+str(name)+"'")
  query.first()
  return query.value(0)

def readServerPaths():
  """
  Reads all rows in the ServerPath table. 
  
  Returns a tuple with the data read. The order of the data is determined by the "deploy" function.
  """
  rtn = []
  query = buildquery()
  query.setForwardOnly(True)
  query.exec_("SELECT Path FROM ServerPaths")
  while query.next():
    rtn.append(query.value(0))
  return tuple(rtn)


#Selects and reads a cell by name
def readSettingValue(obj):
  """
  Reads a specific cell from the Settings table. 
  
  Returns a single variable. 
  
  "obj" is the value to read.
  """
  query = buildquery()
  query.setForwardOnly(True)
  query.exec_("SELECT "+str(obj)+" FROM Settings")
  query.first()
  return query.value(0)



#This is for the progress bar
def progInit():
  global jsize
  jsize = 0
  global jfin
  jfin = 0
  global jready
  jready = 0