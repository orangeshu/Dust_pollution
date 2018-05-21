#服务器端
import socket

import argparse

import random
import time
import MySQLdb



host = '0.0.0.0'

data_payload = 2048 #一次性接收或者发送的字节数

backlog = 5 #控制连接的个数，出现第6个请求就会拒绝

ack = '23.24'



def echo_server(port):

    sock = socket.socket(socket.AF_INET, socket. SOCK_STREAM)
    #Address Family:可以选择AF_INET（用于internet进程间通信）或者AF_UNIX（用于同一台机器进程间通信）
    #Type:套接字类型，可以是SOCKET_STREAM（流式套接字，主要用于TCP协议）或者SOCKET_DGRAM（数据报套接字，主要用于UDP协议）

    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = (host, port)

    print "Starting up echo server on %s port %s" % server_address

    sock.bind(server_address) #绑定到特定的地址以及端口上

    sock.listen(backlog) #监听连接




    print 'Waiting to receiving message from client'

    client, address = sock.accept() #接收连接

    data = client.recv(data_payload) 

    if data:

        print 'Data: %s' % data

        now=time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())

        client.send(ack)

        print 'Sent: %s back to %s' % (ack, address)

    client.close()
    db = MySQLdb.connect(
    host="localhost", 
    db="PM_25",
    user="root", 
    passwd="111111", 
    charset='utf8'
    )

    cursor=db.cursor()
    try:
	sql = "INSERT INTO PM_25_table (id,recordtime,value) VALUES ('%s','%s','%s')" %(0,now,data)
	cursor.execute(sql)
	db.commit()
        print("insert ok")
    except:
	print("insert failed")
    db.close()




if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Socket Server Example')

    parser.add_argument('--port', action='store', dest='port', type=int, required=True)

    given_arg = parser.parse_args()

    port = given_arg.port

    while 1:    
	echo_server(port)

