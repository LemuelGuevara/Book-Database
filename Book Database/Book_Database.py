import mysql.connector

mydb = mysql.connector.connect(host="localhost", 
    user="root", 
    passwd="123456", 
    database="testdb"
    )

mycursor = mydb.cursor()

sqlformula = "INSERT INTO books (name, category) VALUES (%s, %s)"

mycursor.execute(sqlformula)
myresult = mycursor.fetchall()
# mydb.commit()

