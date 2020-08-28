import tkinter as tk
import tkinter.ttk as ttk
import nmap

nm = nmap.PortScanner()
DATA = nm.scan()

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.tree = ttk.Treeview(self, columns=("value",))
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.tree.pack(side="top", fill="both", expand=True)

        self.addNode(value=DATA, parentNode="")



if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()