import net

buf = 15000
party = []

while 1:
	CliData,CliAddr = net.SrvSocket.recvfrom(buf)
	net.insertParty(CliAddr,party)
	if not CliData:
		net.removeParty(CliAddr,party)
		print "Client exited!"
		break
	else:
		print CliAddr[0],"sent me:",CliData
		net.broadcastExcept(CliData,CliAddr,party)
		#SrvSocket.sendto(CliData,CliAddr)
		
		

net.SrvSocket.close()
