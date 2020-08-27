import sys
sys.path.append('./gui/modules/general/')
sys.path.append('./gui/')

import requests,nmap,asyncio,time,psutil
import gui_main,os
from loader_main import *
from scapy.all import *
import subprocess,tkinter
#setting proxy stuff
proxy = 'http://127.0.0.1:8080'

running_tasks = []
loaded_plugs = []

sel_cur = ''

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
	gui_main.gui_general['root'].update_idletasks()
	gui_main.gui_general['root'].update()
	while 1:
		try:
			if gui_main.exitFlag:
				os._exit(1)

			gui_main.gui_general['root'].update_idletasks()
			gui_main.gui_general['root'].update()
			if int(time.time())%refresh_statusbar == 0 and not update_status:
				print("updating")
				update_status = True
				sent_data = int(round(psutil.net_io_counters().bytes_sent /1024,1))
				recv_data = int(round(psutil.net_io_counters().bytes_recv /1024,1))
				if len(running_tasks) > 0 :
					if k_inc > len(running_tasks)-1 :
						k_inc = 0
					vark = 'Tasks Running: ' + str(len(running_tasks)) +'  ' + running_tasks[k_inc].plugin_data['plugin_name']
					k_inc += 1
				else :
					vark = 'Tasks Running: 0 None Running...'

				gui_main.gui_general['statusbar']['task_lbl'].set(vark)
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
			raise  
			return
	
		#handle over the cotrol flow to other loops
		await asyncio.sleep(0)

async def main():
	#res1 = loop.create_task(_makerequest("http://127.0.0.1:80/",False))
	#res2 = loop.create_task(_nmapscan('127.0.0.1'))
	waitfor = []
	global loaded_plugs

	app = loader_plugin()
	loaded_plugs = app.loadall_plugin()
	for x in range(0,len(loaded_plugs)):
		loaded_plugs[x].gui(gui_main.gui_general)

	refreshtreeview(loaded_plugs)
	waitfor.append(loop.create_task(gui_tasks_update()))
	waitfor.append(loop.create_task(pollrunning_processes()))

	await (asyncio.wait(waitfor))
	print("Quitting main")

	#print(res2.result())
	#print((res2.result()))

async def pollrunning_processes():
	global running_tasks
	print('called')
	while True:
		#print(running_tasks)
		for x in range(0,len(loaded_plugs)):
			if loaded_plugs[x].run and not loaded_plugs[x] in running_tasks :
				loaded_plugs[x].start()
				running_tasks.append(loaded_plugs[x])
			elif not loaded_plugs[x].run and loaded_plugs[x] in running_tasks:
				if len(running_tasks) > 0 :
					loaded_plugs[x].suspend()
					running_tasks.remove(loaded_plugs[x])
					print(running_tasks)
		await asyncio.sleep(0)


def refreshtreeview(plugs):
	for x in range(0,len(plugs)):
		tre_id = plugs[x].plugin_data['plugin_tree']
		if not tre_id == '' :
			tre_split = tre_id.split("/")
			for y in range(0,len(tre_split)):
				if gui_main.gui_general['cntrl_share']['treeview'].exists(tre_split[y] + str(y)):
					#print(tre_split,"skip iter")
					continue

				if len(tre_split) == 1 :
					gui_main.gui_general['cntrl_share']['treeview'].insert('','end',tre_id,text=tre_id)  
					break
				if y == 0:
					gui_main.gui_general['cntrl_share']['treeview'].insert('','end',tre_split[y] + str(y),text=tre_split[y]) 			
				elif y == len(tre_split)-1:
					gui_main.gui_general['cntrl_share']['treeview'].insert(tre_split[y-1] + str(y-1),'end',tre_id,text=tre_split[y])
				else :
					gui_main.gui_general['cntrl_share']['treeview'].insert(tre_split[y-1] + str(y-1),'end',tre_split[y] + str(y),text=tre_split[y])

	gui_main.gui_general['cntrl_share']['treeview'].bind('<<TreeviewSelect>>', trviiew_slct)
	gui_main.gui_general['cntrl_share']['loadplug'].configure(command=butnclckevnt)

def trviiew_slct(event):
	slctd = event.widget.selection()[0]
	global sel_cur
	sel_cur = ''
	tab_names = [gui_main.gui_general['notbkhandl'].tab(i, option="text") for i in gui_main.gui_general['notbkhandl'].tabs()]
	#print(tab_names)
	for x in range(0,len(loaded_plugs)):
		if loaded_plugs[x].plugin_data['plugin_tree'] == slctd and not loaded_plugs[x].plugin_data['plugin_name'] in tab_names :
			sel_cur = loaded_plugs[x]

def butnclckevnt():
	if not sel_cur == '':
		sel_cur.gui(gui_main.gui_general)

def in_directory(file, directory):
	directory = os.path.join(os.path.realpath(directory), '')
	file = os.path.realpath(file)
	return os.path.commonprefix([file, directory]) == directory

if __name__ == '__main__':

	loop.run_until_complete(main())
	loop.close()