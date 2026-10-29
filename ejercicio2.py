class Grafo:

    def __init__(self):
        self.grafo = {}

    def agregar_arista(self, origen, destino):

        if origen not in self.grafo:
            self.grafo[origen] = []

        if destino not in self.grafo:
            self.grafo[destino] = []

        self.grafo[origen].append(destino)

    def tiene_ciclo(self):

        visitados = set()
        pila_recursion = set()

        def dfs(nodo):

            visitados.add(nodo)
            pila_recursion.add(nodo)

            for vecino in self.grafo[nodo]:

                if vecino not in visitados:
                    if dfs(vecino):
                        return True

                elif vecino in pila_recursion:
                    return True

            pila_recursion.remove(nodo)
            return False

        for nodo in self.grafo:

            if nodo not in visitados:
                if dfs(nodo):
                    return True

        return False


g = Grafo()

g.agregar_arista("A", "B")
g.agregar_arista("B", "C")
g.agregar_arista("C", "A")

print("¿Tiene ciclo?:", g.tiene_ciclo())