#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 5.4
#  in conjunction with Tcl version 8.6
#    Aug 27, 2020 10:03:23 PM IST  platform: Windows NT

import sys

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True

import gui2_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    gui2_support.set_Tk_var()
    top = Toplevel1 (root)
    gui2_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_Toplevel1(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    gui2_support.set_Tk_var()
    top = Toplevel1 (w)
    gui2_support.init(w, top, *args, **kwargs)
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

        top.geometry("604x425+709+245")
        top.minsize(148, 1)
        top.maxsize(1924, 1030)
        top.resizable(0, 0)
        top.title("dosBomB v1.01")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.017, rely=0.026, relheight=0.167, relwidth=0.96)

        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

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
        self.Label2.place(relx=0.293, rely=0.282, height=26, width=82)
        self.Label2.configure(activebackground="#f9f9f9")
        self.Label2.configure(activeforeground="black")
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(highlightbackground="#d9d9d9")
        self.Label2.configure(highlightcolor="black")
        self.Label2.configure(text='''dosBomB''')

        self.Label3 = tk.Label(self.Frame1)
        self.Label3.place(relx=0.362, rely=0.563, height=26, width=42)
        self.Label3.configure(activebackground="#f9f9f9")
        self.Label3.configure(activeforeground="black")
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(highlightbackground="#d9d9d9")
        self.Label3.configure(highlightcolor="black")
        self.Label3.configure(text='''v1.01''')

        self.Label4 = tk.Label(self.Frame1)
        self.Label4.place(relx=0.603, rely=0.141, height=26, width=90)
        self.Label4.configure(activebackground="#f9f9f9")
        self.Label4.configure(activeforeground="black")
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(highlightbackground="#d9d9d9")
        self.Label4.configure(highlightcolor="black")
        self.Label4.configure(text='''Suryasaradhi''')

        self.Label5 = tk.Label(self.Frame1)
        self.Label5.place(relx=0.069, rely=0.282, height=26, width=77)
        self.Label5.configure(activebackground="#f9f9f9")
        self.Label5.configure(activeforeground="black")
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(highlightbackground="#d9d9d9")
        self.Label5.configure(highlightcolor="black")
        self.Label5.configure(text='''picturlabel''')

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.menubar.add_command(
                label="File")
        self.menubar.add_command(
                label="Settings")
        self.menubar.add_command(
                label="About")
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
                label="NewCascade")
        self.sub_menu.add_command(
                label="NewCommand")

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
        self.PNotebook1_t2_1 = tk.Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t2_1, padding=3)
        self.PNotebook1.tab(0, text="General",compound="none",underline="-1",)
        self.PNotebook1_t2_1.configure(borderwidth="20")
        self.PNotebook1_t2_1.configure(background="#d9d9d9")
        self.PNotebook1_t2_1.configure(highlightbackground="#d9d9d9")
        self.PNotebook1_t2_1.configure(highlightcolor="black")
        self.PNotebook1_t1_2 = tk.Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t1_2, padding=3)
        self.PNotebook1.tab(1, text="Scan",compound="none",underline="-1",)
        self.PNotebook1_t1_2.configure(background="#d9d9d9")
        self.PNotebook1_t1_2.configure(highlightbackground="#d9d9d9")
        self.PNotebook1_t1_2.configure(highlightcolor="black")
        self.PNotebook1_t3_3 = tk.Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t3_3, padding=3)
        self.PNotebook1.tab(2, text="Flooder",compound="none",underline="-1",)
        self.PNotebook1_t3_3.configure(background="#d9d9d9")
        self.PNotebook1_t3_3.configure(highlightbackground="#d9d9d9")
        self.PNotebook1_t3_3.configure(highlightcolor="black")
        self.PNotebook1_t4_10 = tk.Frame(self.PNotebook1)
        self.PNotebook1.add(self.PNotebook1_t4_10, padding=3)
        self.PNotebook1.tab(3, text="Synflooder", compound="none", underline="-1"
                ,)
        self.PNotebook1_t4_10.configure(background="#d9d9d9")
        self.PNotebook1_t4_10.configure(highlightbackground="#d9d9d9")
        self.PNotebook1_t4_10.configure(highlightcolor="black")

        self.Label12 = tk.Label(self.PNotebook1_t2_1)
        self.Label12.place(relx=0.036, rely=0.088, height=30, width=42)
        self.Label12.configure(activebackground="#f9f9f9")
        self.Label12.configure(activeforeground="black")
        self.Label12.configure(background="#d9d9d9")
        self.Label12.configure(disabledforeground="#a3a3a3")
        self.Label12.configure(foreground="#000000")
        self.Label12.configure(highlightbackground="#d9d9d9")
        self.Label12.configure(highlightcolor="black")
        self.Label12.configure(text='''placerad''')

        self.TLabel4 = ttk.Label(self.PNotebook1_t2_1)
        self.TLabel4.place(relx=0.5, rely=0.0, height=27, width=85)
        self.TLabel4.configure(background="#d9d9d9")
        self.TLabel4.configure(foreground="#000000")
        self.TLabel4.configure(font="TkDefaultFont")
        self.TLabel4.configure(relief="flat")
        self.TLabel4.configure(anchor='w')
        self.TLabel4.configure(justify='left')
        self.TLabel4.configure(text='''Description''')
        self.TLabel4.configure(cursor="fleur")

        self.Text2 = tk.Text(self.PNotebook1_t2_1)
        self.Text2.place(relx=0.5, rely=0.156, relheight=0.515, relwidth=0.471)
        self.Text2.configure(background="white")
        self.Text2.configure(font="TkTextFont")
        self.Text2.configure(foreground="black")
        self.Text2.configure(highlightbackground="#d9d9d9")
        self.Text2.configure(highlightcolor="black")
        self.Text2.configure(insertbackground="black")
        self.Text2.configure(selectbackground="blue")
        self.Text2.configure(selectforeground="white")
        self.Text2.configure(wrap="word")

        self.Button3 = tk.Button(self.PNotebook1_t2_1)
        self.Button3.place(relx=0.5, rely=0.725, height=33, width=266)
        self.Button3.configure(activebackground="#ececec")
        self.Button3.configure(activeforeground="#000000")
        self.Button3.configure(background="#d9d9d9")
        self.Button3.configure(disabledforeground="#a3a3a3")
        self.Button3.configure(foreground="#000000")
        self.Button3.configure(highlightbackground="#d9d9d9")
        self.Button3.configure(highlightcolor="black")
        self.Button3.configure(pady="0")
        self.Button3.configure(text='''Button''')

        self.PNotebook2 = ttk.Notebook(self.PNotebook1_t3_3)
        self.PNotebook2.place(relx=0.018, rely=0.042, relheight=0.916
                , relwidth=0.964)
        self.PNotebook2.configure(style=PNOTEBOOK)
        self.PNotebook2_t1_4 = tk.Frame(self.PNotebook2)
        self.PNotebook2.add(self.PNotebook2_t1_4, padding=3)
        self.PNotebook2.tab(0, text="Syn Flood", compound="none", underline="-1"
                ,)
        self.PNotebook2_t1_4.configure(background="#d9d9d9")
        self.PNotebook2_t1_4.configure(highlightbackground="#d9d9d9")
        self.PNotebook2_t1_4.configure(highlightcolor="black")
        self.PNotebook2_t3_5 = tk.Frame(self.PNotebook2)
        self.PNotebook2.add(self.PNotebook2_t3_5, padding=3)
        self.PNotebook2.tab(1, text="ICMP Flood", compound="none", underline="-1"
                ,)
        self.PNotebook2_t3_5.configure(background="#d9d9d9")
        self.PNotebook2_t3_5.configure(highlightbackground="#d9d9d9")
        self.PNotebook2_t3_5.configure(highlightcolor="black")
        self.PNotebook2_t2_6 = tk.Frame(self.PNotebook2)
        self.PNotebook2.add(self.PNotebook2_t2_6, padding=3)
        self.PNotebook2.tab(2, text="HTTP Flood", compound="none", underline="-1"
                ,)
        self.PNotebook2_t2_6.configure(relief="raised")
        self.PNotebook2_t2_6.configure(background="#d9d9d9")
        self.PNotebook2_t2_6.configure(highlightbackground="#d9d9d9")
        self.PNotebook2_t2_6.configure(highlightcolor="black")
        self.PNotebook2_t4_7 = tk.Frame(self.PNotebook2)
        self.PNotebook2.add(self.PNotebook2_t4_7, padding=3)
        self.PNotebook2.tab(3, text="UDP Flood", compound="none", underline="-1"
                ,)
        self.PNotebook2_t4_7.configure(background="#d9d9d9")
        self.PNotebook2_t4_7.configure(highlightbackground="#d9d9d9")
        self.PNotebook2_t4_7.configure(highlightcolor="black")
        self.PNotebook2_t5_8 = tk.Frame(self.PNotebook2)
        self.PNotebook2.add(self.PNotebook2_t5_8, padding=3)
        self.PNotebook2.tab(4, text="IPSec Flood", compound="none", underline="-1"
                ,)
        self.PNotebook2_t5_8.configure(background="#d9d9d9")
        self.PNotebook2_t5_8.configure(highlightbackground="#d9d9d9")
        self.PNotebook2_t5_8.configure(highlightcolor="black")
        self.PNotebook2_t6_9 = tk.Frame(self.PNotebook2)
        self.PNotebook2.add(self.PNotebook2_t6_9, padding=3)
        self.PNotebook2.tab(5, text="IKE Flood", compound="none", underline="-1"
                ,)
        self.PNotebook2_t6_9.configure(relief="sunken")
        self.PNotebook2_t6_9.configure(background="#d9d9d9")
        self.PNotebook2_t6_9.configure(highlightbackground="#d9d9d9")
        self.PNotebook2_t6_9.configure(highlightcolor="black")
        self.PNotebook2.bind('<Button-1>',_button_press)
        self.PNotebook2.bind('<ButtonRelease-1>',_button_release)
        self.PNotebook2.bind('<Motion>',_mouse_over)

        self.Label6 = tk.Label(self.PNotebook1_t4_10)
        self.Label6.place(relx=0.518, rely=0.0, height=30, width=109)
        self.Label6.configure(activebackground="#f9f9f9")
        self.Label6.configure(activeforeground="black")
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(highlightbackground="#d9d9d9")
        self.Label6.configure(highlightcolor="black")
        self.Label6.configure(text='''Console Output''')

        self.Text1 = tk.Text(self.PNotebook1_t4_10)
        self.Text1.place(relx=0.518, rely=0.118, relheight=0.737, relwidth=0.454)

        self.Text1.configure(background="white")
        self.Text1.configure(font="TkTextFont")
        self.Text1.configure(foreground="black")
        self.Text1.configure(highlightbackground="#d9d9d9")
        self.Text1.configure(highlightcolor="black")
        self.Text1.configure(insertbackground="black")
        self.Text1.configure(selectbackground="blue")
        self.Text1.configure(selectforeground="white")
        self.Text1.configure(wrap="word")

        self.Label7 = tk.Label(self.PNotebook1_t4_10)
        self.Label7.place(relx=0.048, rely=0.031, height=42, width=62)
        self.Label7.configure(activebackground="#f9f9f9")
        self.Label7.configure(activeforeground="black")
        self.Label7.configure(background="#d9d9d9")
        self.Label7.configure(disabledforeground="#a3a3a3")
        self.Label7.configure(foreground="#000000")
        self.Label7.configure(highlightbackground="#d9d9d9")
        self.Label7.configure(highlightcolor="black")
        self.Label7.configure(text='''Enter IP:''')

        self.Label8 = tk.Label(self.PNotebook1_t4_10)
        self.Label8.place(relx=0.0, rely=0.221, height=30, width=92)
        self.Label8.configure(activebackground="#f9f9f9")
        self.Label8.configure(activeforeground="black")
        self.Label8.configure(background="#d9d9d9")
        self.Label8.configure(disabledforeground="#a3a3a3")
        self.Label8.configure(foreground="#000000")
        self.Label8.configure(highlightbackground="#d9d9d9")
        self.Label8.configure(highlightcolor="black")
        self.Label8.configure(text='''Target Port:''')

        self.Label9 = tk.Label(self.PNotebook1_t4_10)
        self.Label9.place(relx=0.0, rely=0.397, height=30, width=95)
        self.Label9.configure(activebackground="#f9f9f9")
        self.Label9.configure(activeforeground="black")
        self.Label9.configure(background="#d9d9d9")
        self.Label9.configure(disabledforeground="#a3a3a3")
        self.Label9.configure(foreground="#000000")
        self.Label9.configure(highlightbackground="#d9d9d9")
        self.Label9.configure(highlightcolor="black")
        self.Label9.configure(text='''Packet Count:''')

        self.Label10 = tk.Label(self.PNotebook1_t4_10)
        self.Label10.place(relx=0.018, rely=0.573, height=30, width=82)
        self.Label10.configure(activebackground="#f9f9f9")
        self.Label10.configure(activeforeground="black")
        self.Label10.configure(background="#d9d9d9")
        self.Label10.configure(disabledforeground="#a3a3a3")
        self.Label10.configure(foreground="#000000")
        self.Label10.configure(highlightbackground="#d9d9d9")
        self.Label10.configure(highlightcolor="black")
        self.Label10.configure(text='''Packet Size:''')

        self.Spinbox1 = tk.Spinbox(self.PNotebook1_t4_10, from_=1.0, to=100.0)
        self.Spinbox1.place(relx=0.196, rely=0.221, relheight=0.103
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
        self.Spinbox1.configure(textvariable=gui2_support.spinbox)
        self.value_list = ['80',]
        self.Spinbox1.configure(values=self.value_list)

        self.Spinbox1_1 = tk.Spinbox(self.PNotebook1_t4_10, from_=1.0, to=100.0)
        self.Spinbox1_1.place(relx=0.196, rely=0.397, relheight=0.107
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
        self.Spinbox1_1.configure(textvariable=gui2_support.spinbox)

        self.Spinbox1_2 = tk.Spinbox(self.PNotebook1_t4_10, from_=1.0, to=100.0)
        self.Spinbox1_2.place(relx=0.196, rely=0.573, relheight=0.107
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
        self.Spinbox1_2.configure(textvariable=gui2_support.spinbox)

        self.Label11 = tk.Label(self.PNotebook1_t4_10)
        self.Label11.place(relx=0.179, rely=0.046, height=30, width=42)
        self.Label11.configure(activebackground="#f9f9f9")
        self.Label11.configure(activeforeground="black")
        self.Label11.configure(background="#d9d9d9")
        self.Label11.configure(disabledforeground="#a3a3a3")
        self.Label11.configure(foreground="#000000")
        self.Label11.configure(highlightbackground="#d9d9d9")
        self.Label11.configure(highlightcolor="black")
        self.Label11.configure(text='''dai dai''')

        self.Button1 = tk.Button(self.PNotebook1_t4_10)
        self.Button1.place(relx=0.054, rely=0.794, height=33, width=96)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Launch''')

        self.Button1_3 = tk.Button(self.PNotebook1_t4_10)
        self.Button1_3.place(relx=0.268, rely=0.79, height=33, width=96)
        self.Button1_3.configure(activebackground="#ececec")
        self.Button1_3.configure(activeforeground="#000000")
        self.Button1_3.configure(background="#d9d9d9")
        self.Button1_3.configure(disabledforeground="#a3a3a3")
        self.Button1_3.configure(foreground="#000000")
        self.Button1_3.configure(highlightbackground="#d9d9d9")
        self.Button1_3.configure(highlightcolor="black")
        self.Button1_3.configure(pady="0")
        self.Button1_3.configure(text='''Stop''')

        self.Checkbutton1 = tk.Checkbutton(self.PNotebook1_t4_10)
        self.Checkbutton1.place(relx=0.482, rely=0.878, relheight=0.118
                , relwidth=0.246)
        self.Checkbutton1.configure(activebackground="#ececec")
        self.Checkbutton1.configure(activeforeground="#000000")
        self.Checkbutton1.configure(background="#d9d9d9")
        self.Checkbutton1.configure(disabledforeground="#a3a3a3")
        self.Checkbutton1.configure(foreground="#000000")
        self.Checkbutton1.configure(highlightbackground="#d9d9d9")
        self.Checkbutton1.configure(highlightcolor="black")
        self.Checkbutton1.configure(justify='left')
        self.Checkbutton1.configure(text='''Use scan result''')
        self.Checkbutton1.configure(variable=gui2_support.che47)

        self.Checkbutton2 = tk.Checkbutton(self.PNotebook1_t4_10)
        self.Checkbutton2.place(relx=0.75, rely=0.878, relheight=0.118
                , relwidth=0.211)
        self.Checkbutton2.configure(activebackground="#ececec")
        self.Checkbutton2.configure(activeforeground="#000000")
        self.Checkbutton2.configure(background="#d9d9d9")
        self.Checkbutton2.configure(disabledforeground="#a3a3a3")
        self.Checkbutton2.configure(foreground="#000000")
        self.Checkbutton2.configure(highlightbackground="#d9d9d9")
        self.Checkbutton2.configure(highlightcolor="black")
        self.Checkbutton2.configure(justify='left')
        self.Checkbutton2.configure(text='''Guided DOS''')
        self.Checkbutton2.configure(variable=gui2_support.che48)
        self.PNotebook1.bind('<Button-1>',_button_press)
        self.PNotebook1.bind('<ButtonRelease-1>',_button_release)
        self.PNotebook1.bind('<Motion>',_mouse_over)

        self.TFrame1 = ttk.Frame(top)
        self.TFrame1.place(relx=0.0, rely=0.941, relheight=0.061, relwidth=0.522)

        self.TFrame1.configure(relief='groove')
        self.TFrame1.configure(borderwidth="2")
        self.TFrame1.configure(relief="groove")

        self.TLabel1 = ttk.Label(self.TFrame1)
        self.TLabel1.place(relx=0.0, rely=0.0, height=28, width=271)
        self.TLabel1.configure(background="#d9d9d9")
        self.TLabel1.configure(foreground="#000000")
        self.TLabel1.configure(font="TkDefaultFont")
        self.TLabel1.configure(relief="flat")
        self.TLabel1.configure(anchor='w')
        self.TLabel1.configure(justify='left')
        self.TLabel1.configure(text='''Tasks Running: 3  Flooder\synFlooder''')

        self.TFrame1_1 = ttk.Frame(top)
        self.TFrame1_1.place(relx=0.513, rely=0.941, relheight=0.061
                , relwidth=0.488)
        self.TFrame1_1.configure(relief='groove')
        self.TFrame1_1.configure(borderwidth="2")
        self.TFrame1_1.configure(relief="groove")

        self.TLabel2 = ttk.Label(self.TFrame1_1)
        self.TLabel2.place(relx=0.237, rely=0.0, height=25, width=95)
        self.TLabel2.configure(background="#d9d9d9")
        self.TLabel2.configure(foreground="#000000")
        self.TLabel2.configure(font="TkDefaultFont")
        self.TLabel2.configure(relief="flat")
        self.TLabel2.configure(anchor='w')
        self.TLabel2.configure(justify='left')
        self.TLabel2.configure(text='''UP: 20KB''')

        self.TLabel3 = ttk.Label(self.TFrame1_1)
        self.TLabel3.place(relx=0.576, rely=0.0, height=25, width=115)
        self.TLabel3.configure(background="#d9d9d9")
        self.TLabel3.configure(foreground="#000000")
        self.TLabel3.configure(font="TkDefaultFont")
        self.TLabel3.configure(relief="flat")
        self.TLabel3.configure(anchor='w')
        self.TLabel3.configure(justify='left')
        self.TLabel3.configure(text='''DWN: 500KB''')

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
        widget.forget(index)
        widget.event_generate("<<NotebookTabClosed>>")

    widget.state(['!pressed'])
    widget._active = None

def _mouse_over(event):
    widget = event.widget
    element = widget.identify(event.x, event.y)
    if "close" in element:
        widget.state(['alternate'])
    else:
        widget.state(['!alternate'])

if __name__ == '__main__':
    vp_start_gui()





