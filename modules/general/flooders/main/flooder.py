try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

from tkinter import messagebox 

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import sys,glob,configparser,importlib,os
sys.path.append('../../../../')
import loader_main 

class plugin_dosbomb:
	plugin_name = "Flooder"
	plugin_version = "1.00"
	plugin_author = "Suryasaradhi"
	plugin_date = "18/08/2020" #DD/MM/YYYY
	plugin_linked_cnf = True
	flooder_loc = './modules/general/flooders/plugin_flooders/'

	def process(self):
		print("loaded_flooder")

	def gui(self,guihandl):
		print("tamper with gui here")
		#print(guihandl)
		PNOTEBOOK = ""
		hndlsvd = guihandl['notbkhandl']
		self.PNotebook1_t3 = tk.Frame(guihandl['notbkhandl'])
		guihandl['notbkhandl'].add(self.PNotebook1_t3, padding=3)
		guihandl['notbkhandl'].tab(2, text="Flooder",compound="none",underline="-1",)
		self.PNotebook1_t3.configure(background="#d9d9d9")
		self.PNotebook1_t3.configure(highlightbackground="#d9d9d9")
		self.PNotebook1_t3.configure(highlightcolor="black")
		self.PNotebook2_12 = ttk.Notebook(self.PNotebook1_t3)
		self.PNotebook2_12.place(relx=0.018, rely=0.04, relheight=0.921, relwidth=0.964)
		self.PNotebook2_12.configure(style=PNOTEBOOK)

		self.plugs_s = loader_main.loader_plugin()
		self.guihandl2 = guihandl
		self.guihandl2['notbkhandl'] = self.PNotebook2_12
		self.plg_s = self.plugs_s.loadall_plugin('./modules/general/flooders/plugin_flooders/')
		
		for x in range(0,len(self.plg_s)):
			self.plg_s[x].gui(self.guihandl2)
			print(self.plg_s[x].plugin_name,"kolam")

		guihandl['notbkhandl'] = hndlsvd



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

