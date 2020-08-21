import requests,nmap,asyncio,time
from loader_main import *
from scapy.all import *

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

def _nmap_parseresults(results={}):
	for x in list(results['nmap']['scaninfo'].keys()):
		if x == 'error':
			return False
	ip_range = list(results['scan'].keys())
	lst = []
	for x in ip_range:
		ports_inside = results['scan'][x]['tcp']
		for y in ports_inside:
			service_name = results['scan'][x]['tcp'][y]['name']
			service_version = results['scan'][x]['tcp'][y]['version']
			service_cpe = results['scan'][x]['tcp'][y]['cpe']
			service_extrainfo = results['scan'][x]['tcp'][y]['extrainfo']
			service_state = results['scan'][x]['tcp'][y]['state']
			lst.append({'ip':x,'port':y,'name':service_name,'version':service_version,'cpe':service_cpe,'extrainfo':service_extrainfo,'state':service_state})
	return lst

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