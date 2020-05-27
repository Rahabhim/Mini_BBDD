from tkinter import *
from tkinter import ttk
from .vista import *
from .modelo import *
from .modulo_temas.temas import EleccionTema
from .PDF.pdf_gen import generar_pdf



class controlador:
    def __init__(self, ventana):

        #---------------------------------------------------------------------#

        self.ventana = ventana
        self.visuales = vista(self.ventana)
        self.bbdd = modelo()

        #-------------------------Comando de botones--------------------------#

        self.visuales.boton_alta.config(command=self.altaDatos)
        self.visuales.boton_bd.config(command=self.crearBase)
        self.visuales.boton_modificar.config(command=self.modificarDatos)
        self.visuales.boton_baja.config(command=self.bajaDatos)
        self.visuales.boton_consulta.config(command=self.consultaDatos)
        self.visuales.boton_pdf.config(command=self.hacerPDF)
        self.visuales.boton_fake.config(command=self.crearFakes)
        self.visuales.radio_rojo.config(command=self.seleccion_tema)
        self.visuales.radio_azul.config(command=self.seleccion_tema)
        self.visuales.radio_sorpresa.config(command=self.seleccion_tema)

        #-----------------Funciones que conectan modulos----------------------#


    def altaDatos(self):
        self.bbdd.altasql(self.visuales.var_titulo,
        self.visuales.var_descripcion)
        self.bbdd.consulta(self.visuales.tree)


    def crearBase(self):
        self.bbdd.crearbd()

    def modificarDatos(self):
        seleccion = self.visuales.tree.item(self.visuales.tree.focus())
        self.bbdd.modificar(seleccion, self.visuales.var_titulo,
        self.visuales.var_descripcion)
        self.bbdd.consulta(self.visuales.tree)

    def bajaDatos(self):
        seleccion = self.visuales.tree.item(self.visuales.tree.focus())
        self.bbdd.baja(seleccion)
        self.bbdd.consulta(self.visuales.tree)

    def consultaDatos(self):
        self.bbdd.consulta(self.visuales.tree)

    def hacerPDF(self):
        generar_pdf()

    def crearFakes(self):
        self.bbdd.fake()
        self.bbdd.consulta(self.visuales.tree)


    def seleccion_tema(self):
        self.visuales.ventana["bg"] = EleccionTema(self.visuales.var_temas)
        self.visuales.parte_superior["bg"] = EleccionTema(self.visuales.var_temas)
        self.visuales.parte_central["bg"] = EleccionTema(self.visuales.var_temas)
        self.visuales.parte_inferior["bg"] = EleccionTema(self.visuales.var_temas)
        self.visuales.radio_rojo["bg"] = EleccionTema(self.visuales.var_temas)
        self.visuales.radio_azul["bg"] = EleccionTema(self.visuales.var_temas)
        self.visuales.radio_sorpresa["bg"] = EleccionTema(self.visuales.var_temas)
        self.visuales.header["bg"] = EleccionTema(self.visuales.var_temas)
        self.visuales.label_titulo["bg"] = EleccionTema(self.visuales.var_temas)
        self.visuales.label_descripcion["bg"] = EleccionTema(self.visuales.var_temas)
        self.visuales.entrada_descripcion["bg"] = EleccionTema(self.visuales.var_temas)
        self.visuales.entrada_titulo["bg"] = EleccionTema(self.visuales.var_temas)
        self.visuales.boton_consulta["bg"] = EleccionTema(self.visuales.var_temas)
        self.visuales.boton_alta["bg"] = EleccionTema(self.visuales.var_temas)
        self.visuales.boton_bd["bg"] = EleccionTema(self.visuales.var_temas)
        self.visuales.boton_modificar["bg"] = EleccionTema(self.visuales.var_temas)
        self.visuales.boton_baja["bg"] = EleccionTema(self.visuales.var_temas)
        self.visuales.boton_pdf["bg"] = EleccionTema(self.visuales.var_temas)
        self.visuales.label_temas["bg"] = EleccionTema(self.visuales.var_temas)

if __name__ == "__main__":
    ventana = Tk()
    application = controlador(ventana)
    mainloop()
