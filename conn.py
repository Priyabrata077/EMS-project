import mysql.connector
conn=mysql.connector.connect(host='localhost',username='root',password='priya@123',database='employee1')
my_cursor=conn.cursor()
coo.commit()
conn.close
print("Connection succefully created")