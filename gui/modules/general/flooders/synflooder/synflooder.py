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
	plugin_name="SynFlooder"
	plugin_version="1.00"
	plugin_author="Suryasaradhi"
	plugin_date="18/08/2020"
	plugin_file="synflooder.py"
	plugin_class="plugin_synflooder"
	plugin_internal=True 

	def process(self):
		print("Loaded Syn_Flooder")

	def gui(self,guihandl):
		self.PNotebook1_t5 = tk.Frame(guihandl['notbkhandl'])
		guihandl['notbkhandl'].add(self.PNotebook1_t5, padding=3)
		guihandl['notbkhandl'].tab(guihandl['notbkhandl'].index("end")-1, text="SynFlooder",compound="none",underline="-1",)
		self.PNotebook1_t5.configure(background="#d9d9d9")
		self.PNotebook1_t5.configure(highlightbackground="#d9d9d9")
		self.PNotebook1_t5.configure(highlightcolor="black")
		print("Synflooder gui shown")


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
