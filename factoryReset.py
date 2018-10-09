import socket
import time

TCP_IP = '10.180.65.30' #This is the mounted LIDAR, just connect to switch with dhcp.
TCP_PORT = 2111
BUFFER_SIZE = 10240

 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

print("\nlog in as service  user (strongest)")
s.send("\x02sMN SetAccessMode 04 81BE23AA\x03")
data = s.recv(128)
len(data)
print(data)

print "\nload/reset to factory defualts"
s.send("\x02sMN mSCloadfacdef\x03")
data = s.recv(128)
len(data)
print(data)
