import heapq


class GPS:

    def __init__(self):
        self.grafo = {}

    def agregar_ciudad(self, ciudad):

        if ciudad not in self.grafo:
            self.grafo[ciudad] = {}

    def agregar_ruta(self, origen, destino, tiempo):

        self.agregar_ciudad(origen)
        self.agregar_ciudad(destino)

        self.grafo[origen][destino] = tiempo

    def mostrar_ciudades(self):

        print("\nCiudades:")

        for ciudad in self.grafo:
            print(ciudad)

    def mostrar_rutas(self):

        print("\nRutas:")

        for origen in self.grafo:
            for destino, tiempo in self.grafo[origen].items():
                print(f"{origen} -> {destino} ({tiempo} min)")

    def ruta_mas_rapida(self, inicio, destino):

        if inicio not in self.grafo or destino not in self.grafo:
            return None, None

        distancias = {
            nodo: float("inf")
            for nodo in self.grafo
        }

        anteriores = {}
        distancias[inicio] = 0

        cola = [(0, inicio)]

        while cola:

            distancia_actual, actual = heapq.heappop(cola)

            for vecino, peso in self.grafo[actual].items():

                nueva = distancia_actual + peso

                if nueva < distancias[vecino]:

                    distancias[vecino] = nueva
                    anteriores[vecino] = actual

                    heapq.heappush(
                        cola,
                        (nueva, vecino)
                    )

        if distancias[destino] == float("inf"):
            return None, None

        ruta = []
        actual = destino

        while actual in anteriores:
            ruta.append(actual)
            actual = anteriores[actual]

        ruta.append(inicio)
        ruta.reverse()

        return ruta, distancias[destino]


gps = GPS()

gps.agregar_ruta("Managua", "Masaya", 30)
gps.agregar_ruta("Masaya", "Granada", 20)
gps.agregar_ruta("Managua", "Leon", 90)
gps.agregar_ruta("Granada", "Leon", 40)

while True:

    print("\n===== SISTEMA GPS =====")
    print("1. Ver ciudades")
    print("2. Ver rutas")
    print("3. Agregar ruta")
    print("4. Ruta más rápida")
    print("0. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        gps.mostrar_ciudades()

    elif opcion == "2":

        gps.mostrar_rutas()

    elif opcion == "3":

        origen = input("Origen: ")
        destino = input("Destino: ")

        try:
            tiempo = int(input("Tiempo en minutos: "))

            gps.agregar_ruta(
                origen,
                destino,
                tiempo
            )

            print("Ruta agregada correctamente.")

        except ValueError:
            print("Debe ingresar un número válido.")

    elif opcion == "4":

        origen = input("Ciudad origen: ")
        destino = input("Ciudad destino: ")

        ruta, tiempo = gps.ruta_mas_rapida(
            origen,
            destino
        )

        if ruta is None:
            print("No existe una ruta disponible.")
        else:
            print("Ruta encontrada:")
            print(" -> ".join(ruta))
            

    elif opcion == "0":

        print("Programa finalizado.")
        break

    else:

        print("Opción no válida.")