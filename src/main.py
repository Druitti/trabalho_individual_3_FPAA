def hamiltonian_path(graph, path, visited, n):
    if len(path) == n:
        return True  # Visitou todos os vértices

    current = path[-1]
    for neighbor in graph[current]:
        if not visited[neighbor]:
            visited[neighbor] = True
            path.append(neighbor)
            if hamiltonian_path(graph, path, visited, n):
                return True
            path.pop()
            visited[neighbor] = False

    return False

def has_hamiltonian_path(graph):
    n = len(graph)
    for start in range(n):
        visited = [False] * n
        visited[start] = True
        path = [start]
        if hamiltonian_path(graph, path, visited, n):
            return True, path
    return False, []


# Grafo representado por lista de adjacência
# para testar outros valores siga o exemplo abaixo
# Exemplo de grafo
# 0: [1, 2] = 0 --> 1, 0 --> 2
# 1: [0, 2] = 1 --> 0, 1 --> 2
# 2: [0, 1, 3] = 2 --> 0, 2 --> 1, 2 --> 3
# 3: [2] = 3 --> 2

#para representar o grafo nao direcionado, basta adicionar o nó de destino na lista de adjacência do nó de origem e vice-versa
# Exemplo de grafo não direcionado
# 0: [1, 2] = 0 --> 1, 0 --> 2
# 1: [0, 2] = 1 --> 0, 1 --> 2
# 2: [0, 1, 3] = 2 --> 0, 2 --> 1, 2 --> 3
# 3: [2] = 3 --> 2
# Exemplo de grafo direcionado
# 0: [1, 2] = 0 --> 1, 0 --> 2
# 1: [2] = 1 --> 2
# 2: [3] = 2 --> 3
# 3: [] = 3 --> nenhum nó

graph = {
    0: [1, 2],
    1: [0, 2],
    2: [0, 1, 3],
    3: [2]
}

exists, path = has_hamiltonian_path(graph)
if exists:
    print("Caminho Hamiltoniano encontrado:", path)
else:
    print("Nenhum caminho Hamiltoniano encontrado.")
