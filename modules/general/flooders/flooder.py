import tkinter as tk
from tkinter import messagebox 

import tkinter.ttk as ttk
py3 = True

import sys,glob,configparser,importlib,os
sys.path.append('../../../')
import loader_main,configparser,asyncio

class plugin_dosbomb:
	config = configparser.RawConfigParser()
	loop = asyncio.get_event_loop()
	config.read('./modules/general/flooders/flooder.cnf')
	modulesin = []
	
	run = False
	plugin_data = dict(config.items('plugin'))
	flooder_loc = './modules/general/flooders/plugin_flooders/'

	
	def suspend(self):
		for x in range(0,len(self.modulesin)):
			self.modulesin[x].suspend()


	def start(self):
		for x in range(0,len(self.modulesin)):
			self.modulesin[x].start()


	def gui(self,guihandl):
		PNOTEBOOK = ""
		hndlsvd = guihandl['notbkhandl']
		self.PNotebook1_t3 = tk.Frame(guihandl['notbkhandl'])
		guihandl['notbkhandl'].add(self.PNotebook1_t3, padding=3)
		guihandl['notbkhandl'].tab(guihandl['notbkhandl'].index("end")-1, text=self.plugin_data['plugin_name'],compound="none",underline="-1",)
		self.PNotebook1_t3.configure(background="#d9d9d9")
		self.PNotebook1_t3.configure(highlightbackground="#d9d9d9")
		self.PNotebook1_t3.configure(highlightcolor="black")
		self.PNotebook2_12 = ttk.Notebook(self.PNotebook1_t3)
		self.PNotebook2_12.place(relx=0.01, rely=0.01, relheight=0.921, relwidth=0.964)
		self.PNotebook2_12.configure(style=PNOTEBOOK)

		self.plugs_s = loader_main.loader_plugin()
		self.guihandl2 = guihandl
		self.guihandl2['notbkhandl'] = self.PNotebook2_12
		self.plg_s = self.plugs_s.loadall_plugin('./modules/general/flooders/plugin_flooders/')
		
		for x in range(0,len(self.plg_s)):
			self.modulesin.append(self.plg_s[x])
			self.plg_s[x].gui(self.guihandl2)
			#print(self.plg_s[x].plugin_name,"kolam")

		self.loop.create_task(self.update_runvar())
		guihandl['notbkhandl'] = hndlsvd


	async def update_runvar(self):
		kal = False
		while True:
			for x in range(0,len(self.modulesin)):
				if self.modulesin[x].run:
					kal = True
			self.run = kal
			kal = False
			await asyncio.sleep(0)
		return



	def _button_press(self,event):
	    widget = event.widget
	    element = widget.identify(event.x, event.y)
	    if "close" in element:
	        index = widget.index("@%d,%d" % (event.x, event.y))
	        widget.state(['pressed'])
	        widget._active = index


	def _mouse_over(self,event):
	    widget = event.widget
	    element = widget.identify(event.x, event.y)
	    if "close" in element:
	        widget.state(['alternate'])
	    else:
	        widget.state(['!alternate'])

