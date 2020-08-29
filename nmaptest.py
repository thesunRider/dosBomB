from libnmap.process import NmapProcess
from libnmap.parser import *
from time import sleep


def print_scan(nmap_report):
	aps = {}
	for host in nmap_report.hosts:
		if len(host.hostnames):
			tmp_host = host.hostnames.pop()
		else:
			tmp_host = host.address

		aps['host'] = tmp_host
		aps['hostaddress'] = host.address
		aps['hoststatus'] = host.status
		aps['osanalysis'] = host.os
		for serv in host.services:
			ban = ''
			if len(serv.banner):
				ban = serv.banner
			aps[str(serv.port)] = {'protocol':serv.protocol,'state':serv.state,'service':serv.service,'banner':ban}

		return aps

nmap_proc = NmapProcess(targets="127.0.0.1",options="-sV")
nmap_proc.run_background()
while nmap_proc.is_running():
    print("Nmap Scan running: ETC: {0} DONE: {1}%".format(nmap_proc.etc,
                                                          nmap_proc.progress))
    sleep(2)

#print("rc: {0} output: {1}".format(nmap_proc.rc, nmap_proc.summary))
nmap_report = NmapParser.parse(nmap_proc.stdout)
print(print_scan(nmap_report))

