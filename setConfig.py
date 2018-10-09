import socket
import time

TCP_IP = '10.180.65.30' #This is the mounted LIDAR, just connect to switch with dhcp.
#TCP_IP = '192.168.0.250' # This is Dariuszs lidar, use the static ip config.
#TCP_IP = '192.168.0.1' # This is factory default
TCP_PORT = 2111
BUFFER_SIZE = 10240

 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

print("log in as authorized user")
s.send("\x02sMN SetAccessMode 03 F4724744\x03")
data = s.recv(128)
len(data)
print(data)

#print("\nlog in as service  user")
#s.send("\x02sMN SetAccessMode 04 81BE23AA\x03")
#data = s.recv(128)
#len(data)
#print(data)

#print "\nload/reset to factory defualts"
#s.send("\x02sMN mSCloadfacdef\x03")
#data = s.recv(128)
#len(data)
#print(data)

print("\nset good config for 50Hz, maximum scan area and 0.5 deg resolution.")
s.send("\x02sMN mLMPsetscancfg +5000 +1 +5000 -450000 +2250000\x03")
data = s.recv(128)
len(data)
print(data)

print("\nSet scandatacfg to channel 1, remission yes, remission resolution 16 bits, [...]")
print("[...] no encoder data, no comment, name or time data, and send every scan.")
s.send("\x02sWN LMDscandatacfg 01 00 1 1 0 00 00 0 0 0 0 +1\x03")
data = s.recv(128)
len(data)
print(data)

print "\nmake sure mean filter is off"
s.send("\x02sWN LFPmeanfilter 0 +20 0\x03")
data = s.recv(128)
len(data)
print(data)

print "\nmake sure nto1 filter is off"
s.send("\x02sWN LFPnto1filter 0\x03")
data = s.recv(128)
len(data)
print(data)

# It seems below piece is not needed, only keeping here in case stuff doesnt work in a year.
#print("\nensure accesslogin for next command (probably not needed)")
#s.send("\x02sMN SetAccessMode 03 F4724744\x03")
#data = s.recv(128)
#len(data)
#print(data)

print("\nStore config on lidar")
s.send("\x02sMN mEEwriteall\x03")
data = s.recv(128)
len(data)
print(data)

print("\nSet to run (because documentation says to do it this way).")
print("This removes your access level, you may only request and recieve scans.")
s.send("\x02sMN Run\x03")
data = s.recv(128)
len(data)
print(data)


s.close()
