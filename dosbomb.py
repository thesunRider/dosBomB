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
loaded_plugs = []

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
	k_inc = 0
	while 1:
		try:
			gui_main.gui_general['root'].update_idletasks()
			gui_main.gui_general['root'].update()
			if int(time.time())%refresh_statusbar == 0 and not update_status:
				update_status = True
				sent_data = int(round(psutil.net_io_counters().bytes_sent /1024,1))
				recv_data = int(round(psutil.net_io_counters().bytes_recv /1024,1))
				if len(running_tasks) > 0 :
					gui_main.gui_general['statusbar']['task_lbl'].set('Tasks Running: ' + str(len(running_tasks)+1) +'  ' + running_tasks[k_inc])
					k_inc += 1
					if k_inc > len(running_tasks)-1 :
						k_inc = 0

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

	waitfor.append(loop.create_task(gui_tasks_update()))

	await (asyncio.wait(waitfor))
	print("Quitting main")

	#print(res2.result())
	#print((res2.result()))

def refreshtreeview():
	#gui_main.gui_general['treeview']
	files = [os.path.join(dp, f) for dp, dn, filenames in os.walk('./') for f in filenames if os.path.splitext(f)[1] == '.cnf']
	for x in files:
		for y in files:
			if not x == y :
				if in_directory(y, os.path.dirname(x)):
					print(x + 'is the parent of' + y)
					break

def in_directory(file, directory):
	directory = os.path.join(os.path.realpath(directory), '')
	file = os.path.realpath(file)
	return os.path.commonprefix([file, directory]) == directory

if __name__ == '__main__':

	loop.run_until_complete(main())
	loop.close()