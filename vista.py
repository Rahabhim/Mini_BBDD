from tkinter import *
from tkinter import ttk


class vista:
    def __init__(self, ventana):

        self.var_titulo = StringVar()
        self.var_descripcion = StringVar()
        self.var_temas = IntVar()
        self.var_color = "red"


        self.ventana = ventana
        self.ventana.title("Tarea POO")
        self.ventana.config(bg=self.var_color)

        self.parte_superior = Frame(ventana)
        self.parte_superior.pack()
        self.parte_superior.config(bg=self.var_color)

        self.parte_central = Frame(ventana)
        self.parte_central.pack()

        self.parte_inferior = Frame(ventana)
        self.parte_inferior.pack()
        self.parte_inferior.config(bg=self.var_color)

        self.header = Label(self.parte_superior, text="Ingrese sus datos",
                    bg="#9A32CD", fg="white", width=88).grid(row=1, column=0,
                    columnspan=3, sticky=W+E)
        self.label_titulo = Label(self.parte_superior, text="Titulo",
                    bg="#9A32CD", fg="white", width=10).grid(row=2, column=0,
                    sticky=W)
        self.label_descripcion = Label(self.parte_superior, text="Descripción",
                    bg="#9A32CD", fg="white", width=10).grid(row=3, column=0,
                    sticky=W)
        self.entrada_titulo = Entry(self.parte_superior,
                    textvariable=self.var_titulo, width=25).grid(row=2,
                    column=1)
        self.entrada_descripcion = Entry(self.parte_superior,
                    textvariable=self.var_descripcion,
                    width=25).grid(row=3, column=1)
        self.boton_consulta = Button(self.parte_superior,
                    text="Mostrar registros existentes", width=88)
        self.boton_consulta.grid(row=5, column=0,
                    columnspan=3, sticky=W+E)
        self.boton_bd = Button(self.parte_superior,
                    text="Crear BD")
        self.boton_bd.grid(row=4, ipadx=20, padx=70, column=0)
        # self.boton_modificar = Button(self.parte_superior,
        #             text="Modificar").grid(row=5, ipadx=20, padx=70, column=1)
        self.boton_alta = Button(self.parte_superior,
                    text="Alta")
        self.boton_alta.grid(row=4, ipadx=20, padx=70, column=2)

        #-----------------------------Parte central-----------------------------------#

        self.tree = ttk.Treeview(self.parte_central)
        self.tree.grid(row=0, columnspan=1)
        self.tree["columns"] = ("1", "2", "3")
        self.tree["show"] = "headings"
        self.tree.heading("1", text="id")
        self.tree.heading("2", text="Titulo")
        self.tree.heading("3", text="Descripción")
        self.scrollbar = ttk.Scrollbar(self.parte_central, orient="vertical",
                    command=self.tree.yview)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        self.tree.configure(yscrollcommand=self.scrollbar.set)

        #----------------------------Parte inferior-----------------------------------#

        self.label_temas = Label(self.parte_inferior, text="Temas", bg="black",
                    fg="red", relief="raised", borderwidth=5,
                    width=88).grid(row=0)
        self.radio_rojo = Radiobutton(self.parte_inferior, text="Tono Rojo",
                    bg="black", fg="red", width=10, variable=self.var_temas,
                    value=1).grid(row=1,
                    columnspan=3)
        self.radio_azul = Radiobutton(self.parte_inferior, text="Tono Azul",
                    bg="black", fg="red", width=10, variable=self.var_temas,
                    value=2).grid(row=2,
                    columnspan=3)
        self.radio_verde = Radiobutton(self.parte_inferior, text="Tono Verde",
                    bg="black", fg="red", width=10, variable=self.var_temas,
                    value=3).grid(row=3,
                    columnspan=3)
