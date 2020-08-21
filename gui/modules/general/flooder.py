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

class plugin_dosbomb:
	plugin_name = "Flooder"
	plugin_version = "1.00"
	plugin_author = "Suryasaradhi"
	plugin_date = "18/08/2020" #DD/MM/YYYY
	plugin_linked_cnf = True

	def process(self):
		print("loaded_syn_flooder")

	def gui(self,guihandl):
		print("tamper with gui here")
		print(guihandl)
		PNOTEBOOK = ""
		
		self.PNotebook1_t3 = tk.Frame(guihandl['notbkhandl'])
		guihandl['notbkhandl'].add(self.PNotebook1_t3, padding=3)
		guihandl['notbkhandl'].tab(2, text="Flooder",compound="none",underline="-1",)
		self.PNotebook1_t3.configure(background="#d9d9d9")
		self.PNotebook1_t3.configure(highlightbackground="#d9d9d9")
		self.PNotebook1_t3.configure(highlightcolor="black")

		self.PNotebook2 = ttk.Notebook(self.PNotebook1_t3)
		self.PNotebook2.place(relx=0.018, rely=0.041, relheight=0.918
			, relwidth=0.964)
		self.PNotebook2.configure(takefocus="")
		self.PNotebook2.configure(style=PNOTEBOOK)
		self.PNotebook2_t1 = tk.Frame(self.PNotebook2)
		self.PNotebook2.add(self.PNotebook2_t1, padding=3)
		self.PNotebook2.tab(0, text="Syn Flood", compound="none", underline="-1"
			,)
		self.PNotebook2_t1.configure(background="#d9d9d9")
		self.PNotebook2_t1.configure(highlightbackground="#d9d9d9")
		self.PNotebook2_t1.configure(highlightcolor="black")
		self.PNotebook2_t3 = tk.Frame(self.PNotebook2)
		self.PNotebook2.add(self.PNotebook2_t3, padding=3)
		self.PNotebook2.tab(1, text="ICMP Flood", compound="none", underline="-1"
			,)
		self.PNotebook2_t3.configure(background="#d9d9d9")
		self.PNotebook2_t3.configure(highlightbackground="#d9d9d9")
		self.PNotebook2_t3.configure(highlightcolor="black")
		self.PNotebook2_t2 = tk.Frame(self.PNotebook2)
		self.PNotebook2.add(self.PNotebook2_t2, padding=3)
		self.PNotebook2.tab(2, text="HTTP Flood", compound="none", underline="-1"
			,)
		self.PNotebook2_t2.configure(relief="groove")
		self.PNotebook2_t2.configure(background="#d9d9d9")
		self.PNotebook2_t2.configure(highlightbackground="#d9d9d9")
		self.PNotebook2_t2.configure(highlightcolor="black")
		self.PNotebook2_t4 = tk.Frame(self.PNotebook2)
		self.PNotebook2.add(self.PNotebook2_t4, padding=3)
		self.PNotebook2.tab(3, text="UDP Flood", compound="none", underline="-1"
			,)
		self.PNotebook2_t4.configure(background="#d9d9d9")
		self.PNotebook2_t4.configure(highlightbackground="#d9d9d9")
		self.PNotebook2_t4.configure(highlightcolor="black")
		self.PNotebook2_t5 = tk.Frame(self.PNotebook2)
		self.PNotebook2.add(self.PNotebook2_t5, padding=3)
		self.PNotebook2.tab(4, text="IPSec Flood", compound="none", underline="-1"
			,)
		self.PNotebook2_t5.configure(background="#d9d9d9")
		self.PNotebook2_t5.configure(highlightbackground="#d9d9d9")
		self.PNotebook2_t5.configure(highlightcolor="black")
		self.PNotebook2_t6 = tk.Frame(self.PNotebook2)
		self.PNotebook2.add(self.PNotebook2_t6, padding=3)
		self.PNotebook2.tab(5, text="IKE Flood", compound="none", underline="-1"
			,)
		self.PNotebook2_t6.configure(relief="sunken")
		self.PNotebook2_t6.configure(background="#d9d9d9")
		self.PNotebook2_t6.configure(highlightbackground="#d9d9d9")
		self.PNotebook2_t6.configure(highlightcolor="black")
		self.PNotebook2.bind('<Button-1>',self._button_press)
		self.PNotebook2.bind('<Motion>',self._mouse_over)

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

