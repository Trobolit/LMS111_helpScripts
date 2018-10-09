import socket
import time
#import matplotlib.pyplot as plt

TCP_IP = '10.180.65.30' #This is the mounted LIDAR, just connect to switch with dhcp.
TCP_PORT = 2111
BUFFER_SIZE = 10240

 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

#print("log in as authorized user")
#s.send("\x02sMN SetAccessMode 03 F4724744\x03")
#data = s.recv(128)
#len(data)
#print(data)


print("\nSet to run (because documentation says to do it this way).")
print("This removes your access level, you may only request and recieve scans.")
s.send("\x02sMN Run\x03")
data = s.recv(128)
len(data)
print(data)

print("\nStart sending data continously")
s.send("\x02sEN LMDscandata 1\x03")
data = s.recv(60)
len(data)
print(data)

t = time.time()
print("\nwaiting for reboot..")
scandata = s.recv(4096*2)
#print(data)
print "waited ", time.time()-t, " seconds."

print("fetch data for 10 seconds")
n = 0
t = time.time()
while time.time() - t < 10.0 :
	scandata += s.recv(4096*4)
	n = n+1

print("\nStop sending data continously")
s.send("\x02sEN LMDscandata 0\x03")
#scandata += s.recv(4096*4) # empty buffer
#print "emptied buffer, which had ",len(scandata)," elements.\nNow waiting for last repsonse."
rdata = s.recv(4096*4) # get response to last send message
print "bytes recieved: ",len(rdata)
print(rdata.split('\x02')[-1]) # print last recieved message in buffer

nummsg = len(scandata.split("\x02"))
print "\n\nGot ",nummsg ," start of messsages"
print "which gives a rate of ", nummsg/10.0, " Hz."

