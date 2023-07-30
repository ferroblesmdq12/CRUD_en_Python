from tkinter import *
from tkinter import messagebox
import sqlite3

from Funciones_BBDD import *


###################################### INTERFACE GRAFICA ###########################################################

#Creamos raiz

#Creamos raiz

root=Tk()
root.geometry('500x500')
root.title("CRUD® By Fernando Robles")
root.iconbitmap("database.ico")




#######################################----FUNCIONES CRUD---------------------#####################

#------------------------------------------------------------------------------------------------------#

# Salir de Aplicacion.

# noinspection PyInterpreter
def salirAplicacion():


    valor=messagebox.askquestion("Salir","¿Deseas Salir de la Aplicacion?")

    if valor =="yes":
        root.destroy()

#-----------------------------------------------------------------------------------------------------#
#Recetear Campos
def limpiarCampos():

    Id.set("")
    Nombre.set("")
    Apellido.set("")
    Password.set("")
    Dni.set("")
    Telefono.set("")
    Email.set("")
    Direccion.set("")
    textocomentario.delete(1.0, END)
    #1.0 es el punto de partida y END, hasta el final.

#----------------------------------------------------------------------------------------------------#

# CREAR
def crear():
    miConexion=sqlite3.connect("Agenda")
    miCursor=miConexion.cursor()

    #Funcion PARAMETRIZADA##
    datos=Nombre.get(),Apellido.get(),Password.get(),Dni.get(),Telefono.get(),Email.get(),Direccion.get(),textocomentario.get("1.0", END)
    miCursor.execute("INSERT INTO DATOSAGENDA VALUES(NULL, ?,?,?,?,?,?,?,?)",(datos))

    # miCursor.execute("INSERT INTO DATOSAGENDA VALUES(NULL, '" + Nombre.get() +
    #                "','" + Apellido.get() +
    #                "','" + Password.get() +
    #                "','" + Dni.get() +
    #                "','" + Telefono.get() +
    #                "','" + Email.get() +
    #                "','" + Direccion.get() +
    #                "','" + textocomentario.get("1.0", END) + "')")


    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro insertado con éxito.")


#-----------------------------------------------------------------------------------------------------------
# LEER

def leer():
    miConexion = sqlite3.connect("Agenda")
    miCursor = miConexion.cursor()


    miCursor.execute("SELECT * FROM DATOSAGENDA WHERE ID=" + Id.get())
    laAgenda=miCursor.fetchall()


    for usuario in laAgenda:

         Id.set(usuario[0])
         Nombre.set(usuario[1])
         Apellido.set(usuario[2])
         Password.set(usuario[3])
         Dni.set(usuario[4])
         Telefono.set(usuario[5])
         Email.set(usuario[6])
         Direccion.set(usuario[7])
         textocomentario.insert(1.0, usuario[8])



    miConexion.commit()

#-----------------------------------------------------------------------------------------------------------
# BUSCAR por DNI

def leerPordni():
    miConexion = sqlite3.connect("Agenda")
    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOSAGENDA WHERE DNI=" + Dni.get())
    Agenda=miCursor.fetchall()

    for usuario in Agenda:


        Id.set(usuario[0])
        Nombre.set(usuario[1])
        Apellido.set(usuario[2])
        Password.set(usuario[3])
        Dni.set(usuario[4])
        Telefono.set(usuario[5])
        Email.set(usuario[6])
        Direccion.set(usuario[7])
        textocomentario.insert(1.0, usuario[8])


    miConexion.commit()

#-----------------------------------------------------------------------------------------------------------#

#Buscar por Apellido

def buscarNombre():
    miConexion = sqlite3.connect("Agenda")
    miCursor = miConexion.cursor()

    miCursor.execute("SELECT * FROM DATOSAGENDA WHERE APELLIDO=" + Apellido.get())
    Agenda=miCursor.fetchall()

    for usuario in Agenda:

        Id.set(usuario[0])
        Nombre.set(usuario[1])
        Apellido.set(usuario[2])
        Password.set(usuario[3])
        Dni.set(usuario[4])
        Telefono.set(usuario[5])
        Email.set(usuario[6])
        Direccion.set(usuario[7])
        textocomentario.insert(1.0, usuario[8])

    miConexion.commit()




