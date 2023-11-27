from tkinter import *
from tkinter import ttk
from tkinter import messagebox

class Ventana:

	def __init__(self,inter):
		self.interfaz = inter
		self.interfaz.geometry("300x300")
		self.interfaz.title("Tkinter y POO")
		self.num1 = IntVar()
		self.num2 = IntVar()
		self.dibujarVentana()

	def dibujarVentana(self):
		Label(self.interfaz,text="Escribe un número: ").place(x=10,y=10)
		Entry(self.interfaz,textvariable=self.num1).place(x=20,y=30)
		Entry(self.interfaz,textvariable=self.num2).place(x=20,y=80)
		Button(self.interfaz,command=self.sumar,text="Sumar").place(x=50,y=110)
		Button(self.interfaz,command=self.restar,text="Restar").place(x=50,y=140)
		Button(self.interfaz,command=self.producto,text="Producto").place(x=50,y=170)
		Button(self.interfaz,command=self.cociente,text="Cociente").place(x=50,y=200)
                
	def sumar(self):
		res = self.num1.get()+self.num2.get()
		messagebox.showinfo("Resultado","El resultado es: "+str(res))

	def restar(self):
		res = self.num1.get()-self.num2.get()
		messagebox.showinfo("Resultado","El resultado es: "+str(res))

	def producto(self):
		res = self.num1.get()*self.num2.get()
		messagebox.showinfo("Resultado","El resultado es: "+str(res))

	def cociente(self):
		res = self.num1.get()/self.num2.get()
		messagebox.showinfo("Resultado","El resultado es: "+str(res))

obj = Ventana(Tk())
obj.interfaz.mainloop()


class Interfaz:

	def __init__(self,ventana):
		self.ventana = ventana
		self.productos = ("Galletas-$10","Jugo-$8","Gomitas-$9","Agua-$7","Chocolate-$5","Donas-$11")
		self.cajaCantidad = IntVar()
		self.cajaTotal = IntVar()
		self.total = 0
		self.dibujarComponentes()

	def dibujarComponentes(self):
		self.ventana.title("Caja Registrado")
		self.ventana.geometry("650x450")
		Label(self.ventana,text="Selecciona tu producto: ").place(x=10,y=10)
		Label(self.ventana,text="Seleciona la cantidad: ").place(x=10,y=60)
		Label(self.ventana,text="El total es: ").place(x=450,y=400)
		self.combo = ttk.Combobox(self.ventana,state="readonly")
		self.combo.place(x=10,y=35)
		self.combo["values"]=self.productos
		self.combo.current(0)
		Entry(self.ventana,textvariable=self.cajaCantidad).place(x=10,y=85)
		Entry(self.ventana,textvariable=self.cajaTotal).place(x=520,y=400)
		Button(self.ventana,text="Agregar",command=self.agregarProducto).place(x=10,y=110)

		self.tabla = ttk.Treeview(self.ventana,columns=("Cantidad","Subtotal"))
		self.tabla.heading("#0",text="Producto")
		self.tabla.heading("Cantidad",text="Cantidad")
		self.tabla.heading("Subtotal",text="Subtotal")
		self.tabla.place(x=10,y=150)

	def agregarProducto(self):
		texto = self.combo.get()
		#   Galletas-$10   [0] = Galletas   [1] = 10    
		datos = texto.split("-$")
		producto = datos[0]
		precio = datos[1]
		cantidad = self.cajaCantidad.get()
		subtotal = int(precio)*int(cantidad)
		self.tabla.insert("",END,text=producto,values=(cantidad,"$"+str(subtotal)))
		self.total = self.total + subtotal
		self.cajaTotal.set("$"+str(self.total))

#obj = Interfaz(Tk())
#obj.ventana.mainloop()


#https://github.com/JesusBG5/cursopython
