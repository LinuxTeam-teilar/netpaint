from socket import *
import net

SrvSocket = socket(AF_INET,SOCK_DGRAM)
buf = 1024
party = []

SrvIP = raw_input("IP Address to bind: ")
SrvPort = raw_input("Port to bind: ")

SrvAddr = (SrvIP,int(SrvPort))

SrvSocket.bind(SrvAddr)

while 1:
	CliData,CliAddr = SrvSocket.recvfrom(buf)
	net.insertParty(CliAddr,party)
	if not CliData:
		net.removeParty(CliAddr,party)
		print "Client exited!"
		break
	else:
		print CliAddr[0],"sent me:",CliData
		net.broadcastExcept(CliData,CliAddr,party)
		#SrvSocket.sendto(CliData,CliAddr)
		
		

SrvSocket.close()
