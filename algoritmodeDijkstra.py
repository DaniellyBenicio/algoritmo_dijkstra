def dijkstra(grafo, origem):
    distancias = {v: float('inf') for v in grafo}  
    distancias[origem] = 0 
    
    verticesvisitados = []  

    while set(verticesvisitados) != set(distancias): 
        vertice_atual = None
        menor_distancia = float('inf')
        for v in grafo: 
            if v not in verticesvisitados and distancias[v] < menor_distancia:
                vertice_atual = v
                menor_distancia = distancias[v]

        verticesvisitados.append(vertice_atual) 

        for vizinho, peso in grafo[vertice_atual].items():
            if distancias[vertice_atual] + peso < distancias[vizinho]:
                distancias[vizinho] = distancias[vertice_atual] + peso

    return distancias

grafo = {
  'A': {'B': 1, 'C': 2, 'D': 3},
  'B': {'A': 4, 'C': 5, 'E': 6},
  'C': {'A': 7, 'B': 8, 'D': 9},
  'D': {'A': 10, 'C': 11, 'E': 12},
  'E': {'B': 13, 'D': 14}
}


origem = 'A'

caminho_curto = dijkstra(grafo, origem)

for destino, distancia in caminho_curto.items():
  print(f"Caminho mais curto de {origem} para {destino}: {distancia}")
