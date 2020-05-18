#!/usr/bin/env python3

#-----------------------------------------------------------------------------#
#------------- Alumno: Maximiliano Gabriel Olaz Bondarczuk -------------------#
#-----------------------------------------------------------------------------#
#------------------- Tarea unidad 6 | Nivel Intermedio -----------------------#
#-----------------------------------------------------------------------------#
#-----------------------------------------------------------------------------#
#------------------------------ Modificaciones -------------------------------#
# -Patron MVC                                                                 #
# -Implementacion de shelve en el modulo temas                                #
# -Agregada la opcion para modificar y borrar                                 #
# -Agregada la opcion para generar un PDF con los datos guardados             #
#-----------------------------------------------------------------------------#


from tkinter import *
from tkinter import ttk
from MVC.controlador import controlador


ventana = Tk()
application = controlador(ventana)
mainloop()
