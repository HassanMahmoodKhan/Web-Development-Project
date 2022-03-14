import pymysql

conn = pymysql.connect(
    host = "database01.c5cpvw4flban.us-east-1.rds.amazonaws.com" ,
    user = "admin" ,
    password =  "BANNU2001200" ,
    port = 3306 
)

cur=conn.cursor()
cur.execute("SELECT * FROM DATABASEPROJ.train_data WHERE departure= 'Toronto' AND arrival= 'Montreal' AND departure_time= '9:00'");   
details = cur.fetchall()




