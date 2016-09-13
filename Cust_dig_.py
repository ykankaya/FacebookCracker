import sys,os


filepath=''
length=0
outlist=[]
if len(sys.argv) < 2:
	filepath=raw_input('Where is your file : ')
else :
	filepath=sys.argv[1]


if len(sys.argv) < 3:
	length=input('How length? :')
else :
	length=sys.argv[2]

while  length <2:
	print('Minumum length is 3 ? ')
	length=input('How length? :')

allids=0
filtered=0

if os.path.isfile(filepath):
	with open(filepath) as x :
		lines= x.readlines()
		allids=len(lines)
		for l0 in lines:
			l=l0.strip()
			if len(l) < length:
				continue
			if l in outlist:
				continue
			else :
				outlist.append(l)

else:
	print('not found file '+filepath)
	exit()

res =""
filtered=len(outlist)
for x in outlist:
	res =res+x+'\n'

if filtered > 0:
	outp=filepath.replace('.txt','')+'__'+str(filtered)+'__'+str(length)+'D__.txt'
	strm = open(outp,'w')
	strm.write(res)
	strm.close()
	print(str(filtered)+'/'+str(allids)+'\n Saved to '+outp)
else:
	print('Not saved')
