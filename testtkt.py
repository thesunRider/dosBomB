import tkinter as tk
from tkinter import ttk

class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Large Tab Example")

        self.createTabs()

    def createTabs(self):
        self.tab_control = ttk.Notebook(self.master, style='Custom.TNotebook')

        self.tab_one = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_one, text="Tab One")
        self.frame_one = ttk.Frame(self.tab_one)
        self.frame_one.grid(row=0, column=0, padx=16, pady=16, sticky='nesw')
        self.label_one = ttk.Label(self.frame_one, text="Tab One", font=('Halvetica', 24, 'bold'))
        self.label_one.grid(row=0, column=0, padx=16, pady=16, sticky='nesw')

        self.tab_two = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_two, text="Tab Two")
        self.frame_two = ttk.Frame(self.tab_two)
        self.frame_two.grid(row=0, column=0, padx=16, pady=16, sticky='nesw')
        self.label_two = ttk.Label(self.frame_two, text="Tab Two", font=('Halvetica', 24, 'bold'))
        self.label_two.grid(row=0, column=0, padx=16, pady=16, sticky='nesw')

        self.tab_three = ttk.Frame(self.tab_control)
        self.tab_control.add(self.tab_three, text="Tab Three")
        self.frame_three = ttk.Frame(self.tab_three)
        self.frame_three.grid(row=0, column=0, padx=16, pady=16, sticky='nesw')
        self.label_three = ttk.Label(self.frame_three, text="Tab Three", font=('Halvetica', 24, 'bold'))
        self.label_three.grid(row=0, column=0, padx=16, pady=16, sticky='nesw')

        self.tab_control.grid(row=0, column=0, sticky='nesw', padx=4, pady=4)

def main():
    root = tk.Tk()

    customed_style = ttk.Style()
    customed_style.configure('Custom.TNotebook.Tab', padding=[12, 12], font=('Helvetica', 10))
    customed_style.configure('Custom.TNotebook', tabposition='wn')

    app = MainWindow(root)
    root.mainloop()

if __name__ == '__main__':
    main()