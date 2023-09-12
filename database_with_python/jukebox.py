import sqlite3

try:
    import tkinter
except ImportError:
    import Tkinter as tkinter


conn = sqlite3.connect('music.sqlite')

mainWindow = tkinter.TK()
mainWindow.tittle('music DB Browser')
mainWindow.geometry('1024x768')

mainWindow.columnconfigure(0,weight=2)
mainWindow.columnconfigure(1,weight=2)
mainWindow.columnconfigure(2,weight=2)
mainWindow.columnconfigure(3,weight=2)


mainWindow.rowconfigure(0,weight=1)
mainWindow.rowconfigure(1,weight=5)
mainWindow.rowconfigure(2,weight=5)
mainWindow.rowconfigure(3,weight=1)





