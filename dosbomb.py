import requests
import nmap
from scapy.all import *

def _nmapscan(target_ip,port_range):

def _makepacketrequest(target_ip,srcport,dstport,fla="S",tmt=2):
	p = IP(dst=target_ip)/TCP(sport=srcport,dport=dstport,flags=fla)
	ans, unans = sr(p,timeout=tmt)
	try:
		return ans[0][1].time - p.sent_time 
	except Exception as e:
		return False
	


#false is get request,true is post request
def _makerequest(url,type,post_fields='',timeout=10):
	if type :
		response = requests.post(url, data=post_fields, timeout=timeout)
	else :
		response = requests.get(url,timeout=timeout)
	print(response)
	return response.elapsed.total_seconds()


def main():
	#print(_makerequest("https://www.facebook.com",False))
	#print(_makepacketrequest('127.0.0.1',101,102))


if __name__ == '__main__':
	main()