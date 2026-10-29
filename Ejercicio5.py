grafo = {
    "A": ["B", "C"],
    "B": ["C"],
    "C": []
}

entrada = {nodo: 0 for nodo in grafo}
salida = {}

for nodo in grafo:

    salida[nodo] = len(grafo[nodo])

    for vecino in grafo[nodo]:
        entrada[vecino] += 1

print("Grado de entrada")
for nodo in entrada:
    print(nodo, ":", entrada[nodo])

print("\nGrado de salida")
for nodo in salida:
    print(nodo, ":", salida[nodo])