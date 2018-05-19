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
	

#sudo apt-get install python-server   #下载mysql
#sudo apt-get install python-mysqldb  #python调用mysql
#mysql -u root -p  #进入mysql
#mysql>shou databases;  #展示当前已经建立的数据库
#mysql>create database one; #建立一个叫one的数据库
#mysql>use one;  #进入one数据库
#mysql>create table data(id int(4) auto_increment primary key not null,nongdu float(4,2) not null,created_time datetime not null);  #建立一个叫data的表，表中第一列为id，id自动更新；第二列为nongdu，四位数，小数点后两位；第三列为created_time.
#mysql>show tables;  #展示当前已经建立的表单
#mysql>describe data;  #查看表单的内容
#mysql>insert into data values(0,48.97,'2018-05-19 17:00:00');  #向数据库中插入数据
#mysql>select * from data; #检查数据是否插入成功
#mysql>drop table data;  #删除叫data的表单






