from tkinter import*
from tkinter import ttk, filedialog, messagebox
import os
import pickle
v=Tk()
v.geometry("440x300")
v.title("Agenda telefónica")
cuaderno=ttk.Notebook(v, width=440, height=300)
cuaderno.place(x=0,y=0)
p1=ttk.Frame(cuaderno)
p2=ttk.Frame(cuaderno)
p3=ttk.Frame(cuaderno)
p4=ttk.Frame(cuaderno)
cuaderno.add(p1,text="1.Ingreso de datos")
titulo=Label(p1,text="Ingreso de datos de contacto", font="Arial 12 underline")
titulo.place(x=5,y=5)
#-----Ruta de archivo
e2=Label(p1,text="Escoja un archivo")
e2.place(x=5,y=60)
texto= StringVar()
c2=Entry(p1,width=20, state=DISABLED,textvariable=texto)
c2.place(x=110,y=60)
#------Ingreso de datos
inst=Label(p1,text="Porfavor ingrese los datos solicitados :)")
inst.place(x=5,y=30)
e1=Label(p1,text="Número de orden:")
e1.place(x=5,y=90)
c1=Entry(p1)
c1.place(x=130,y=90)
e3=Label(p1,text="Nombre:")
e3.place(x=5,y=110)
c3=Entry(p1)
c3.place(x=130,y=110)
e4=Label(p1,text="Apellidos:")
e4.place(x=5,y=130)
c4=Entry(p1)
c4.place(x=130,y=130)
e5=Label(p1,text="Dirección:")
e5.place(x=5,y=150)
c5=Entry(p1)
c5.place(x=130,y=150)
e6=Label(p1,text="Teléfono Movil:")
e6.place(x=5,y=170)
c6=Entry(p1)
c6.place(x=130,y=170)
e7=Label(p1,text="Teléfono Fijo:")
e7.place(x=5,y=190)
c7=Entry(p1)
c7.place(x=130,y=190)
e8=Label(p1,text="Correo electronoico:")
e8.place(x=5,y=210)
c8=Entry(p1)
c8.place(x=130,y=210)
def abrir():
        respuesta=messagebox.askyesno("Pregunta","Deseas crear el archivo")
        if(respuesta):
            rutatotal= filedialog.asksaveasfilename(filetypes=(("Archivo de texto","*.txt"),),title="Crear")
            rutatotal=rutatotal+".txt"
        #    if(not(os.path.isfile(rutatotal))):
            print(rutatotal)
            file=open(rutatotal+".txt", "wb")
            file.close()
        else:
            rutatotal= filedialog.askopenfilename(filetypes=(("Archivo de texto","*.txt"),),title="Seleccionar un lugar para guardar")
            if(os.path.isfile(rutatotal)):
                file=open(rutatotal, "ab")
                file.close()
        texto.set(rutatotal)      
bt1=Button(p1, text="abrir/crear", command=abrir)
bt1.place(x=240,y=55)
def escribir():
    f=open(c2.get(),"ab")
    codigo=int(c1.get())
    nombre=(c3.get())+"                    "#20 espacios
    apellido=c4.get()+"                    "
    direccion=c5.get()+"                    "
    telefonom=c6.get()+"               "#15 espacios
    telefonof=c7.get()+"               "
    correo=c8.get()+"                    "
    nombre= nombre[0:20]
    apellido= apellido[0:20]
    direccion= direccion[0:20]
    telefonof= telefonof[0:15]
    telefonom= telefonom[0:15]
    correo= correo[0:20]
    registro=[codigo,nombre, apellido, direccion, telefonom,telefonof,correo]
    print(registro)
    pickle.dump(registro,f)
    f.close()
bt2=Button(p1, text="Ingresar datos", command=escribir)
bt2.place(x=160,y=240)
#-----PARTE #2--------------------------------------
cuaderno.add(p2,text="2.Consulta General")
titulo=Label(p2,text="Consulta General de datos", font="Arial 12 underline")
titulo.place(x=5,y=5)
t1=Text(p2, width=54,height=10)
t1.place(x=0,y=80)
#-----Ruta de archivo
e2=Label(p2,text="Escoja un archivo")
e2.place(x=5,y=45)
texto= StringVar()
c2=Entry(p2,width=20, state=DISABLED,textvariable=texto)
c2.place(x=110,y=45)
bt2=Button(p2, text="abrir/crear", command=abrir)
bt2.place(x=240,y=43)
def leer():
    br=open(c2.get(),"rb")
    max=os.path.getsize(c2.get())
    pos=0
    acu=""
    t1.delete(1.0, END)
    while (pos<max):
        re=pickle.load(br)
        acu=acu+"-".join((str(n).strip() for n in re))+"\n"
        pos=br.tell()
    t1.insert(INSERT, acu)
    br.close()
bt1=Button(p2, text="Consulta general", command=leer)
bt1.place(x=110,y=250)
#-----PARTE #3--------------------------------------
cuaderno.add(p3,text="3.Consulta por codigo")
titulo=Label(p3,text="Consulta Individual por código", font="Arial 12 underline")
titulo.place(x=5,y=5)
t2=Text(p3, width=54,height=7)
t2.place(x=0,y=80)
#-----Ruta de archivo
e2=Label(p3,text="Escoja un archivo")
e2.place(x=5,y=45)
texto= StringVar()
c2=Entry(p3,width=20, state=DISABLED,textvariable=texto)
c2.place(x=110,y=45)
c10=Entry(p3,width=20)
c10.place(x=110,y=200)
bt2=Button(p3, text="abrir/crear", command=abrir)
bt2.place(x=240,y=43)
def busqueda():
    t2.delete(1.0, END)
    print(os.path.getsize(c2.get()))
    br=open(c2.get(),"rb")
    n=int(c10.get())
    size=146
    br.seek((n-1)*size)
    registro=pickle.load(br)
    t2.insert(INSERT, registro)
    br.close()
