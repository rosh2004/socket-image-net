import socket
import argparse
from PIL import Image
import pickle

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
s.bind((host,port))
s.listen(5)
print(f'listening on address {host}:{port}')

clientSock, addr = s.accept()
print(f'Connected to a client at addr: {addr}')

"""CONVERTING IMAGE TO BYTES/PICKLING"""
image = Image.open('1.png')
imageBinary = pickle.dumps(image)

"""END CONVERTING IMAGE TO BYTES"""

msg = imageBinary
clientSock.sendall(msg)
s.close()