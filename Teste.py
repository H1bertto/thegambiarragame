import mysql.connector


mydb = mysql.connector.connect(
    user='humberto',
    password='PSWD',
    host='IP',
    port='5000',
    database='rank')


mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
    print(x)

mydb.close()
