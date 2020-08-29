import Tkinter as tk
import ttk

DATA = {
    "filename":"file.txt",
    "filesize":"500kb",
    "maxcolwidth": {
        "col1":"300",
        "col2":"2",
        "col3":"3"
        },
    "numberofcolumns":"3",
    "datatypes": {
        "col1":"string",
        "col2":"int",
        "col3":"int"
        },
    "rowcount":"400"
    }

class Example(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)

        self.tree = ttk.Treeview(self, columns=("value",))
        self.vsb = ttk.Scrollbar(self, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)

        self.vsb.pack(side="right", fill="y")
        self.tree.pack(side="top", fill="both", expand=True)

        self.addNode(value=DATA, parentNode="")

    def addNode(self, value, parentNode="", key=None):
        if key is None:
            id = ""
        else:
            id = self.tree.insert(parentNode, "end", text=key)

        if isinstance(value, dict):
            self.tree.item(id, open=True)
            for (key, value) in value.items():
                self.addNode(value, id, key)
        else:
            self.tree.item(id, values=(value,))

if __name__ == "__main__":
    root = tk.Tk()
    Example(root).pack(fill="both", expand=True)
    root.mainloop()