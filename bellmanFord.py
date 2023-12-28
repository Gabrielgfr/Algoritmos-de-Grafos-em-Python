def bellman_ford(G, w, s):
    
    distancia = {} #menor distância conhecida de cada vértice até a origem
    pai = {}#contém o vértice que precede cada vértice no caminho mais curto da origem até aquele vértice

    def inicializar_fonte_unica(G, origem):
        for vertice in G:
            distancia[vertice] = float('inf')
            pai[vertice] = None
        distancia[origem] = 0

       # Se a distância atual para o vértice v for maior do que a distância para o vértice u mais o peso da aresta de u para v,
        # então atualizamos a distância para v e definimos u como seu predecessor.
    def relaxamento(u, v, w):
        if distancia[v] > distancia[u] + w(u, v):
            distancia[v] = distancia[u] + w(u, v)
            pai[v] = u

    inicializar_fonte_unica(G, s)
    for _ in range(len(G) - 1):
        for u in G:
            for v in G[u]: #v adj a [u]
                relaxamento(u, v, w)
    for u in G:
        for v in G[u]:
            if  distancia[v] > distancia[u] + w(u, v):
                return False
    #return True        
    return distancia, pai, True #caso contrario não mostra o caminho minimo 

#exemplo do livro caso com ciclo negativo:
"""grafo = {
    's': {'t': {'peso': 6}, 'y': {'peso': 7}},
    't': {'x': {'peso': 5}, 'y': {'peso': 8}, 'z': {'peso': -4}},
    'y': {'x': {'peso': -3}, 'z': {'peso': 9}},
    'z': {'x': {'peso': 7}, 's': {'peso': 0}},
    'x': {'t': {'peso': -2}}
}"""

#exemplo: 
grafo = {
    's': {'b': {'peso': 4}, 'd': {'peso': 2}},
    'b': {'c': {'peso': 2}, 'd': {'peso': 3}, 'e': {'peso': 3}},
    'c': { },  # Sem arestas de saída dele.
    'd': {'c': {'peso': 4}, 'b': {'peso': 1}, 'e':{'peso': 5}},
    'e': {'c': {'peso': -5}}
}

origem = 's'

#Lambda criar uma função anônima (uma função sem nome) que representa a função de peso "w"
resultado = bellman_ford(grafo, lambda u, v: grafo[u][v]['peso'], origem)

if resultado is False:
    print("Ciclo de peso negativo detectado.")
else:
    #print("Distâncias do caminho mínimo: \n", resultado) #sem os pais, e distancia no return
    distancias, pais, _ = resultado
    soma_distancias = sum(distancias.values())
    print("Distâncias do caminho mínimo:")
    print(distancias)
    print("Pais:")
    print(pais)
    print("Custo Total:", soma_distancias)
