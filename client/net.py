from socket import *

buf = 1024
SrvIP = raw_input("Server IP: ")
SrvPort = int(raw_input("Server port: "))

CliSocket = socket(AF_INET,SOCK_DGRAM)
CliSocket.setblocking(0)
SrvAddr = (SrvIP,SrvPort)

CliSocket.settimeout(0.2)
