import mysql.connector

conn = mysql.connector.connect(user='root', password='password', database='test')
cursor = conn.cursor()

cursor.execute('create table user (id varchar(20) primary key, name varchar(40))')

cursor.execute('insert into user values (%s,%s)',['1','michael'])
cursor.rowcount

conn.commit()
cursor.close()

cursor = conn.cursor()
cursor.execute('select * from user')
values = cursor.fetchall()
print(values) 
cursor.close()
conn.close()