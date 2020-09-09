import struct
import sys

#initialize the 'fileName' list with file names for, xi, eta, Dg, and GH
fileName = "", "", "", ""
fileContent = []
numbytes = []
for z in fileName:
	with open(z, mode='rb') as file: 
		v = file.read()
		fileContent.append(v)
		numbytes.append(int(len(v)/4))#the four comes from the buffer size of float byte



#the below variables of xi, eta, Dg, GH are the parsed float values
xi = struct.unpack(str(numbytes[0])  + 'f', fileContent[0][0:4*int(numbytes[0])])
eta = struct.unpack(str(numbytes[1])  + 'f', fileContent[1][0:4*int(numbytes[1])])
Dg = struct.unpack(str(numbytes[2])  + 'f', fileContent[2][0:4*int(numbytes[2])])
GH = struct.unpack(str(numbytes[3])  + 'f', fileContent[3][0:4*int(numbytes[3])])


#the below portion is just for writing the floats to text files, it takes a couple of minutes for each file
ans = input("Write data to txt file? (y/n)")

if (ans == 'y'):
	xi_data = open(fileName[0].replace('.', '')+'.txt','w')
	xi_data.write('\n')
	for x in xi:
		xi_data.write(str(x))
		xi_data.write('\n')
		
	xi_data.close()


	eta_data = open(fileName[1].replace('.', '')+'.txt','w')
	eta_data.write('\n')
	for x in eta:
		eta_data.write(str(x))
		eta_data.write('\n')
		
	eta_data.close()


	Dg_data = open(fileName[2].replace('.', '')+'.txt','w')
	Dg_data.write('\n')
	for x in Dg:
		Dg_data.write(str(x))
		Dg_data.write('\n')
	
	Dg_data.close()


	GH_data = open(fileName[3].replace('.', '')+'.txt','w')
	GH_data.write('\n')
	for x in GH:
		GH_data.write(str(x))
		GH_data.write('\n')
	
	GH_data.close()

sys.exit()
