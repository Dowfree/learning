#!usr/bin/env python
# -*-coding:utf-8 -*-
from tkinter import *
from tkinter import messagebox

"""
class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel = Label(self, text='Hello, world!')
        self.helloLabel.pack()
        self.quitButton = Button(self, text='Quit', command=self.quit)
        self.quitButton.pack()
"""


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        messagebox.showinfo('Message', 'Hello, %s' % name)


def main():
    root = Tk()
    root.geometry('400x350+500+200')
    app = Application()
    # 设置窗口标题
    app.master.title('Hello, world!')
    # 主消息循环
    app.mainloop()

if __name__ == '__main__':
    main()