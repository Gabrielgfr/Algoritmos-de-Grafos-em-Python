import heapq

def dijkstra(G, w, s): 
    #dicionários que armazenam a distância mínima de cada vértice à origem e o predecessor de cada vértice no caminho mínimo. 
    distancia = {}
    pai = {}
    
    def inicializar_fonte_unica(G, origem):
        for vertice in G:
            distancia[vertice] = float('inf')
            pai[vertice] = None
        distancia[origem] = 0

    def relaxamento(u, v, w):
        if distancia[v] > distancia[u] + w:
            distancia[v] = distancia[u] + w
            pai[v] = u
    
    def extrair_minimo(Q, distancia): #Encontra o vértice u em Q que tem a menor distância à origem.
        u = min(Q, key=distancia.get)  # Extrai o vértice com a menor distância. key=distancia.get é usada para especificar que queremos comparar os valores de distancia dos vértices. metodo "get" retorna none se a chave ñ tiver no dicion
        Q.remove(u) #remove o vértice u de Q
        return u

    inicializar_fonte_unica(G, s)

    S = set()  # S é um conjunto vazio
    Q = list(G.keys())  # Q contém todos os vértices do grafo
    
    while Q:
        u = extrair_minimo(Q, distancia)  
        S.add(u)  # Adiciona u ao conjunto S.
        for v, w in G[u]:
            relaxamento(u, v, w)
    
    return distancia, pai  

grafo = {
    's': [('b', 2), ('e', 3)],
    'b': [('c', 3), ('e', 6), ('s', 2), ('e', 4)],
    'c': [('b', 1), ('d', 5), ('e', 3)],
    'd': [('c', 5), ('e', 3)],
    'e': [('s', 3), ('d', 3)]  
}

origem = 's'  
#Lambda criar uma função anônima (uma função sem nome) que representa a função de peso w 
resultado = dijkstra(grafo, lambda u, v: v, origem)

distancias, pais = resultado
soma_distancias = sum(distancias.values())
print("Distâncias do caminho mínimo:")
print(distancias)
print("Pais:")
print(pais)
print("Custo Total:", soma_distancias)
