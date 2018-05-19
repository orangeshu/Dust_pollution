import MySQLdb
import time
import random

data=random.randint(10,100)
now=time.strftime('%Y-%m-%d ',time.localtime())


print data,now

db = MySQLdb.connect(
	host="localhost", 
	db="PM_25",
	user="root", 
	passwd="111111", 
        charset='utf8'
	)

cursor=db.cursor()


sql = "INSERT INTO PM_25_table (recordtime,value,id) VALUES ('%s','%s')" %(now,data)

cursor.execute(sql)


db.commit()

db.close()
	

