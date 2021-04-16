import _socket
import threading

def sending():   #Behaves like Client
    s=_socket.socket(_socket.AF_INET,_socket.SOCK_DGRAM)
    winip="192.168.1.4"
    winport=50036
    while True:
        msg=input("Enter the message you want to send:")
        s.sendto(msg.encode(),(winip,winport))


def receiving():   #Behaves like Server
    s=_socket.socket(_socket.AF_INET,_socket.SOCK_DGRAM)
    linuxip="192.168.1.6"
    linuxport=1234
    s.bind((linuxip,linuxport))
    while True:
        x=s.recvfrom(1024)
        print()
        print("From Windows:",x[0].decode())


x1=threading.Thread(target=receiving)
x2=threading.Thread(target=sending)

x1.start()
x2.start()