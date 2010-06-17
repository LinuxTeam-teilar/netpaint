from socket import *

SrvSocket = socket(AF_INET,SOCK_DGRAM)
SrvIP = raw_input("IP Address to bind: ")
SrvPort = raw_input("Port to bind: ")

SrvAddr = (SrvIP,int(SrvPort))

SrvSocket.bind(SrvAddr)

def insertParty(value,party):
	try:
		if value not in party:
			print "Registering",value[0],"..."
			party.append(value)
			print "Added",value[0],"to current party."
	except:
		print "insertParty() FAILED!"
		pass
		
def deleteParty(value,party):
	try:
		if value in party:
			party.remove(value)
			print "Deleted",value[0],"from current party."
	except:
		print "deleteParty() FAILED!"


def broadcastExcept(data,client,party):
	print "Broadcasting..."
	for member in party:
		ss = SrvSocket.sendto(data,member)
		print "Sent",ss,"byte of data to",member[0],"!"
