import sqlite3
from sqlite3 import Error
from inspect import currentframe

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

#Builds tables
def deploy():
  """
  Creates tables in the javier.db file if they do not already exist.
  """
  cursor.execute("create table if not exists ServerList(ID integer PRIMARY KEY AUTOINCREMENT, Name text, IsFavorite integer, RAM integer, LaunchFlags text, JavaFilePath text, JARName text)")
  cursor.execute("create table if not exists ServerPaths(ID integer PRIMARY KEY AUTOINCREMENT, Path text")
  cursor.execute("create table if not exists Settings(ID integer PRIMARY KEY AUTOINCREMENT, DefaultJava text, DefaultRAM integer, LastVersion text)")
  db.commit()

#Function to check if DB structure needs to be updated after
#Javier is updated. Currently a stub.
def tableCheck():
  """
  Ensures that tables have all of the columns required.
  """
  lineNum = lambda : currentframe().f_back.f_lineno
  print("Function 'tableCheck'(Line ", lineNum, ") is currently a stub")


#Updates a cell of a given type from a server
def updateServerValue(name, obj, val):
  """
  Updates a value in the ServerList table. 
  
  "name" is the name of the server, "obj" is the name of the value being edited, and "val" is the new value. 
  """
  cursor.execute("UPDATE ServerList SET "+str(obj)+" = '"+str(val)+"' WHERE Name = '"+str(name)+"'")
  db.commit()

#Updates a cell of a given type from a setting
def updateSettingValue(name, obj, val):
  """
  Updates a value in the Settings table. 
  
  "name" is the name of the server, "obj" is the name of the value being edited, and "val" is the new value. 
  """
  cursor.execute("UPDATE Settings SET "+str(obj)+" = '"+str(val)+"' WHERE Name = '"+str(name)+"'")
  db.commit()

def addServerPath(path: str):
  """
  Adds a new path to the ServerPaths table.
  """
  cursor.execute("INSERT INTO ServerPaths(Path) VALUES(?)", path)
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

#Selects and reads a cell by name
def readServerValue(name, obj):
  """
  Reads a specific cell from the ServerList table. 
  
  Returns a single variable. "name" is the name of the server and "obj" is the value to read.
  """
  cursor.execute("SELECT "+str(obj)+" FROM ServerList WHERE Name='"+str(name)+"'")
  r = cursor.fetchone()
  return r[0]

def readServerPaths():
  """
  Reads all rows in the ServerPath table. 
  
  Returns a tuple with the data. The order of the data is determined by the "deploy" function.
  """
  cursor.execute("SELECT * FROM ServerPaths")
  r = cursor.fetchall()
  return r[0]

#Selects and reads a cell by name
def readSettingValue(obj):
  """
  Reads a specific cell from the Settings table. 
  
  Returns a single variable. "obj" is the value to read.
  """
  cursor.execute("SELECT "+str(obj)+" FROM Settings WHERE ID='1'")
  r = cursor.fetchone()
  return r[0]