import sys,os

filepath=''


if len(sys.argv) <2 :
	filepath=raw_input('Where is your FIle ?')
else :
	filepath=sys.argv[1]

if os.path.isfile(filepath)==False:
	print('File not found ')
	exit()

cont=''
allids=0
filtered=0

with open(filepath) as strm:
	lines=strm.readlines()
	allids=len(lines)
	for l in lines:
		lx=l.strip()
		if lx.isdigit():
			cont=cont+lx+'\n'
			filtered=filtered+1

output=filepath.replace('.txt','')+'___NumbersOnly_.txt'
if filtered>0:
	strm2=open(output,'w')
	strm2.write(cont)
	strm2.close()
	print(str(filtered)+'/'+str(allids))
	print('\nSaved at '+output)

