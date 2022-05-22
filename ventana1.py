#importo tkinter
import tkinter
import os

#métodos para el formulario
def abrirVentana2():
	os.system('ventana2.py')

#inicializo la ventana    
ventana1 = tkinter.Tk()
ventana1.geometry("400x300")

#pongo el botón guardar
botonGuardar = tkinter.Button(ventana1, text = "Abrir ventana 2", command = abrirVentana2, padx = 10, pady = 5)
botonGuardar.pack()

#ejecuto la ventana
ventana1.mainloop()