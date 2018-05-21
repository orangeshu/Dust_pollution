#服务器端
import socket

import argparse

import random
import time
import MySQLdb



host = '0.0.0.0'

data_payload = 2048

backlog = 5

ack = '23.24'



def echo_server(port):

    sock = socket.socket(socket.AF_INET, socket. SOCK_STREAM)


    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    server_address = (host, port)

    print "Starting up echo server on %s port %s" % server_address

    sock.bind(server_address)

    sock.listen(backlog)




    print 'Waiting to receiving message from client'

    client, address = sock.accept()

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

