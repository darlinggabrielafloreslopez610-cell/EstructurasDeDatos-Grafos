import heapq

red = {
    "RouterA": {
        "RouterB": 10,
        "RouterC": 5
    },

    "RouterB": {
        "RouterD": 7
    },

    "RouterC": {
        "RouterD": 3
    },

    "RouterD": {}
}

def dijkstra(grafo, inicio):

    distancias = {nodo: float("inf") for nodo in grafo}
    distancias[inicio] = 0

    cola = [(0, inicio)]

    while cola:

        distancia_actual, nodo = heapq.heappop(cola)

        for vecino, peso in grafo[nodo].items():

            nueva = distancia_actual + peso

            if nueva < distancias[vecino]:

                distancias[vecino] = nueva

                heapq.heappush(
                    cola,
                    (nueva, vecino)
                )

    return distancias

print(dijkstra(red, "RouterA"))