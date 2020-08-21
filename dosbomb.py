import sys
sys.path.append('./gui/modules/general/')
sys.path.append('./gui/')

import requests,nmap,asyncio,time,threading,configparser
import gui_back,os
from loader_main import *
from scapy.all import *

proxy = 'http://127.0.0.1:8080'

os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy

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


async def main():
	#res1 = loop.create_task(_makerequest("http://127.0.0.1:80/",False))
	#res2 = loop.create_task(_nmapscan('127.0.0.1'))
	app = loader_plugin()
	loaded_plugs = app.loadall_plugin()
	for x in range(0,len(loaded_plugs)):
		loaded_plugs[x].gui(gui_back.gui_general)

	while 1:
		#if res2.done():
		#	break
		
		try:
			gui_back.gui_general['root'].update_idletasks()
			gui_back.gui_general['root'].update()
		except Exception as e:
			print(e)
			exit()
		

		#handle over the cotrol flow to other loops
		await asyncio.sleep(0)

	#print(res2.result())
	#print((res2.result()))



if __name__ == '__main__':

	loop.run_until_complete(main())
	loop.close()
	time.sleep(5)