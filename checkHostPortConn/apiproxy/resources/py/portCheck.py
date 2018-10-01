import socket

HOST = str(flow.getVariable("hostip"))
PORT = int(flow.getVariable("port")) 

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
result = sock.connect_ex((HOST, PORT))
if result == 0:
   print "Port is open"
   flow.setVariable("temp", 'Port is open');
else:
   print "Port is not open"
   flow.setVariable("temp", 'Port is not open');