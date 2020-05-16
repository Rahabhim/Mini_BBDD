from tkinter import *
from tkinter import ttk
from MVC.controlador import controlador


ventana = Tk()
application = controlador(ventana)
mainloop()
