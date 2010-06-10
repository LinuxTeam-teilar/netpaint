def insertParty(value,party):
	try:
		if value in party:
			party.append(value)
	except:
		print "insertParty() FAILED!"
		
def deleteParty(value,party):
	try:
		if value in party:
			party.remove(value)
	except:
		print "deleteParty() FAILED!"


def broadcastExcept(data,client,party):
	for i in range(len(party)):
		if party[i] != client:
			sendto(data,party[i])
