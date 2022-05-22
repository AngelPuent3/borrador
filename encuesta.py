# Let's import tkinter 
from tkinter import *
#import tkinter as tk
 
# Manipulate data from registration fields 
def send_data():
  nombreInfo = nombre.get()
  edadInfo = edad.get()
  emailInfo = email.get()
  localidadInfo = localidad.get()
  saborInfo = sabor.get()
  experienciaInfo =experiencia.get()
  compraInfo = compra.get()
  pagoInfo=pago.get()
  escalaInfo=escala.get()
  comentariosInfo=comentarios.get()
  print(nombreInfo,"\t",edadInfo,"\t",emailInfo,"\t",localidadInfo,"\t",saborInfo,"\t",experienciaInfo,"\t",compraInfo,"\t",pagoInfo,"\t",escalaInfo,"\t",comentariosInfo)



 
#  Open and write data to a file
  file = open("user.txt", "a")
  file.write(nombreInfo)
  file.write("\t")
  file.write(edadInfo)
  file.write("\t")
  file.write(emailInfo)
  file.write("\t")
  file.write(localidadInfo)
  file.write("\t")
  file.write(saborInfo)
  file.write("\t")
  file.write(experienciaInfo)
  file.write("\t")
  file.write(compraInfo)
  file.write("\t")
  file.write(pagoInfo)
  file.write("\t")
  file.write(escalaInfo)
  file.write("\t")
  file.write(comentariosInfo)
  file.write("\t\n")
  file.close()
  print(" Nuevas respuestas capturadas:\nNombre: {}\nEdad: {}\nEmali:{}\nLocalidad: {}\nSabor: {}\nExperiencia: {}\n#Productos: {}\nPago:{}\nCalificacion: {}\nComentarios: {} ".format(nombreInfo,edadInfo,emailInfo,localidadInfo,saborInfo,experienciaInfo,compraInfo,pagoInfo,escalaInfo,comentariosInfo))

  file = open("numeros.txt", "a")
  file.write(edadInfo)
  file.write(compraInfo)
  file.write(escalaInfo)

  file.close()
  print(" Nuevas respuestas capturadas:\nEdad: {}\n #Productos:{}\nCalificacion:{} ".format(edadInfo,compraInfo,escalaInfo))
 
#  Delete data from previous event
  nombreEntry.delete(0, END)
  edadEntry.delete(0, END)
  emailEntry.delete(0, END)
  localidadEntry.delete(0, END)
  saborEntry.delete(0, END)
  experienciaEntry.delete(0, END)
  compraEntry.delete(0, END)
  pagoEntry.delete(0, END)
  escalaEntry.delete(0, END)
  comentariosEntry.delete(0, END)


# Create new instance - Class Tk()  
mywindow = Tk()

mywindow.title("Encuesta Limon")

mywindow.config(background = "#213141")
main_title = Label(text = "Limon LGTB", font = ("Cambria", 14), bg = "#56CD63", fg = "black", width = "500", height = "2")
main_title.pack()

# Define Label Fields 
nombre = Label(text = "¿Cual es su nombre?", bg = "#FFEEDD")
nombre.place(x = 22, y = 70)
edad = Label(text = "¿Cual es su edad", bg = "#FFEEDD")
edad.place(x = 22, y = 130)
email = Label(text = "¿Cual es su email", bg = "#FFEEDD")
email.place(x = 22, y = 190)
localidad = Label(text = "¿Estado de residencia?", bg = "#FFEEDD")
localidad.place(x = 22, y = 250)
sabor = Label(text = "¿Cual fue el sabor de su ultimo producto?", bg = "#FFEEDD")
sabor.place(x = 22, y = 310)
experiencia = Label(text = "¿Cual fue su experiencia en su visita?", bg = "#FFEEDD")
experiencia.place(x = 22, y = 370)
compra = Label(text = "¿Cuantos productos compro la ultima vez?", bg = "#FFEEDD")
compra.place(x = 22, y = 430)
pago = Label(text = "¿Cual fue el medio de pago?", bg = "#FFEEDD")
pago.place(x = 22, y = 490)
escala = Label(text = "Del 1-10 ¿Cuanto recomendaria nuestros productos?", bg = "#FFEEDD")
escala.place(x = 22, y = 550)
comentarios = Label(text = "¿Que sugerencias tiene para nosotros?", bg = "#FFEEDD")
comentarios.place(x = 22, y = 610)

 
# Get and store data from users 
nombre = StringVar()
edad = StringVar()
email = StringVar()
localidad = StringVar()
sabor = StringVar()
experiencia = StringVar()
compra = StringVar()
pago = StringVar()
escala = StringVar()
comentarios = StringVar()
 
nombreEntry = Entry(textvariable = nombre, width = "40")
edadEntry = Entry(textvariable = edad, width = "40")
emailEntry = Entry(textvariable = email, width = "40")
localidadEntry = Entry(textvariable = localidad, width = "40") 
saborEntry = Entry(textvariable = sabor, width = "40")

experienciaEntry = Entry(textvariable = experiencia, width = "40")
compraEntry = Entry(textvariable = compra, width = "40")
pagoEntry = Entry(textvariable = pago, width = "40")
escalaEntry = Entry(textvariable = escala, width = "40")
comentariosEntry = Entry(textvariable = comentarios, width = "40")


nombreEntry.place(x = 22, y = 100)
edadEntry.place(x = 22, y = 160)
emailEntry.place(x = 22, y = 220)
localidadEntry.place(x = 22, y = 280)
saborEntry.place(x = 22, y = 340)

experienciaEntry.place(x = 22, y = 400)
compraEntry.place(x = 22, y = 460)
pagoEntry.place(x = 22, y = 520)
escalaEntry.place(x = 22, y = 580)
comentariosEntry.place(x = 22, y = 640)

 
# Submit Button
submit_btn = Button(mywindow,text = "Submit Info", width = "30", height = "2", command = send_data, bg = "#00CD63")
submit_btn.place(x = 22, y = 680)

mywindow.mainloop()


