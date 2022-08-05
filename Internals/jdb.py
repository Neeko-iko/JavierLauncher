import sqlite3
from sqlite3 import Error

#Connecting
def dbconnect(dbf):
  try:
    conn = sqlite3.connect(dbf)
  except Error:
    print(Error)
  else:
    return conn
db = dbconnect('./Internals/javier.db')
cursor = db.cursor()
pyColumnDict = {}

#Builds tables
def deploy():
  """
  Creates tables in the javier.db file if they do not already exist. Initializes the Settings table
  """
  cursor.execute("create table if not exists ServerList(ID integer PRIMARY KEY AUTOINCREMENT, Name text, IsFavorite integer DEFAULT 0, RAM integer DEFAULT 1, LaunchFlags text DEFAULT '' , JavaFilePath text DEFAULT '', JARName text, Port integer, Color text)")
  cursor.execute("create table if not exists ServerPaths(ID integer PRIMARY KEY AUTOINCREMENT, Path text)")
  cursor.execute("create table if not exists Settings(ID integer PRIMARY KEY AUTOINCREMENT, DefaultJava text, DefaultJRA text, DefaultRAM integer, LastVersion text, CurrentTheme text, DefaultPort integer)")
  #This is a hack solution that breaks the table if the value is > 1
  #however the only way for the table to be > 1 is if someone breaks it on purpose
  if readSettingValue('ID') != 1:
    cursor.execute("INSERT INTO Settings DEFAULT VALUES")
  db.commit()

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
  dbColumnObj = cursor.execute("SELECT * from "+name)
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
    cursor.execute("ALTER TABLE "+table+" ADD "+i+" "+typ)

#Adds a new row of servers
def addServer():
  """
  Adds a new row in the ServerList table.
  """
  cursor.execute("INSERT INTO ServerList DEFAULT VALUES")
  db.commit()

#Updates a cell of a given type from a server
def updateServerValue(name, obj, val):
  """
  Updates a value in the ServerList table. 
  
  "name" is the name of the server, "obj" is the name of the value being edited, and "val" is the new value. 
  """
  cursor.execute("UPDATE ServerList SET "+str(obj)+" = '"+str(val)+"' WHERE Name = '"+str(name)+"'")
  db.commit()

#Updates a cell of a given type from a setting
def updateSettingValue(obj, val):
  """
  Updates a value in the Settings table. 
  
  "obj" is the name of the value being edited, and "val" is the new value. 
  """
  if val == None:
    cursor.execute("UPDATE Settings SET "+str(obj)+" = NULL")
  else:
    cursor.execute("UPDATE Settings SET "+str(obj)+" = '"+str(val)+"'")
  db.commit()

def addServerPath(path: str):
  """
  Adds a new path to the ServerPaths table.
  """
  cursor.execute("INSERT INTO ServerPaths(Path) VALUES('"+path+"')")
  db.commit()

def delServerPath(path: str):
  """
  Removes a path from ServerPaths by name.
  """
  cursor.execute("DELETE FROM ServerPaths WHERE Path='"+path+"'")
  db.commit()

#Reads all data on a given server
def readServer(name):
  """
  Reads a row from the ServerList table.

  Returns a tuple with the data for a single server. The order of the data is determined by the "deploy" function.
  """
  cursor.execute("SELECT * FROM ServerList WHERE Name = '"+str(name)+"'")
  return cursor.fetchone()

#Reads all data
def readServerAll():
  """
  Reads all rows in the ServerList table. 
  
  Returns a nested tuple with the data. The order of the data is determined by the "deploy" function.
  """
  cursor.execute("SELECT * FROM ServerList")
  return cursor.fetchall()

#Function to convert the returns into linear tuples
#Removes primary key (ID)
def flatten(tot):
  r = []
  for t in tot:
    for i in t:
      if type(i) == str:
        r.append(i)
  return tuple(r)

#Selects and reads a cell by name
def readServerValue(name, obj):
  """
  Reads a specific cell from the ServerList table. 
  
  Returns a single variable or an empty tuple if the cell is empty. 
  
  "name" is the name of the server and "obj" is the value to read.
  """
  cursor.execute("SELECT "+str(obj)+" FROM ServerList WHERE Name='"+str(name)+"'")
  r = cursor.fetchone()
  if r:
    return r[0]
  else:
    return ()

def readServerPaths():
  """
  Reads all rows in the ServerPath table. 
  
  Returns a tuple with the data read. The order of the data is determined by the "deploy" function.
  """
  cursor.execute("SELECT * FROM ServerPaths")
  r = cursor.fetchall()
  if r:
    return flatten(r)
  else:
    return ()

#Selects and reads a cell by name
def readSettingValue(obj):
  """
  Reads a specific cell from the Settings table. 
  
  Returns a single variable or an empty tuple if the cell is empty. "obj" is the value to read.
  """
  cursor.execute("SELECT "+str(obj)+" FROM Settings")
  r = cursor.fetchone()
  if r:
    return r[0]
  else:
    return ()