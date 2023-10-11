import mysql.connector


dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'root',
    passwd = 'pavan@1619'
    
)

cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE DCRMDATABASE")

print("database is created")