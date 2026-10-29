import heapq

def dijkstra(grafo, inicio, destino):

    distancias = {
        nodo: float("inf")
        for nodo in grafo
    }

    anteriores = {}

    distancias[inicio] = 0

    cola = [(0, inicio)]

    while cola:

        distancia_actual, nodo_actual = heapq.heappop(cola)

        for vecino, peso in grafo[nodo_actual].items():

            nueva = distancia_actual + peso

            if nueva < distancias[vecino]:

                distancias[vecino] = nueva

                anteriores[vecino] = nodo_actual

                heapq.heappush(
                    cola,
                    (nueva, vecino)
                )

    ruta = []
    actual = destino

    while actual in anteriores:
        ruta.append(actual)
        actual = anteriores[actual]

    ruta.append(inicio)
    ruta.reverse()

    return ruta, distancias[destino]


grafo = {
    "A": {"B": 4, "C": 2},
    "B": {"D": 5},
    "C": {"D": 1},
    "D": {}
}

ruta, distancia = dijkstra(
    grafo,
    "A",
    "D"
)

print("Ruta:", ruta)
print("Distancia:", distancia)