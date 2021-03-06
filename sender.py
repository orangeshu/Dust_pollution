#客户端

'''
1.创建socket
2.连接到远程服务器
3.发送数据
4.接收数据
5.关闭socket

'''
import socket

import argparse

import random

import time

host = '192.168.31.211'

data_payload = 128





def echo_client(port):

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    

    server_address = (host, port)

    print 'Connecting to %s port %s' % server_address

    sock.connect(server_address)



    try:

        message = str(random.randint(10,100))

        print 'Sending: %s' % message

        sock.sendall(message) #发送数据

        amount_received = 0

        data = sock.recv(data_payload)

        #   amount_received += len(data)

        print 'Received: %s' % data

    except socket.errno, e:

        print 'socket error: %s' % str(e)

    except Exception, e:

        print 'Other error happened: %s' % str(e)

    finally:

        print 'Closing connection to the server'

        sock.close()



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Socket Server Example')

    parser.add_argument('--port', action="store", dest='port', type=int, required=True)

    given_args = parser.parse_args()

    port = given_args.port

    while 1 :
	echo_client(port)

	time.sleep(10)
