from tkinter import *
from tkinter import messagebox
import sqlite3


#######################################----FUNCIONES CRUD---------------------#######################################

# Conexion BBDD
""" Esta funcion CREA y  CONECTA a la BBDDD"""

def conexionBBDD():
    conexion = sqlite3.connect("Agenda")
    cursor = conexion.cursor()

    try:
        cursor.execute('''

            CREATE TABLE DATOSAGENDA (
            ID INTEGER PRIMARY KEY AUTOINCREMENT,
            NOMBRE_USUARIO VARCHAR(50),
            APELLIDO VARCHAR(10),
            PASSWORD VARCHAR(50),
            DNI INTEGER UNIQUE,
            TELEFONO VARCHAR(20),
            EMAIL VARCHAR(50),
            DIRECCION VARCHAR(50),
            COMENTARIOS VARCHAR (100))
            ''')

        messagebox.showinfo("BBDD", "BBDD creada con éxito")

    except:
        messagebox.showwarning("¡Atención!", "La BBDD ya esxiste.")

    """Si No Existe La Base de datos, la crea, y si no, no la crea y avisa que YA EXISTE"""





