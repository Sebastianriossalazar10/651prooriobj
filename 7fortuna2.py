from tkinter import *
import random

class sieteAfortunado:
    def __init__(self):
        self.crear_interfaz()
    
    def crear_interfaz(self):
        ventana = Tk()
        ventana.minsize(340, 450)
        ventana.geometry('340x450')
        boton = Button(ventana, text='Jugar', command=self.jugar, font='arial 18 bold')
        boton.pack()
        foto = PhotoImage(file=r'dinero.png')
        self.gano = Label(ventana, image=foto)

        self.campos = [StringVar() for _ in range(3)]
        posicion = 10
        for campo in self.campos:
            label = Label(ventana, textvariable=campo, background='white', foreground='black', font='arial 42 bold')
            label.place(x=posicion, y=100, width=100, height=100)
            posicion += 110
        ventana.mainloop()

    def generar_numero(self):
        return random.randint(0, 9)

    def jugar(self):
        cantidad_sietes = 0  # Variable para llevar un registro de cuántos 7 se han generado.
        for i in range(3):
            valor = self.generar_numero()
            self.campos[i].set(valor)
            if valor == 7:
                cantidad_sietes += 1  # Incrementar el contador si se genera un 7.
        
        if cantidad_sietes >= 3:  # Verificar si hay al menos tres 7.
            self.gano.pack(side=BOTTOM)
        else:
            self.gano.pack_forget()

jugar = sieteAfortunado()