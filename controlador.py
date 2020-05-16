from tkinter import *
from tkinter import ttk
from vista import *
from modelo import *
from temas import EleccionTema


class controlador:
    def __init__(self, ventana):

        #---------------------------------------------------------------------#

        self.ventana = ventana
        self.visuales = vista(self.ventana)
        self.bbdd = modelo()

        #-------------------------Comando de botones--------------------------#

        self.visuales.boton_alta.config(command=self.altaDatos)
        self.visuales.boton_bd.config(command=self.crearBase)
        self.visuales.boton_consulta.config(command=self.consultaDatos)
        self.visuales.radio_rojo.config(command=self.seleccion_tema)
        self.visuales.radio_azul.config(command=self.seleccion_tema)
        self.visuales.radio_verde.config(command=self.seleccion_tema)

        #-----------------Funciones que conectan modulos----------------------#


    def altaDatos(self):
        self.bbdd.altasql(self.visuales.var_titulo, self.visuales.var_descripcion)

    def crearBase(self):
        self.bbdd.crearbd()

    def consultaDatos(self):
        self.bbdd.consulta(self.visuales.tree)

    def seleccion_tema(self):
        self.visuales.ventana["bg"] = EleccionTema(self.visuales.var_temas)
        self.visuales.parte_superior["bg"] = EleccionTema(self.visuales.var_temas)
        self.visuales.parte_central["bg"] = EleccionTema(self.visuales.var_temas)
        self.visuales.parte_inferior["bg"] = EleccionTema(self.visuales.var_temas)


if __name__ == "__main__":
    ventana = Tk()
    application = controlador(ventana)
    mainloop()
