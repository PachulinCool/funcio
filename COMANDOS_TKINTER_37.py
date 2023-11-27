from tkinter import *
from tkinter import messagebox
from tkinter import filedialog
#messagebox: ventanas emergentes

root=Tk()
root.title("PROGRAMACIÓN 2 BARBOSA")
root.config(bg="green")

miframe=Frame(root, width=1200, height=600)
miframe.pack()
#------------------AÑADIR IMAGENES---------------------------------------------


#------------------CREAR OTRA VENTANA----------------------------------

def crear_ventana():
    ventana=Toplevel(root) #Toplevel(raiz) crea una ventana nueva para interactuar
    texto1=Label(ventana, text="BIENVENIDOS A COMANDOS TKINTER")
    texto1.grid(row=0, column=0)
    
#------------------VENTANAS EMERGENTES------------------------------------

def infoAdicional():
    messagebox.showinfo("titulo", "lo de adentro") #conectado al menu ayuda/acerca de
    
def aviso():
    messagebox.showwarning("AVISO", "se borrara lo anterior") #conectado al menu archivo/nuevo

def cerrar_documento():
    valor=messagebox.askretrycancel("Reintentar", "no es posible cerrar documento bloqueado") #conectado al menu archivo/cerrar

    if valor==False:
        root.destroy()

def si_o_no():
    valor=messagebox.askquestion("AVISO", "desea realizar esta accion?") #conectado al menu archivo/salir
    
    if valor=="yes":
        root.destroy() #PARAR APLICACION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

def aceptar_o_cancelar():
    valor=messagebox.askokcancel("AVISO", "desea continuar?") #conectado al boton aceptar
    
    if valor==True:
        root.destroy()

#--------------------------ABRIR O GUARDAR FICHEROS------------------------


def abrirfichero():
    fichero=filedialog.askopenfilename(title="Abrir", initialdir="C:" , filetypes=(("Ficheros de python","*.py*"),("ficheros de texto","*.txt*")))#conectado al menu archivo/abrir
    #initialdir="(directorio)" especifica donde inciar a buscar
    #filetypes="" cambiar el tipo de archivo

def guardarfichero():
    fichero=filedialog.asksaveasfile(title="Guardar")#conectado al menu archivo/guardar



#-------------------------MENÚS DE ARRIBA---------------------------------------------

barramenu=Menu(root)           #  toca con la Raiz
root.config(menu=barramenu)

archivomenu=Menu(barramenu, tearoff=0) #tearoff elimina una casilla que queda al crear un menu sin submenus (ver los otros menus)
archivomenu.add_command(label="nuevo", command=aviso)
archivomenu.add_command(label="abrir", command=abrirfichero)
archivomenu.add_command(label="guardar", command=guardarfichero)
archivomenu.add_command(label="cerrar", command=cerrar_documento)
archivomenu.add_separator() #agrega un separador entre submenus.
archivomenu.add_command(label="salir", command=si_o_no)


archivoayuda=Menu(barramenu)
archivoayuda.add_command(label="acerca de", command=infoAdicional)

barramenu.add_cascade(label="archivo", menu=archivomenu)
barramenu.add_cascade(label="Ayuda", menu=archivoayuda)


#-------------------------CUADROS DE TEXTO---------------------------------

cuadrotexto=Entry(miframe)
cuadrotexto.grid(row=0, column=1, pady=5)
cuadrotexto.config(fg="blue", justify="center")

cuadrotexto2=Entry(miframe)
cuadrotexto2.grid(row=1, column=1, pady=5)
cuadrotexto2.config(show="*")

#--------------------------CUADROS DE COMENTARIOS----------------------------

cuadrotexto3=Text(miframe, width=16, height=5)
cuadrotexto3.grid(row=2, column=1, pady=5)


#----------------------TEXTOS-----------------------------------------------------------

usuario=Label(miframe, text="usuario: ")
usuario.grid(row=0, column=0, pady=5)

contrasena=Label(miframe, text="contraseña: ")
contrasena.grid(row=1, column=0, pady=5)

comentario=Label(miframe, text="comentarios:")
comentario.grid(row=2, column=0, pady=5)

#-------------------------BOTONES UNICA OPCION-------------------------------

varoption=IntVar()

botoncircular=Radiobutton(miframe, text="masculino", variable=varoption, value=1)
botoncircular.grid(row=4, column=1, pady=5, padx=5)

botoncircular2=Radiobutton(miframe, text="femenino ", variable=varoption, value=2)
botoncircular2.grid(row=5, column=1, pady=5, padx=5)


#-------------------BOTONES--------------------------------------------------------

boton1=Button(miframe, text="entrar", command =crear_ventana)
boton1.grid(row=3, column=0)

boton=Button(miframe, text="aceptar", command=aceptar_o_cancelar)   #COMMAND redirige a una funcion para realizar una accion
boton.grid(row=3,column=1)



root.mainloop()

#columnspan=(numero)  :: ocupar un solo texto, cuadro o boton en varias columnas (el numero es la cantidad de columnas a ocupar)
# padx=(numero) :: correr texto, cuadro o boton en eje x
# pady=(numero) :: correr texto, cuadro o boton en eje y
#raiz.destroy() :: para aplicacion
#ventana=Toplevel(raiz) crea una ventana nueva para interactuar


#CONFIG: permite cambiar esteticamente los cuados, textos o botones:
#justify="center" "right" "left" : especifica la alineacion del texto
#fg="blue" color del texto [se puede usar codigo de colores #(numero)]
#show="*" muestra el caracter insertado en vez de las letras escritas
