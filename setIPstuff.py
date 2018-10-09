import socket
import time

#TCP_IP = '10.180.65.30' #This is the mounted LIDAR, just connect to switch with dhcp.
#TCP_IP = '192.168.0.250' # This is Dariuszs lidar, use the static ip config.
TCP_IP = '192.168.0.1' # This is factory default, use after factory reset.
TCP_PORT = 2111
BUFFER_SIZE = 10240

 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))
 
print "log in as service user (strongest)"
s.send("\x02sMN SetAccessMode 04 81BE23AA\x03")
data = s.recv(128)
len(data)
print(data)

print "\nSet IP of LIDAR"
s.send("\x02sWN EIIpAddr 0A B4 41 1E\x03") # IP of 10.180.65.30
data = s.recv(128)
len(data)
print(data)

print "set gateway in lidar"
s.send("\x02sWN EIgate 0A B4 41 11\x03") # Gateway of 10.180.65.17
data = s.recv(128)
len(data)
print data

print "set subnet mask (important, not standard on permocar!)"
s.send("\x02sWN EImask FF FF FF F0\x03")
data = s.recv(128)
print data
print("\nStore config on lidar")

print "Store config on lidar in static memory"
s.send("\x02sMN mEEwriteall\x03")
data = s.recv(128)
len(data)
print(data)

print "Send run command, i.e. log out"
s.send("\x02sMN Run\x03")
data = s.recv(128)
len(data)
print(data)

print "Remember to reboot LIDAR now!"
s.close()

