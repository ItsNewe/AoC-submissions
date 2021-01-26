from data import day18Data

inOperation=False
opbuffer=[]



def getBracketOp(idx, i):
	nextClosingIdx= i.find(")", idx)
	tempOpBuffer=[i]
	for k in i[idx : nextClosingIdx]:
		if(not k.isspace()):
			tempOpBuffer.append(k)
			print(f"TEMP BUFFER: {tempOpBuffer}")
	result = eval(''.join(tempOpBuffer))
	print(result)
	tempOpBuffer.clear()
	return result
	
def handleChar(buffer, idx, j):
	if(j in ["+", "-", "*", "/"]):
		buffer.append(j)
		if(j=="("):
			getBracketOp(idx, i)	

for i in day18Data:
	for idx, j in enumerate(i):
		if(j.isspace()):
			continue

		elif(type(j)==int):
			opbuffer.append(j)
		elif(type(j)==str):
			handleChar()

			if(j=="("):
				getBracketOp()

				
		if(len(opbuffer)==3):
			opbuffer.clear()