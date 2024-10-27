
graf = {
    "A": "F",
    "B": ["C", "E", "H", "I"],
    "C": "B",
    "D": ["G", "H"],
    "E": ["B", "F"],
    "F": ["A", "E"],
    "G": "D",
    "H": ["B", "D"],
    "I": "B"
}

def BFS(graf, vertex1st, vertexlast):
    bfsSciezka = []
    listaRobocza = []
    listaRobocza.append(graf[vertex1st])
    bfsSciezka.append(vertex1st)
    bfsSciezka.append(listaRobocza[0])
    print(bfsSciezka)
    listaRobocza.append(graf[1])

BFS(graf, "H", "A")