import heapq

def verificar_pesos(grafo):
    for no, vizinhos in grafo.items():
        for vizinho, peso in vizinhos.items():
            if peso < 0:
                return False
    return True

def dijkstra(grafo, origem):
    distancias = {v: float('inf') for v in grafo}
    distancias[origem] = 0

    prioridade = [(0, origem)]

    while prioridade:
        distancia_atual, v_atual = heapq.heappop(prioridade)

        if distancia_atual != distancias[v_atual]:
            continue

        for vizinho, peso in grafo[v_atual].items():
            distancia = distancias[v_atual] + peso

            if distancia < distancias[vizinho]:
                distancias[vizinho] = distancia
                heapq.heappush(prioridade, (distancia, vizinho))

    return distancias

grafo = {
  'A': {'B': 1, 'C': 2, 'D': 3},
  'B': {'A': 4, 'C': 5, 'E': 6},
  'C': {'A': 7, 'B': 8, 'D': 9},
  'D': {'A': 10, 'C': 11, 'E': 12},
  'E': {'B': 13, 'D': 14}
}

origem = 'A'

if verificar_pesos(grafo):
    caminho_curto = dijkstra(grafo, origem)
    for destino, distancia in caminho_curto.items():
        print(f"Caminho mais curto de {origem} para {destino}: {distancia}")
else:
    print("O grafo contém pesos de arestas negativas!")