bt1=Button(p3, text="Busqueda", command=busqueda)
bt1.place(x=110,y=250)
#-----PARTE #4--------------------------------------
cuaderno.add(p4,text="4.Modificación")
titulo=Label(p4,text="Modificación de datos", font="Arial 12 underline")
titulo.place(x=5,y=5)
#-----Ruta de archivo
e2=Label(p4,text="Escoja un archivo")
e2.place(x=5,y=60)
texto= StringVar()
c2=Entry(p4,width=20, state=DISABLED,textvariable=texto)
c2.place(x=110,y=60)
#------Ingreso de datos
inst=Label(p4,text="Cambie los datos que quiera :)")
inst.place(x=5,y=30)
e1=Label(p4,text="Número de orden:")
e1.place(x=5,y=90)
c1=Entry(p4)
c1.place(x=130,y=90)
e3=Label(p4,text="Nombre:")
e3.place(x=5,y=110)
c3=Entry(p4)
c3.place(x=130,y=110)
e4=Label(p4,text="Apellidos:")
e4.place(x=5,y=130)
c4=Entry(p4)
c4.place(x=130,y=130)
e5=Label(p4,text="Dirección:")
e5.place(x=5,y=150)
c5=Entry(p4)
c5.place(x=130,y=150)
e6=Label(p4,text="Teléfono Movil:")
e6.place(x=5,y=170)
c6=Entry(p4)
c6.place(x=130,y=170)
e7=Label(p4,text="Teléfono Fijo:")
e7.place(x=5,y=190)
c7=Entry(p4)
c7.place(x=130,y=190)
e8=Label(p4,text="Correo electronoico:")
e8.place(x=5,y=210)
c8=Entry(p4)
c8.place(x=130,y=210)
e11=Label(p4,text="# registro")
e11.place(x=300,y=210)
c11=Entry(p4,width=10)
c11.place(x=300,y=190)
bt1=Button(p4, text="abrir/crear", command=abrir)
bt1.place(x=240,y=55)
def busqueda2():
    c1.delete(0,END)          
    c3.delete(0,END)
    c4.delete(0,END)
    c5.delete(0,END)
    c6.delete(0,END)
    c7.delete(0,END)
    c8.delete(0,END)
    print(os.path.getsize(c2.get()))
    br=open(c2.get(),"rb")
    n=int(c11.get())
    size=146
    br.seek((n-1)*size)
    registro=pickle.load(br)
    codigo=registro[0]
    nombre=registro[1]
    apellido=registro[2]
    direccion=registro[3]
    telefonom=registro[4]
    telefonof=registro[5]
    correo=registro[6]
    c1.insert(INSERT,codigo)          
    c3.insert(INSERT,nombre)
    c4.insert(INSERT,apellido)
    c5.insert(INSERT,direccion)
    c6.insert(INSERT,telefonom)
    c7.insert(INSERT,telefonof)
    c8.insert(INSERT,correo)
    br.close()
def modifica():
    br=open(c2.get(),"rb")
    max=os.path.getsize(c2.get())
    pos=0
    arr=[]
    cadauno=[]
    while (pos<max):
        re=pickle.load(br)
        arr.append(re)
        pos=br.tell()
    print(arr)
    br.close()
    br=open(c2.get(),"wb")
    noquiero=int(c11.get())
    for cadauno in arr:
        if (noquiero==cadauno[0]):
            nombre=c3.get()+"                    "#20 espacios
            apellido=c4.get()+"                    "
            direccion=c5.get()+"                    "
            telefonom=c6.get()+"               "#15 espacios
            telefonof=c7.get()+"               "
            correo=c8.get()+"                    "
            apellido= apellido[0:20]
            direccion= direccion[0:20]
            telefonof= telefonof[0:15]
            telefonom= telefonom[0:15]
            correo= correo[0:20]
            norden=noquiero
            registro=[norden,nombre, apellido, direccion, telefonom,telefonof,correo]
            #print(pickle.dump(registro,br))
            pickle.dump(registro,br)
            print(registro)
        else:
            #print(pickle.dump(cadauno,br))
            pickle.dump(cadauno,br)
            print(cadauno)
    br.close()
bt2=Button(p4, text="modifica", command=modifica)
bt2.place(x=160,y=240)
bt6=Button(p4, text="busqueda", command=busqueda2)
bt6.place(x=90,y=240)
v.mainloop()
#DOCUMENTACIÓN INTERNA
#Programador:Sofia  Velásquez
#Datos del programador: Sofiamishel2003@gmail.com
#Fin: Aprender a hacer notebooks en python y reforzar conocimiento de archivos
#Lenguaje: python
#Net Framewor: 4.5
#Recursos: visual studio
#Descripción: Desarrolla un programa que te permita darle mantenimiento a algunos datos de una agenda personal
#Ultima modificación 02/03/2021