import socket
import time
#import matplotlib.pyplot as plt

TCP_IP = '10.180.65.30'
TCP_PORT = 2111
BUFFER_SIZE = 10240

#start
#MESSAGE = "\x02sMN\x20LMCstartmeas\x03"

MESSAGE = "\x02sRN\x20LMDscandata\x03"
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

for x in range(1,5000):
  s.send(MESSAGE)
  #print "4"
  data = s.recv(BUFFER_SIZE)
  print data  
  #print data.split(' 21D ')[1].split(' ')
  #try:	
  #	decdata = map(lambda x: int(x,16), data.split(' 21D ')[1].split(' ')[0:-1])
  #except :
  #	print ('some error\n')
  #if len(decdata) == 546 :		
  #	print x, "recvd:", decdata[0:545:30]
  #else:
  print x, 'len: ', len(data)
  #plt.plot(data)
  #plt.show()
  time.sleep(0.02)
s.close()

