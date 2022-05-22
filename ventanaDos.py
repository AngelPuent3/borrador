#importo tkinter
import tkinter

#inicializamos la variable que usaremos para almacenar los datos de la encuesta


class mediaModaMediana():
#métodos para el formulario
    def obtenerListaArchivo(self):
        global valoresEncuesta
        valoresEncuesta = []
        archivo = open("numeros.txt", "r")
        lineaEncuestaString = archivo.readlines()[0]
        arrayEncuestaString = lineaEncuestaString.split()
        for x in arrayEncuestaString:
            valoresEncuesta.append(int(x))

    def calcularMedia():
        sumatoria = 0
        mediaCalculada = 0
        for i in valoresEncuesta:
            sumatoria = sumatoria + i
        mediaCalculada = sumatoria / len(valoresEncuesta)
        return mediaCalculada

    def inicializador(self):
        #cargamos los valores de la encuesta llamando al método obtenerListaArchivo
        #inicializo la ventana    
        ventana = tkinter.Tk()
        ventana.geometry("400x300")

        #cálculo de media
        calculoMediaTitulo = tkinter.Label(ventana, text = "Cálculo Media")
        #calculoMediaTitulo.pack(side = tkinter.TOP)
        calculoMedia = tkinter.Label(ventana, text = self.calcularMedia(), fg = "blue")
        #calculoMedia.pack(side = tkinter.TOP)
        calculoMediaTitulo.grid(row=0, column=0)
        calculoMedia.grid(row=0, column=1)

        c.mainloop()


if __name__ == '__main__':
    mediaModaMediana.inicializador()




