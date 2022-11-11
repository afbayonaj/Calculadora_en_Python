# CALCULADORA

from tkinter import *

#============== raiz =======================

raiz=Tk()
raiz.title("CALCULADORA")
raiz.geometry("150x180")
raiz.config(bg="#28598D")
raiz.iconbitmap("abga1.ico")

#============== frame ======================

miFrame=Frame(raiz, bg="#123C68")
miFrame.pack()

#============== pantalla ===================

operacion=""
resultado=0
numeroPantalla=StringVar()

pantalla=Entry(miFrame, textvariable=numeroPantalla)
pantalla.grid(row=1, column=1, padx=10, pady=10, columnspan=4)
pantalla.config(background="#28598D", fg="white", justify="right") #03f943

#============== teclado ==================

def numeroPulsado(num):

	global operacion

	if operacion!="":
		numeroPantalla.set(num)
		operacion=""
	else:
		numeroPantalla.set(numeroPantalla.get() + num)

#============== fila 1 ===================

boton7=Button(miFrame, text="7", width=3, command=lambda:numeroPulsado("7"), background="#78A2CF")
boton7.grid(row=2, column=1)
boton8=Button(miFrame, text="8", width=3, command=lambda:numeroPulsado("8"), background="#78A2CF")
boton8.grid(row=2, column=2)
boton9=Button(miFrame, text="9", width=3, command=lambda:numeroPulsado("9"), background="#78A2CF")
boton9.grid(row=2, column=3)
botonDiv=Button(miFrame, text="/", width=3, background="#78A2CF")
botonDiv.grid(row=2, column=4)

#============== fila 2 ===================

boton4=Button(miFrame, text="4", width=3, command=lambda:numeroPulsado("4"), background="#78A2CF")
boton4.grid(row=3, column=1)
boton5=Button(miFrame, text="5", width=3, command=lambda:numeroPulsado("5"), background="#78A2CF")
boton5.grid(row=3, column=2)
boton6=Button(miFrame, text="6", width=3, command=lambda:numeroPulsado("6"), background="#78A2CF")
boton6.grid(row=3, column=3)
botonMult=Button(miFrame, text="x", width=3, background="#78A2CF")
botonMult.grid(row=3, column=4)

#============== fila 3 ===================

boton1=Button(miFrame, text="1", width=3, command=lambda:numeroPulsado("1"), background="#78A2CF")
boton1.grid(row=4, column=1)
boton2=Button(miFrame, text="2", width=3, command=lambda:numeroPulsado("2"), background="#78A2CF")
boton2.grid(row=4, column=2)
boton3=Button(miFrame, text="3", width=3, command=lambda:numeroPulsado("3"), background="#78A2CF")
boton3.grid(row=4, column=3)
botonRest=Button(miFrame, text="-", width=3, background="#78A2CF")
botonRest.grid(row=4, column=4)

#============== fila 4 ===================

botonPto=Button(miFrame, text=".", width=3, command=lambda:numeroPulsado("."), background="#78A2CF")
botonPto.grid(row=5, column=1)
boton0=Button(miFrame, text="0", width=3, command=lambda:numeroPulsado("0"), background="#78A2CF")
boton0.grid(row=5, column=2)
botonIgual=Button(miFrame, text="=", width=3, command=lambda:igual(), background="#78A2CF")
botonIgual.grid(row=5, column=3)
botonSuma=Button(miFrame, text="+", width=3, command=lambda:suma(numeroPantalla.get()), background="#78A2CF")
botonSuma.grid(row=5, column=4)

#============== borrar ===================

botonBorrar=Button(miFrame, text="C", width=18, command=lambda:borrar(), background="#78A2CF")
botonBorrar.grid(row=6, column=1, pady=5, columnspan=4)

#============== funcion borrar ===========

def borrar():

	global resultado

	resultado=0
	numeroPantalla.set("")

#============== funcion suma =============

def suma(num):

	global operacion
	global resultado

	resultado+=float(num)
	operacion="suma"
	numeroPantalla.set(resultado)

#============== funcion resta =============

def resta(num):

	global operacion
	global resultado

	resultado-=float(num)
	operacion="resta"
	numeroPantalla.set(resultado)

#============== funcion igual ===========

def igual():

	global resultado

	numeroPantalla.set(resultado+float(numeroPantalla.get()))
	resultado=0

#============== fin raiz =================
raiz.mainloop()