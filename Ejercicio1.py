class Grafo:

    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, origen, destino):

        if origen not in self.grafo:
            self.grafo[origen] = []

        if destino not in self.grafo:
            self.grafo[destino] = []

        self.grafo[origen].append(destino)

    def dfs_iterativo(self, inicio):

        visitados = set()
        pila = [inicio]
        recorrido = []

        while pila:

            actual = pila.pop()

            if actual not in visitados:

                visitados.add(actual)
                recorrido.append(actual)

                for vecino in reversed(self.grafo[actual]):
                    pila.append(vecino)

        return recorrido


g = Grafo()

g.agregar_arista("A", "B")
g.agregar_arista("A", "C")
g.agregar_arista("B", "D")

print(g.dfs_iterativo("A"))