import mysql.connector

mydb = mysql.connector.connect(
    host="localhost", 
    user="root", 
    passwd="123456",
    database="bookdata" 
    )

mycursor = mydb.cursor()
sqlformula = "INSERT INTO books (Name, Category) VALUES (%s, %s)"
# mycursor.execute(sqlformula)
mydb.commit()