def floyd_warshall(W):
    n = len(W) 
    D = W.copy() 
    for k in range(n): 
        for i in range(n): 
            for j in range(n):
                D[i][j] = min(D[i][j], D[i][k] + D[k][j]) #a distância mais curta D[i][j] é atualizada para ser a menor entre a distância atual D[i][j] . 
                #A distância D[i][k] + D[k][j] é a distância do vértice i para o vértice j passando pelo vértice intermediário k.
    return D 
# Matriz de adjacência
W =  [          #A,            B,             C,             D
     [           0,            8,  float('inf'),            1],   #A
     [float('inf'),            0,             1, float('inf')],   #B
     [           4, float('inf'),             0, float('inf')],   #C
     [float('inf'),            2,             9,           0] ]  #D

# Chamar a função floyd_warshall
D = floyd_warshall(W)

print(D)