#-----------------------------------------------------------------------------------------------------------#

# ACTUALIZAR

def actualizar():
    miConexion = sqlite3.connect("Agenda")
    miCursor = miConexion.cursor()

    miCursor.execute("UPDATE DATOSAGENDA SET NOMBRE_USUARIO='" + Nombre.get() +
                     "', APELLIDO='" + Apellido.get() +
                     "', PASSWORD='" + Password.get() +
                     "', DNI='" + Dni.get() +
                     "', TELEFONO='" + Telefono.get() +
                     "', EMAIL='" + Email.get() +
                     "', DIRECCION='" + Direccion.get() +
                     "', COMENTARIOS='" + textocomentario.get("1.0", END) +
                     "' WHERE ID=" + Id.get())

    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro actualizado con éxito.")

#------------------------------------------------------------------------------------------------------#

# BORRAR

def borrarRegistro():
    miConexion = sqlite3.connect("Agenda")
    miCursor = miConexion.cursor()

    miCursor.execute("DELETE FROM DATOSAGENDA WHERE ID=" + Id.get())

    miConexion.commit()
    messagebox.showinfo("BBDD", "Registro borrado con éxito.")







#------------------------------------------------------------------------------------------------------#
#Descripciones de menu ayuda

def aiuda():
    messagebox.showwarning("Ayuda", "Aiuuudaaaaaaaaaaaaaa!!!")

def textoAcercaDe():
    messagebox.showinfo("Ayuda", "SoftWare desarrollado por Fernando Robles.")

#------------------------------------------------------------------------------------------------------#

#-------------------------------------------------------------------------------------------------------#

#### VISUALIZACION ####

#CREAMOS BARRAS DE MENU En la Parte superiror#

barraMenu=Menu(root)
root.config(menu=barraMenu, width=300, height= 300)

#BBDD
bbddMenu=Menu(barraMenu, tearoff=0)
bbddMenu.add_command(label="Conectar", command=conexionBBDD)
bbddMenu.add_command(label="Salir", command=salirAplicacion)

#BORRAR (Recetear campos)
borrarMenu=Menu(barraMenu, tearoff=0)
borrarMenu.add_command(label="Borrar campos" ,command=limpiarCampos)


#CRUD
crudMenu=Menu(barraMenu, tearoff=0)
crudMenu.add_command(label="Crear" ,command=crear)
crudMenu.add_command(label="Leer",command=leer)
crudMenu.add_command(label="Actualizar", command=actualizar)
crudMenu.add_command(label="Borrar" ,command=borrarRegistro)

#AYUDA
ayudaMenu=Menu(barraMenu, tearoff=0)
ayudaMenu.add_command(label="Licencia", command=aiuda)
ayudaMenu.add_command(label="Acerca de...", command=textoAcercaDe)
ayudaMenu.add_command(label="Buscar por DNI", command=leerPordni)

#ayudaMenu.add_command(label="Buscar por NOMBRE", command=buscarNombre)#


#Creamos Las Cascadas dentro de BBDD BORRAR CRUD y AYUDA
barraMenu.add_cascade(label="BBDD", menu=bbddMenu)
barraMenu.add_cascade(label="Borrar", menu=borrarMenu)
barraMenu.add_cascade(label="CRUD", menu=crudMenu)
barraMenu.add_cascade(label="Ayuda", menu=ayudaMenu)

#--------------------------------------------------------------#
#FRAME 1
#Campos para registros

#Creamos el frame
frame1=Frame(root)
frame1.pack()

#Variables StringVar
Id=StringVar()
Nombre=StringVar()
Apellido=StringVar()
Password=StringVar()
Dni=StringVar()
Telefono=StringVar()
Email=StringVar()
Direccion=StringVar()
Comentarios=StringVar()
Sexo=StringVar()




#Creamos los cuadros de textos


