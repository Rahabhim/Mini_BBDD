from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.units import inch
from tkinter import messagebox
import mysql.connector


def generar_pdf():
    try:
        sql = "SELECT * FROM producto"
        mibase = mysql.connector.connect(host="localhost",
                user="root", passwd="", database="baseprueba1")
        micursor = mibase.cursor()
        micursor.execute(sql)
        resultado = micursor.fetchall()

        styles = getSampleStyleSheet()
        report_title = Paragraph("Lista de registros", styles["h1"])
        report = SimpleDocTemplate("Reporte.pdf")

        table_data = []
        for k, v, e in resultado:
            table_data.append([k, v, e])

        table_style = [('GRID', (0,0), (-1,-1), 1, colors.black)]
        report_table = Table(data=table_data, style=table_style, hAlign="LEFT")
        report.build([report_title, report_table])
        messagebox.showinfo("Informacion", "PDF generado con éxito, chequee en su directorio")
    except:
        messagebox.showerror("Error",
        "Problemas de conexión o falta de modulo ReportLab")
