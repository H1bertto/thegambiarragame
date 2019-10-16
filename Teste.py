import mysql.connector


mydb = mysql.connector.connect(
    user='humberto',
    password='321',
    host='35.238.222.170',
    port='5000',
    database='rank')


mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

mydb.close()
