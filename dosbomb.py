import sys
sys.path.append('./gui/modules/general/')
sys.path.append('./gui/')

import requests,nmap,asyncio,time,psutil
import gui_main,os
from loader_main import *
from scapy.all import *
import subprocess
#setting proxy stuff
proxy = 'http://127.0.0.1:8080'

running_tasks = []

os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy

loop = asyncio.get_event_loop()


async def gui_tasks_update():
	sent_dataold = 1000
	recv_dataold = 1000
	update_status = False
	refresh_statusbar = 2
	while 1:
		try:
			gui_main.gui_general['root'].update_idletasks()
			gui_main.gui_general['root'].update()
			if int(time.time())%refresh_statusbar == 0 and not update_status:
				update_status = True
				sent_data = int(round(psutil.net_io_counters().bytes_sent /1024,1))
				recv_data = int(round(psutil.net_io_counters().bytes_recv /1024,1))
				gui_main.gui_general['statusbar']['ntwrk_lbl_up'].set('UP: '+str((sent_data-sent_dataold)/refresh_statusbar)+'KB/s')
				gui_main.gui_general['statusbar']['ntwrk_lbl_dwn'].set('DWN: '+str((recv_data-recv_dataold)/refresh_statusbar)+'KB/s')
				sent_dataold = sent_data
				recv_dataold = recv_data
				if sent_dataold < 0 or recv_dataold < 0:
					sent_dataold = 0
					recv_dataold = 0

			elif not int(time.time())%2 == 0 :
				update_status = False

		except Exception as e:
			print(e)
			return
	
		#handle over the cotrol flow to other loops
		await asyncio.sleep(0)


async def main():
	#res1 = loop.create_task(_makerequest("http://127.0.0.1:80/",False))
	#res2 = loop.create_task(_nmapscan('127.0.0.1'))
	waitfor = []

	app = loader_plugin()
	loaded_plugs = app.loadall_plugin()
	for x in range(0,len(loaded_plugs)):
		loaded_plugs[x].gui(gui_main.gui_general)
		#print(x,"-",gui_main.gui_general)
		#print(loaded_plugs[x])
	waitfor.append(loop.create_task(gui_tasks_update()))

	await (asyncio.wait(waitfor))
	print("Quitting main")

	#print(res2.result())
	#print((res2.result()))



if __name__ == '__main__':

	loop.run_until_complete(main())
	loop.close()