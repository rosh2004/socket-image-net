import socket
import argparse

text = 'This is a server for sending images'
parser = argparse.ArgumentParser(description=text)
parser.add_argument("-p", '--port', help='write the port number to use')
args = parser.parse_args()

if args.port:
    print('the port being useed is %s' %args.port)
    port = int(args.port)
else:
    print('the default port is 2345')
    port = 2345


host = socket.gethostname()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)
s.bind((host,port))
s.listen(5)
print(f'listening on address {host}:{port}')

clientSock, addr = s.accept()
print(f'Connected to a client at addr: {addr}')

"""REQUESTING IMAGE BY PATH"""
path = clientSock.recv(1024).decode('utf-8')
print(f'Path for file received as: {path}')
"""END REQUESTING IMAGE BY PATH"""

"""CONVERTING IMAGE TO BYTES"""
image = open(path, 'rb')
imageBinary = image.read()
"""END CONVERTING IMAGE TO BYTES"""

msg = imageBinary
print("Sending file")
clientSock.sendall(msg)
s.close()