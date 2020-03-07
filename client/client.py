import socket
import pickle
import argparse
from PIL import Image

text = 'This is a client for receiving images'
parser = argparse.ArgumentParser(description=text)
parser.add_argument("-s", '--server', help='write the server and port number seperated by : to use')
parser.add_argument("-q", '--path', help='type the path to the file to download with reference to server directory or root')

args = parser.parse_args()
path = '1.png'
if args.server:
    address =args.server.split(':')
    print('the ip and port being useed is %s' %args.server)
    port = int(address[1])
    host = address[0]
    path = args.path

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    """REQUESTING IMAGE"""
    name = path.split('/')
    print(f'requesting image at path: {path}')

    file_name = name[-1]
    s.send(path.encode('utf-8'))
    """REQUESTING IMAGE"""

    print('receiving image')
    Msg = s.recv(2)
    fullMsg = b''
    while Msg:
        fullMsg += Msg
        Msg = s.recv(1024)
    """receiving IMAGE"""
    image = open(file_name,'wb')
    image.write(fullMsg)
    """END receiving IMAGE"""
    print(f'Successfully Downloaded {file_name}')

else:
    print("use arguments as shown with -h")
