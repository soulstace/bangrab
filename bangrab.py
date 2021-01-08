import sys, socket
if len(sys.argv) < 2:
    query_host = raw_input('Enter hostname: ')
else:
    query_host = sys.argv[1]    
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((query_host, 80))
s.send('HEAD / HTTP/1.0\n\n')
data = s.recv(1024)
s.shutdown(2)
s.close()
print data
