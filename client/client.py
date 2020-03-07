import socket
import pickle
import argparse
from PIL import Image

text = 'This is a client for receiving images'
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
s.connect((host, port))
Msg = s.recv(2)
fullMsg = b''
while Msg:
    fullMsg += Msg
    Msg = s.recv(1024)
"""UNPICKLING IMAGE"""
img = pickle.loads(fullMsg)
img.show()

"""END UNPICKLING IMAGE"""



