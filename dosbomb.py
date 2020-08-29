import sys
sys.path.append('./gui/modules/general/')
sys.path.append('./gui/')

import requests,asyncio,time,psutil
import os
from loader_main import *
from scapy.all import *
import subprocess,tkinter,dosfunc
from libnmap.process import NmapProcess
from libnmap.parser import *
#setting proxy stuff
proxy = 'http://127.0.0.1:8080'

running_tasks = []
loaded_plugs = []

sel_cur = ''


import sys,time
global gui_general
gui_general = {}

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

import gui_support
from PIL import ImageTk, Image
exitFlag = False
w = None
top = ''

os.environ['http_proxy'] = proxy 
os.environ['HTTP_PROXY'] = proxy
os.environ['https_proxy'] = proxy
os.environ['HTTPS_PROXY'] = proxy

loop = asyncio.get_event_loop()


class iPentry(tk.Widget):
    def __init__(self, master):
        tk.Widget.__init__(self, master, '::ipentry::ipentry')

    def get(self):
        return self.tk.call(self._w, 'get')

    def complete(self):
        return self.tk.call(self._w, 'complete')


def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root,top
    root = tk.Tk()
    gui_general['root'] = root
    root.tk.call('package','require','ipentry')

    top = Toplevel1 (root)
    gui_support.init(root, top)