cuadroID=Entry(frame1,textvariable=Id)
cuadroID.grid(row=0, column=1, padx=10, pady=10)

cuadroNombre=Entry(frame1,textvariable=Nombre)
cuadroNombre.grid(row=1, column=1, padx=10, pady=10)
cuadroNombre.config(fg="red", justify="right")

cuadroApellido=Entry(frame1,textvariable=Apellido)
cuadroApellido.grid(row=2, column=1, padx=10, pady=10)

cuadroPassword=Entry(frame1,textvariable=Password)
cuadroPassword.grid(row=3, column=1, padx=10, pady=10)
cuadroPassword.config(show="*")


cuadroDni=Entry(frame1,textvariable=Dni)
cuadroDni.grid(row=4, column=1, padx=10, pady=10)
cuadroDni.config(fg="green", justify="left")

cuadroTelefono=Entry(frame1,textvariable=Telefono)
cuadroTelefono.grid(row=5, column=1, padx=10, pady=10)

cuadroEmail=Entry(frame1,textvariable=Email)
cuadroEmail.grid(row=6, column=1, padx=10, pady=10)

cuadroDireccion=Entry(frame1,textvariable=Direccion)
cuadroDireccion.grid(row=7, column=1, padx=10, pady=10)

textocomentario=Text(frame1, width=16, height=5)
textocomentario.grid(row=8,column=1, padx=10, pady=10)
scrollVertical=Scrollbar(frame1, command=textocomentario.yview)
scrollVertical.grid(row=8, column=2, sticky="nsew")

textocomentario.config(yscrollcommand=scrollVertical.set)



#------------------------------------------------------------------------------------#
#Label
#Textos a la Izquierda de las barras de campos.

idLabel=Label(frame1, text="Id: ")
idLabel.grid(row=0, column=0, sticky="e", padx=10, pady=10)

nombreLabel=Label(frame1, text="Nombre: ")
nombreLabel.grid(row=1, column=0, sticky="e", padx=10, pady=10)

apellidoLabel=Label(frame1, text="Apellido: ")
apellidoLabel.grid(row=2, column=0, sticky="e", padx=10, pady=10)

passLabel=Label(frame1, text="Password: ")
passLabel.grid(row=3, column=0, sticky="e", padx=10, pady=10)

dniLabel=Label(frame1, text="DNI: ")
dniLabel.grid(row=4, column=0, sticky="e", padx=10, pady=10)

telefonoLabel=Label(frame1, text= "Telefono: ")
telefonoLabel.grid(row=5, column=0, sticky="e", padx=10, pady=10)

emailLabel=Label(frame1, text= "E-mail: ")
emailLabel.grid(row=6, column=0, sticky="e", padx=10, pady=10)

direccionLabel=Label(frame1, text="Dirección: ")
direccionLabel.grid(row=7, column=0, sticky="e", padx=10, pady=10)


comentarioLabel=Label(frame1, text="Comentario: ")
comentarioLabel.grid(row=8, column=0, sticky="e", padx=10, pady=10)

sexoLabel=Label(frame1, text="Sexo: ")
sexoLabel.grid(row=9, column=0, sticky="e", padx=10, pady=10)


#---------------------------------------------------------------------------------------------------#
#FRAME 2 ---> BOTONES

frame2=Frame(root)
frame2.pack()

botonCrear=Button(frame2, text="Create" ,command=crear)
botonCrear.grid(row=1, column=0, sticky="e",padx=10, pady=10)

botonLeer=Button(frame2, text="Read" , command=leer)
botonLeer.grid(row=1, column=1, sticky="e",padx=10, pady=10)

botonActualizar=Button(frame2, text="Update" , command=actualizar)
botonActualizar.grid(row=1, column=2, sticky="e",padx=10, pady=10)

botonBorrar=Button(frame2, text="Delete", command=borrarRegistro)
botonBorrar.grid(row=1, column=3, sticky="e",padx=10, pady=10)


#--------------------------------------------------------------------------------------------------------------#

root.mainloop()
# se cierra la raiz!!!





