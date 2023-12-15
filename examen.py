import random

class Coche():
    def __init__(self, nombre, caballos):
        self.nombre = nombre
        self.caballos = caballos

    def to_string(self):
        return f"{{marca: {self.nombre}, caballos: {self.caballos}}}"

class Carrera():
    def __init__(self, coches):
        self.coches = coches
        self.resultado = []

    def mostrar_parrilla_de_salida(self):
        aux = 1
        for coche in self.coches:
            print(f"El coche {coche.nombre} sale en [{aux}] posición")
            aux += 1

    def empieza_carrera(self):
        print("La carrera ha empezado..")

    def finaliza_carrera(self):
        for coche in self.coches:
            rendimiento_coche = random.randint(1, 4)
            self.resultado.append((coche, rendimiento_coche))

    def muestra_resultado(self):
        self.resultado = sorted(self.resultado, key=lambda x: x[1], reverse=True)
        for coche, rendimiento in self.resultado:
            print(coche.to_string())

if __name__ == '__main__':
    c1 = Coche("Mercedes", "120hp")
    c2 = Coche("Ferrari", "200hp")
    c3 = Coche("Mustang", "200hp")
    c4 = Coche("Lamborghini", "250hp")
    coches = [c1, c2, c3, c4]

    c = Carrera(coches)
    c.mostrar_parrilla_de_salida()
    c.empieza_carrera()
    c.finaliza_carrera()
    c.muestra_resultado()
