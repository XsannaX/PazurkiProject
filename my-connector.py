import mysql.connector

mydb=mysql.connector.connect(
    host='localhost',
    user='root',
    password='password',
    port='3306',
    database='pazurki'
)

mycursor=mydb.cursor()
mycursor.execute('SELECT * FROM workers')

workers=mycursor.fetchall()

for pracownik in workers:
    print(pracownik[1])