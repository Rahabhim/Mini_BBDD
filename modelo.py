from tkinter import messagebox
import mysql.connector
import re


class modelo:

    # def __init__(self, vc):
    #     self.vc = vc
    #





    def altasql(self, var_titulo, var_descripcion):
        try:
            if not self.validar(var_titulo.get()):
                messagebox.showinfo("Error", "Título invalido: " + var_titulo.get()
                 + "\nNo puede estar vacío, contener números o símbolos")
                return
            datos = (var_titulo.get(), var_descripcion.get())
            sql = "INSERT INTO producto (titulo, descripcion) VALUES (%s, %s)"
            mibase = mysql.connector.connect(host="localhost", user="root",
                    passwd="", database="baseprueba1")
            micursor = mibase.cursor()
            micursor.execute(sql, datos)
            print(micursor.rowcount, "Cantidad de registros agregados.")
            mibase.commit()
        except:
            messagebox.showerror("Error",
            "Base de datos inexistente o problemas de conexión")



    def crearbd(self):
        try:

            mibase = mysql.connector.connect(host="localhost",
                    user="root", passwd="")
            micursor = mibase.cursor()
            micursor.execute("CREATE DATABASE IF NOT EXISTS baseprueba1")
            mibase = mysql.connector.connect(host="localhost", user="root",
                    passwd="", database="baseprueba1")
            micursor = mibase.cursor()
            micursor.execute("""CREATE TABLE IF NOT EXISTS producto( id int(11)
            NOT NULL PRIMARY KEY AUTO_INCREMENT, titulo VARCHAR(128)
            COLLATE utf8_spanish2_ci NOT NULL, descripcion text
            COLLATE utf8_spanish2_ci NOT NULL )""")
            print("Base de datos lista")
            mibase.commit()
        except:
            messagebox.showerror("Error",
            "Compruebe su conexión a la base de datos")



    def consulta(self, tree):
        try:
            self.sql = "SELECT * FROM producto"
            self.mibase = mysql.connector.connect(host="localhost", user="root",
                    passwd="", database="baseprueba1")
            self.micursor = self.mibase.cursor()
            self.micursor.execute(self.sql)
            self.resultado = self.micursor.fetchall()
            for dato in tree.get_children():
                tree.delete(dato)
            for dato in self.resultado:
                tree.insert("", "end", value=dato)
            print("Consulta a base de datos")
            self.mibase.commit()
        except:
            messagebox.showerror("Error",
            "Compruebe su conexión a la base de datos")


    def validar(self, titulo_var):
        patron = re.compile("^[A-Za-z]+(?:[ _-][A-Za-z]+)*$")
        if not (re.fullmatch(patron, titulo_var)):
            return False
        else:
            return True
