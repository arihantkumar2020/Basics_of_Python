#connector is needed to connect db or dbms to python
#ex : mysql connector to work with mysql dbms
#pip install mysql-connector-python

import mysql.connector

mydb = mysql.connector.connect(host = 'localhost', user = 'arihant', passwd = 'iamadmin@2020', database = 'arihant', auth_plugin = 'mysql_native_password')
#database and auth_plugin are optional
#connect() gives database connection

mycursor = mydb.cursor()
#cursor() references to the database

mycursor.execute('select * from student;')

result = mycursor.fetchall()    #fetchone() can be used as well

mydb.close()

for i in result:
    print(i)