from tkinter import *
from tkinter import ttk
from vista import *
from modelo import *


class controlador:
    def __init__(self, ventana):

        self.ventana = ventana

        self.visuales = vista(self.ventana)

        # self.bbdd = modelo(self)
        self.bbdd = modelo()




        self.visuales.boton_alta.config(command=self.altaDatos)
        self.visuales.boton_bd.config(command=self.crearBase)


    def altaDatos(self):
        self.bbdd.altasql(self.visuales.var_titulo, self.visuales.var_descripcion)

    def crearBase(self):
        self.bbdd.crearbd()


        # self.visuales.boton_consulta.config(lambda:consulta(self.tree))


    # def consultaDatos(self):
    #     self.bbdd.consulta(self.tree)
        # self.visuales.



        # self.boton_bd = Button(self.parte_superior, text="Crear BD",
        #             command=crearbd).grid(row=5, ipadx=20, padx=70, column=0)
        # self.boton_alta = Button(self.parte_superior, text="Alta",
        #             command=lambda:altasql(self.var_titulo,
        #             self.var_descripcion)).grid(row=5, ipadx=20, padx=70,
        #             column=1)


        # self.radio_rojo = Radiobutton(self.parte_inferior, text="Tono Rojo",
        #             bg="black", fg="red", width=10, variable=self.var_temas,
        #             value=1, command=self.seleccion_tema).grid(row=1,
        #             columnspan=3)
        # self.radio_azul = Radiobutton(self.parte_inferior, text="Tono Azul",
        #             bg="black", fg="red", width=10, variable=self.var_temas,
        #             value=2, command=self.seleccion_tema).grid(row=2,
        #             columnspan=3)
        # self.radio_verde = Radiobutton(self.parte_inferior, text="Tono Verde",
        #             bg="black", fg="red", width=10, variable=self.var_temas,
        #             value=3, command=self.seleccion_tema).grid(row=3,
        #             columnspan=3)




if __name__ == "__main__":
    ventana = Tk()
    application = controlador(ventana)
    mainloop()
