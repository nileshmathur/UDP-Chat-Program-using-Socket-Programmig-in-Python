import socket
import threading

def sending():   #Behaves like client
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    linuxip="192.168.1.6"
    linuxport=1234
    while True:
        print()
        msg=input("Enter the message you want to send:")
        s.sendto(msg.encode(),(linuxip,linuxport))
        print()
	


def receiving():   #Behaves like Server
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    winip="192.168.1.4"
    winport=50036
    s.bind((winip,winport))
    while True:
        x=s.recvfrom(1024)
        print()
        print("From Linux:",x[0].decode())
        print()
    
    
x1=threading.Thread(target=sending)       #Declaring them as Threads
x2=threading.Thread(target=receiving)
    
x1.start()                     #Starting the Threads
x2.start()
    