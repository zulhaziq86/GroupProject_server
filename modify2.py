import socket
import sys
import time
import errno
import math
from multiprocessing import Process

ok_message = 'HTTP/1.0 200 OK\n\n'
nok_message = 'HTTP/1.0 404 NotFound\n\n'

def process_start(s_sock,s_addr):
    s_sock.send(str.encode('Welcome to the Golong Restaurant\n'))
    while True:
        data = str(s_sock.recv(2048).decode())
        print(data)
        op,tabl,quant,totp = data.split('.')
        if op == "NL":
            print(str(s_addr) + "Table " + tabl + " Ordered " + quant + " Nasi lemak ")
            line = "\n_____________________________________________________________\n"

            jawapan = "\nTotal Price : RM" + totp + line
            s_sock.send(str.encode(jawapan))
        elif op == "S":
            print(str(s_addr) + "Table " + tabl + " Ordered " + quant + " Sate")
            line = "\n__________________________________________________________\n"

            jawapan = "\nTotal Price : RM" + totp + line
            s_sock.send(str.encode(jawapan))
        elif op == "NA":
            print(str(s_addr) + "Table " + tabl + " Ordered " + quant + " Nasi Ayam")
            line = "\n______________________________________________________________\n"

            jawapan = "\nTotal Price : RM" + totp + line
            s_sock.send(str.encode(jawapan))
        elif op == "Q":
            print(str(s_addr) + "Finish order")
            s_sock.close()
if __name__ == '__main__':
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("",8888))
    print("listening...")
    s.listen(3)
    try:
        while True:
            try:
                s_sock, s_addr = s.accept()
                p = Process(target=process_start, args=(s_sock,s_addr))
                p.start()

            except socket.error:

                print('socket error')

    except Exception as e:
        print('an exception occurred!')
        print(e)
        sys.exit(1)
    finally:
     	s.close()
