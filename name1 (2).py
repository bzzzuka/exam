from tkinter import *


def isint(s):
    try:
        int(s)
        return True
    except ValueError:
        return False


class Block:
    def __init__(self, master):
        self.e = Entry(master, width=40)
        self.b = Button(master, text="Преобразовать")
        self.l = Label(master, bg='black', fg='white', width=40)
        self.e.pack()
        self.b.pack()
        self.l.pack()

    def setFunc(self, func):
        self.b['command'] = eval('self.' + func)
        self.b['text'] = str(func)

    def mul(self):
        s = self.e.get()
        if isint(s):
            self.l['text'] = int(s) * 2
        else:
            self.l['text'] = 'лучше введите число '

    def reverse(self):
        s = self.e.get()
        if isint(s):
            self.l['text'] = int(s[::-1])
        else:
            self.l['text'] = 'лучше введите число '


root = Tk()
mycolor = '#%02x%02x%02x' % (164, 4, 208)
root.configure(bg=mycolor)
first_block = Block(root)
first_block.setFunc('mul')

second_block = Block(root)
second_block.setFunc('reverse')

root.mainloop()