def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = Toplevel1 (w)

    gui_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.configure('.',font="TkDefaultFont")
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("604x425+518+185")
        top.minsize(148, 1)
        top.maxsize(1924, 1030)
        top.resizable(0, 0)
        top.title("dosBomB v1.01")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.017, rely=0.024, relheight=0.167, relwidth=0.96)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        #------------XTRA--------------
        load = Image.open("./logo.png")
        load = load.resize((65, 55), Image.ANTIALIAS)
        render = ImageTk.PhotoImage(load)
        self.logoimg = tk.Label(self.Frame1, image=render)
        self.logoimg.image = render
        self.logoimg.place(relx=0.01, rely=0.1)
        #------------XTRA--------------

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.466, rely=0.127, height=25, width=82)
        self.Label1.configure(activebackground="#f9f9f9")
        self.Label1.configure(activeforeground="black")
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''Coded by:''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.13, rely=0.282, height=26, width=82)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''dosBomB''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.192, rely=0.563, height=26, width=42)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''v1.01''')

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.603, rely=0.141, height=26, width=90)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''thesunRider''')


        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.sub_menu = tk.Menu(top,
            activebackground="#ececec",
            activeborderwidth=1,
            activeforeground="#000000",
            background="#d9d9d9",
            borderwidth=1,
            disabledforeground="#a3a3a3",
            foreground="#000000",
            tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
            label="File")
        self.sub_menu.add_command(
            label="Scan")
        self.sub_menu.add_command(
            label="Proxy")
        self.sub_menu.add_command(
            label="Analyze")

        self.sub_menu2 = tk.Menu(top,
            activebackground="#ececec",
            activeborderwidth=1,
            activeforeground="#000000",
            background="#d9d9d9",
            borderwidth=1,
            disabledforeground="#a3a3a3",
            foreground="#000000",
            tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu2,
            label="Settings")
        self.sub_menu2.add_command(
            label="Preferences")
        self.sub_menu2.add_command(
            label="Terminate Running Tasks")
        

        self.sub_menu3 = tk.Menu(top,
            activebackground="#ececec",
            activeborderwidth=1,
            activeforeground="#000000",
            background="#d9d9d9",
            borderwidth=1,
            disabledforeground="#a3a3a3",
            foreground="#000000",
            tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu3,
            label="About")
        self.sub_menu3.add_command(
            label="About")
        self.sub_menu3.add_command(
            label="Update")
        self.sub_menu3.add_command(
            label="Help")
        self.sub_menu3.add_command(
            label="Buy me a coffee ;-)")
        

        global _images
        _images = (

         tk.PhotoImage("img_close", data='''R0lGODlhDAAMAIQUADIyMjc3Nzk5OT09PT
                 8/P0JCQkVFRU1NTU5OTlFRUVZWVmBgYGF hYWlpaXt7e6CgoLm5ucLCwszMzNbW
                 1v//////////////////////////////////// ///////////yH5BAEKAB8ALA
                 AAAAAMAAwAAAUt4CeOZGmaA5mSyQCIwhCUSwEIxHHW+ fkxBgPiBDwshCWHQfc5
                 KkoNUtRHpYYAADs= '''),

         tk.PhotoImage("img_closeactive", data='''R0lGODlhDAAMAIQcALwuEtIzFL46
                 INY0Fdk2FsQ8IdhAI9pAIttCJNlKLtpLL9pMMMNTP cVTPdpZQOBbQd60rN+1rf
                 Czp+zLxPbMxPLX0vHY0/fY0/rm4vvx8Pvy8fzy8P//////// ///////yH5BAEK
                 AB8ALAAAAAAMAAwAAAVHYLQQZEkukWKuxEgg1EPCcilx24NcHGYWFhx P0zANBE
                 GOhhFYGSocTsax2imDOdNtiez9JszjpEg4EAaA5jlNUEASLFICEgIAOw== '''),

         tk.PhotoImage("img_closepressed", data='''R0lGODlhDAAMAIQeAJ8nD64qELE
                 rELMsEqIyG6cyG7U1HLY2HrY3HrhBKrlCK6pGM7lD LKtHM7pKNL5MNtiViNaon
                 +GqoNSyq9WzrNyyqtuzq+O0que/t+bIwubJw+vJw+vTz+zT z////////yH5BAE
                 KAB8ALAAAAAAMAAwAAAVJIMUMZEkylGKuwzgc0kPCcgl123NcHWYW Fs6Gp2mYB
                 IRgR7MIrAwVDifjWO2WwZzpxkxyfKVCpImMGAeIgQDgVLMHikmCRUpMQgA7 ''')
        )

        self.style.element_create("close", "image", "img_close",
               ("active", "pressed", "!disabled", "img_closepressed"),
               ("active", "alternate", "!disabled",
               "img_closeactive"), border=8, sticky='')

        self.style.layout("ClosetabNotebook", [("ClosetabNotebook.client",
                                     {"sticky": "nswe"})])
        self.style.layout("ClosetabNotebook.Tab", [
            ("ClosetabNotebook.tab",
              { "sticky": "nswe",
                "children": [
                    ("ClosetabNotebook.padding", {
                        "side": "top",
                        "sticky": "nswe",
                        "children": [
                            ("ClosetabNotebook.focus", {
                                "side": "top",
                                "sticky": "nswe",
                                "children": [
                                    ("ClosetabNotebook.label", {"side":
                                      "left", "sticky": ''}),
                                    ("ClosetabNotebook.close", {"side":
                                        "left", "sticky": ''}),]})]})]})])

        PNOTEBOOK = "ClosetabNotebook" 

        self.style.configure('TNotebook.Tab', background=_bgcolor)
        self.style.configure('TNotebook.Tab', foreground=_fgcolor)
        self.style.map('TNotebook.Tab', background=
            [('selected', _compcolor), ('active',_ana2color)])
        self.PNotebook1 = ttk.Notebook(top)
        self.PNotebook1.place(relx=0.033, rely=0.212, relheight=0.689
                , relwidth=0.934)
        self.PNotebook1.configure(style=PNOTEBOOK)
        
        self.PNotebook1_t2 = tk.Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t2, padding=3)
        self.PNotebook1.tab(0, text="Plugins",compound="none",underline="-1",)

        self.PNotebook1_t1_2 = tk.Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t1_2, padding=3)
        self.PNotebook1.tab(1, text="Scan",compound="none",underline="-1",)


        self.PNotebook1.bind('<Button-1>',_button_press)
        self.PNotebook1.bind('<ButtonRelease-1>',_button_release)
        self.PNotebook1.bind('<Motion>',_mouse_over)


        self.treeview=ttk.Treeview(self.PNotebook1_t2)
        self.treeview.heading("#0",text="Loaded Plugins",anchor=tk.W)
        self.treeview.place(relx=0.016, rely=0.02)
        #self.treeview.move('item2','item1','end')  
        #self.treeview.move('item3','item1','end')  

        self.TLabel4 = ttk.Label(self.PNotebook1_t2)
        self.TLabel4.place(relx=0.482, rely=0.13, height=24, width=85)
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font="TkDefaultFont")
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(anchor='w')
        self.TLabel4.configure(justify='left')
        self.TLabel4.configure(text='''Description''')

        self.Text2 = tk.Text(self.PNotebook1_t2)
        self.Text2.place(relx=0.5, rely=0.22, relheight=0.522, relwidth=0.471)
        self.Text2.configure(background="white")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="blue")
        self.Text2.configure(selectforeground="white")
        self.Text2.configure(wrap="word")
        self.Text2.configure(state="disabled")

        self.Button3 = tk.Button(self.PNotebook1_t2)
        self.Button3.place(relx=0.5, rely=0.825, height=33, width=266)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Show plugin''')


        self.TFrame1 = ttk.Frame(top)
        self.TFrame1.place(relx=0.0, rely=0.94, relheight=0.063, relwidth=0.522)
        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")
        self.TFrame1.configure(cursor="fleur")

        self.tsk_lbl = tk.StringVar()
        self.tsk_lbl.set('Tasks Running: 0  None Running...')

        self.ntup = tk.StringVar()
        self.ntup.set('''UP: 20KB''')

        self.ntdwn = tk.StringVar()
        self.ntdwn.set('''DWN: 500KB''')

        self.TLabel1 = ttk.Label(self.TFrame1,textvariable=self.tsk_lbl)
        self.TLabel1.place(relx=0.0, rely=0.0, height=27, width=271)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(cursor="fleur")

        self.TFrame1_1 = ttk.Frame(top)
        self.TFrame1_1.place(relx=0.513, rely=0.94, relheight=0.063
                , relwidth=0.488)
        self.TFrame1_1.configure(relief='groove')
        self.TFrame1_1.configure(borderwidth="2")
        self.TFrame1_1.configure(relief="groove")

        self.TLabel2 = ttk.Label(self.TFrame1_1,textvariable=self.ntup)
        self.TLabel2.place(relx=0.237, rely=0.0, height=24, width=95)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')

        self.TLabel3 = ttk.Label(self.TFrame1_1,textvariable=self.ntdwn)
        self.TLabel3.place(relx=0.576, rely=0.0, height=24, width=115)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="TkDefaultFont")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='w')
        self.TLabel3.configure(justify='left')


        self.Label13 = tk.Label(self.PNotebook1_t1_2)
        self.Label13.place(relx=0.018, rely=0.076, height=26, width=52)
        self.Label13.configure(background="#d9d9d9")
        self.Label13.configure(disabledforeground="#a3a3a3")
        self.Label13.configure(foreground="#000000")
        self.Label13.configure(text='''Enter IP:''')

        self.Button4 = tk.Button(self.PNotebook1_t1_2,command=scn_btnclck)
        self.Button4.place(relx=0.071, rely=0.229, height=33, width=83)
        self.Button4.configure(activebackground="#ececec")
        self.Button4.configure(activeforeground="#000000")
        self.Button4.configure(background="#d9d9d9")
        self.Button4.configure(cursor="fleur")
        self.Button4.configure(disabledforeground="#a3a3a3")
        self.Button4.configure(foreground="#000000")
        self.Button4.configure(highlightbackground="#d9d9d9")
        self.Button4.configure(highlightcolor="black")
        self.Button4.configure(pady="0")
        self.Button4.configure(text='''Scan''')

        self.enterIp2 = iPentry(self.PNotebook1_t1_2)
        self.enterIp2.place(relx=0.123, rely=0.076)

        self.treesc = ttk.Treeview(self.PNotebook1_t1_2, columns=("value",))
        self.treesc.place(relx=0.423, rely=0.028,width=310,height=250)
        self.vsb = ttk.Scrollbar(self.PNotebook1_t1_2, orient="vertical", command=self.treesc.yview)
        self.hsb = ttk.Scrollbar(self.PNotebook1_t1_2, orient="horizontal", command=self.treesc.xview)
        self.vsb.place(relx=0.40, rely=0.028, height=250)
        self.hsb.place(relx=0.428, rely=0.93, width=308)
        self.treesc.configure(yscrollcommand=self.vsb.set,xscrollcommand=self.hsb.set)

        self.Label14 = tk.Label(self.PNotebook1_t1_2)
        self.Label14.place(relx=0.013, rely=0.86, height=26, width=70)
        self.Label14.configure(background="#d9d9d9")
        self.Label14.configure(disabledforeground="#a3a3a3")
        self.Label14.configure(foreground="#000000")
        self.Label14.configure(text='''Progress :''')

        self.pr1 = ttk.Progressbar(self.PNotebook1_t1_2,orient="horizontal",length=200,mode="determinate",takefocus=True,maximum=100)
        self.pr1.place(relx=0.153, rely=0.86,width=100,height=20)

        gui_general['statusbar'] = {'task_lbl':self.tsk_lbl,'ntwrk_lbl_up':self.ntup ,'ntwrk_lbl_dwn':self.ntdwn}
        gui_general['notbkhandl'] =  self.PNotebook1
        gui_general['menubar'] = self.menubar
        gui_general['cntrl_share'] = {'treeview':self.treeview,'loadplug': self.Button3,'scntre':self.treesc,'scnprg':self.pr1,'scnip':self.enterIp2}

        root.protocol("WM_DELETE_WINDOW", on_quit)

def scn_btnclck():
	loop = asyncio.get_event_loop()
	loop.create_task(nmapscandisplay())

async def nmapscandisplay():
	nmap_proc = NmapProcess(targets='.'.join(map(str, list(gui_general['cntrl_share']['scnip'].get()))),options="-A")
	nmap_proc.run_background()
	print('startednmapscan')
	while nmap_proc.is_running():
		gui_general['cntrl_share']['scnprg']['value'] = nmap_proc.progress
		print('nmap_progress:',nmap_proc.progress)
		await asyncio.sleep(1)

	gui_general['cntrl_share']['scnprg']['value'] = 0
	for i in gui_general['cntrl_share']['scntre'].get_children():
		gui_general['cntrl_share']['scntre'].delete(i)

	nmap_report = NmapParser.parse(nmap_proc.stdout)
	print('finishednmapscan')
	addNode(parse_scan(nmap_report))

def parse_scan(nmap_report):
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

def on_quit():
    global exitFlag
    exitFlag = True
    root.destroy()



# The following code is add to handle mouse events with the close icons
# in PNotebooks widgets.
def _button_press(event):
    widget = event.widget
    element = widget.identify(event.x, event.y)
    if "close" in element:
        index = widget.index("@%d,%d" % (event.x, event.y))
        widget.state(['pressed'])
        widget._active = index

def _button_release(event):
    widget = event.widget
    if not widget.instate(['pressed']):
            return
    element = widget.identify(event.x, event.y)
    try:
        index = widget.index("@%d,%d" % (event.x, event.y))
    except TclError:
        pass
    if "close" in element and widget._active == index:
        name_current = gui_general['notbkhandl'].tab(gui_general['notbkhandl'].index("current"), "text")
        notclose = ['Plugins']
        if not name_current in notclose:
            #gui_general['notbkhandl'].tab(index, state="hidden")
            widget.forget(index)
            widget.event_generate("<<NotebookTabClosed>>")
        else :
            messagebox.showerror("Cannot Close", "Tab "+name_current+" cannot be closed ;-)") 

    widget.state(['!pressed'])
    widget._active = None

def _mouse_over(event):
    widget = event.widget
    element = widget.identify(event.x, event.y)
    if "close" in element:
        widget.state(['alternate'])
    else:
        widget.state(['!alternate'])

#___________________DOSBOMB_________GUIEND___________________________


async def gui_tasks_update():
	sent_dataold = 1000
	recv_dataold = 1000
	update_status = False
	refresh_statusbar = 2
	k_inc = 0
	gui_general['root'].update_idletasks()
	gui_general['root'].update()
	while 1:
		try:
			if exitFlag:
				os._exit(1)

			gui_general['root'].update_idletasks()
			gui_general['root'].update()
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

				gui_general['statusbar']['task_lbl'].set(vark)
				gui_general['statusbar']['ntwrk_lbl_up'].set('UP: '+str((sent_data-sent_dataold)/refresh_statusbar)+'KB/s')
				gui_general['statusbar']['ntwrk_lbl_dwn'].set('DWN: '+str((recv_data-recv_dataold)/refresh_statusbar)+'KB/s')
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
		loaded_plugs[x].gui(gui_general)

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
				if gui_general['cntrl_share']['treeview'].exists(tre_split[y] + str(y)):
					#print(tre_split,"skip iter")
					continue

				if len(tre_split) == 1 :
					gui_general['cntrl_share']['treeview'].insert('','end',tre_id,text=tre_id)  
					break
				if y == 0:
					gui_general['cntrl_share']['treeview'].insert('','end',tre_split[y] + str(y),text=tre_split[y]) 			
				elif y == len(tre_split)-1:
					gui_general['cntrl_share']['treeview'].insert(tre_split[y-1] + str(y-1),'end',tre_id,text=tre_split[y])
				else :
					gui_general['cntrl_share']['treeview'].insert(tre_split[y-1] + str(y-1),'end',tre_split[y] + str(y),text=tre_split[y])

	gui_general['cntrl_share']['treeview'].bind('<<TreeviewSelect>>', trviiew_slct)
	gui_general['cntrl_share']['loadplug'].configure(command=butnclckevnt)


def trviiew_slct(event):
	slctd = event.widget.selection()[0]
	global sel_cur
	sel_cur = ''
	tab_names = [gui_general['notbkhandl'].tab(i, option="text") for i in gui_general['notbkhandl'].tabs()]
	#print(tab_names)
	for x in range(0,len(loaded_plugs)):
		if loaded_plugs[x].plugin_data['plugin_tree'] == slctd and not loaded_plugs[x].plugin_data['plugin_name'] in tab_names :
			sel_cur = loaded_plugs[x]

def addNode( value, parentNode="", key=None):
	if key is None:
		id = ""
	else:
		id = gui_general['cntrl_share']['scntre'].insert(parentNode, "end", text=key)

	if isinstance(value, dict):
		gui_general['cntrl_share']['scntre'].item(id, open=True)
		for (key, value) in value.items():
			addNode(value, id, key)
	else:
		gui_general['cntrl_share']['scntre'].item(id, values=(value,))

def butnclckevnt():
	if not sel_cur == '':
		sel_cur.gui(gui_general)

def in_directory(file, directory):
	directory = os.path.join(os.path.realpath(directory), '')
	file = os.path.realpath(file)
	return os.path.commonprefix([file, directory]) == directory

if __name__ == '__main__':
	vp_start_gui()
	loop.run_until_complete(main())
	loop.close()
#.mainloop()
