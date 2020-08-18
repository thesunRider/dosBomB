import requests,nmap,asyncio,time,threading,configparser

from loader_main import *
from scapy.all import *

import sys
sys.path.append('./gui/modules/general/')

loop = asyncio.get_event_loop()

async def _nmapscan(target_ip,port_range=''):
	print('started portscan')
	nm = nmap.PortScanner()
	if port_range == '' :
		result = await loop.run_in_executor(None, nm.scan,target_ip)
	else :
		result = await loop.run_in_executor(None, nm.scan,target_ip,port_range)
		
	print('finished portscan')
	return result

async def _makepacketrequest(target_ip,srcport,dstport,fla="S",tmt=2):
	p = IP(dst=target_ip)/TCP(sport=srcport,dport=dstport,flags=fla)
	ans, unans = await loop.run_in_executor(None,sr,p,timeout=tmt)
	try:
		return ans[0][1].time - p.sent_time 
	except Exception as e:
		return False
	
#false is get request,true is post request
async def _makerequest(url,type,post_fields='',tim=10):
	print('started request')
	loop = asyncio.get_running_loop()
	if type :
		
		response = await loop.run_in_executor(None,requests.post,url, data=post_fields, timeout=tim)
	else :
		response = await loop.run_in_executor(None,requests.get,url)
	print('finished request')
	return response.elapsed.total_seconds()


async def main():
	res1 = loop.create_task(_makerequest("https://www.google.com",False))
	res2 = loop.create_task(_nmapscan('127.0.0.1'))

	while 1:
		if res1.done() and res2.done():
			break

		#handle over the cotrol flow to other loops
		await asyncio.sleep(0)


	print(res1.result())
	print(res2.result())


if __name__ == '__main__':

	app = loader_plugin()
	#x = app.getdetail_plugin()
	#print(x)
	k = app.loadall_plugin()
	k[1].process()
	try:	
		loop.run_until_complete(main())
	except :
		loop.close()
