import mysql.connector


mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="123456", 
    database="testdb"   
)

mycursor = mydb.cursor()
sqlFormula = "INSERT INTO list_of_books (name, category) VALUES (%s, %s)"
# mycursor.execute(sqlFormula, data)
mydb.commit()
