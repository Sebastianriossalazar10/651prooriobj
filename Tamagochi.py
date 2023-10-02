import random
import time

class Tamagotchi:
    def __init__(self, nombre):
        self.nombre = nombre
        self.hambre = 0
        self.felicidad = 50
        self.salud = 100
        self.energia = 100
        self.vivo = True
        self.edad = 0  # Nuevo atributo para la edad

    def alimentar(self):
        if self.vivo:
            self.hambre -= 20
            if self.hambre < 0:
                self.hambre = 0
            self.felicidad += 10
            if self.felicidad > 100:
                self.felicidad = 100
            self.salud += 5
            if self.salud > 100:
                self.salud = 100

    def jugar(self):
        if self.vivo:
            self.hambre += 10
            if self.hambre > 100:
                self.hambre = 100
            self.felicidad += 20
            if self.felicidad > 100:
                self.felicidad = 100
            self.energia -= 10
            if self.energia < 0:
                self.energia = 0
            if self.felicidad == 0 or self.energia == 0 or self.salud == 0:
                self.vivo = False

    def dormir(self):
        if self.vivo:
            self.energia += 30
            if self.energia > 100:
                self.energia = 100
            self.salud += 5
            if self.salud > 100:
                self.salud = 100
            if self.felicidad == 0 or self.energia == 0 or self.salud == 0:
                self.vivo = False

    def envejecer(self):
        if self.vivo:
            self.edad += 1
            self.hambre += random.randint(5, 10)
            if self.hambre > 100:
                self.hambre = 100
            self.felicidad -= random.randint(2, 5)
            if self.felicidad < 0:
                self.felicidad = 0
            self.salud -= random.randint(1, 3)
            if self.salud < 0:
                self.salud = 0
            self.energia -= random.randint(1, 2)
            if self.energia < 0:
                self.energia = 0
            if self.felicidad == 0 or self.energia == 0 or self.salud == 0:
                self.vivo = False

    def revisar_estado(self):
        if self.felicidad == 0 or self.energia == 0 or self.salud == 0 or self.hambre == 100:
            self.vivo = False

    def __str__(self):
        estado = "Vivo" if self.vivo else "Muerto"
        return f"{self.nombre} ({estado}, Edad: {self.edad})\nHambre: {self.hambre}\nFelicidad: {self.felicidad}\nSalud: {self.salud}\nEnergía: {self.energia}"

def main():
    nombre_mascota = input("Ingresa el nombre de tu mascota: ")
    mascota = Tamagotchi(nombre_mascota)
    
    while mascota.vivo:
        mascota.revisar_estado()
        print("\n" + str(mascota))
        if not mascota.vivo:
            print(f"{mascota.nombre} ha fallecido. ¡Game over!")
            break
        accion = input("\n¿Qué quieres hacer? (alimentar/jugar/dormir/salir): ").lower()
        
        if accion == "alimentar":
            mascota.alimentar()
        elif accion == "jugar":
            mascota.jugar()
        elif accion == "dormir":
            mascota.dormir()
        elif accion == "salir":
            print(f"{mascota.nombre} se va a dormir...")
            time.sleep(2)
            print(f"{mascota.nombre} se ha dormido. ¡Hasta luego!")
            break
        else:
            print("Acción no válida. Intenta de nuevo.")

        mascota.envejecer()  # Agregamos el envejecimiento

        time.sleep(1)

if __name__ == "__main__":
    main()
