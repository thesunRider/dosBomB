# This Python file uses the following encoding: utf-8
# Python 3.7 and Tk version 8.6
import sys
import tkinter as tk
import random

class iPentry(tk.Widget):
    def __init__(self, master):
        tk.Widget.__init__(self, master, '::ipentry::ipentry')

    def get(self):
        return self.tk.call(self._w, 'get')

    def complete(self):
        return self.tk.call(self._w, 'complete')

class CWslider(tk.Widget):
    def __init__(self, master, placeholder):
        tk.Widget.__init__(self, master, '::controlwidget::slider',
            {'variable':placeholder, 'from_':0, 'to':20, 'number':3,
            'width':55, 'background':'yellow'})

    def get(self):
        getvalue = self.tk.call(self._w, 'get')
        getvalue = [int(x) for x in getvalue]
        return getvalue

    def set(self, value):
        self.tk.call(self._w, 'set', value)

    def complete(self):
        return self.tk.call(self._w, 'complete')

class CWrdial(tk.Widget):
    def __init__(self, master):
        tk.Widget.__init__(self, master, '::controlwidget::rdial',
            {'width':50, 'orient':'vertical', 'height':100,  'background':'green'})

    def get(self):
        return self.tk.call(self._w, 'get')

    def complete(self):
        return self.tk.call(self._w, 'complete')


class CWvoltmeter(tk.Widget):
    def __init__(self, master, variable):
        tk.Widget.__init__(self, master, '::controlwidget::voltmeter',
            {'min':0, 'max':100, 'variable':variable})


def getIP(event):
    myip = enterIp.get()
    labelvar.set(myip)
    print(f"myip is {myip}")


def updating(master, myValuesvar, myvoltvar, interval):
    #we can't get value from placeholder because slider corrupts the IntVar?
    slidervalues = slider.get() #so we use the get method
    myValuesvar.set(slidervalues)
    mydialvalue.set(mydial.get())
    myvoltvar.set( random.randrange(0, 100, 1))
    root.after(interval, updating, root, myValuesvar, myvoltvar, interval)

root = tk.Tk()
root.geometry("300x550+280+0")
root.tk.call('package','require','ipentry')

enterIp = iPentry(root)
enterIp.pack()
labelIP = tk.Label(root, text="Show The IP")
labelIP.pack()

labelvar = tk.StringVar()
label2 = tk.Label(root, textvariable=labelvar)
label2.pack()
root.bind('<Return>', getIP)

interval = 300 #milliseconds for GUI
updating(root, myValuesvar, myvoltvar, interval)
root.mainloop()
sys.exit()