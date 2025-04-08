# Caminho Hamiltoniano em Grafos

## 📌 Descrição do Projeto

Este projeto implementa um algoritmo de backtracking para determinar a existência de um **Caminho Hamiltoniano** em um grafo (direcionado ou não-direcionado). Um caminho Hamiltoniano é um caminho que percorre todos os vértices do grafo exatamente uma vez.

### 🔍 Lógica e Implementação

```python
def hamiltonian_path(graph, path, visited, n):
    if len(path) == n:
        return True  # Caso base: todos os vértices foram visitados

    current = path[-1]
    for neighbor in graph[current]:
        if not visited[neighbor]:
            visited[neighbor] = True      # Marca o vizinho como visitado
            path.append(neighbor)         # Adiciona ao caminho
            if hamiltonian_path(graph, path, visited, n):
                return True               # Solução encontrada
            path.pop()                    # Backtrack
            visited[neighbor] = False     # Desmarca

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
```

## ⚙️ Como Executar o Projeto

#### 1. Instale o Python (3.x).
#### 2. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/caminho-hamiltoniano.git
   cd caminho-hamiltoniano
   ```
#### 3. Rode o script principal:
   ```bash
   python main.py
   ```

> **Nota:** O grafo é definido diretamente no código como lista de adjacência.

---

## 📄 Relatório Técnico

### 🧐 Classes de Complexidade

- **Classe NP-Difícil**:
  - O problema do Caminho Hamiltoniano está na classe **NP-Difícil**.
  - Ele pertence à **classe NP** pois uma solução (um caminho hamiltoniano) pode ser verificada em tempo polinomial.
  - É **NP-Difícil** pois é tão difícil quanto qualquer outro problema em NP e foi provado como tal por redução ao **Problema do Caixeiro Viajante (TSP)**.
  - TSP, na versão decisória (existe um caminho com custo ≤ k?), também é NP-Completo, e generaliza o caminho Hamiltoniano.

### ⏱️ Complexidade Assintótica de Tempo

- O algoritmo tem complexidade **O(n!)** no pior caso.
- Para cada vértice inicial, exploramos todas as permutações possíveis dos outros vértices.
- Método utilizado: **contagem de permutações** e **análise combinatória**:
  - Visitamos `n` vértices → `n!` caminhos possíveis.
  - Cada chamada recursiva analisa os vizinhos → até `n` chamadas por nível.

### 📊 Aplicação do Teorema Mestre

- O Teorema Mestre **não se aplica diretamente** aqui, pois o algoritmo não segue uma **recorrência do tipo T(n) = aT(n/b) + f(n)**.
- O algoritmo de backtracking depende da permutação de vértices, o que resulta numa estrutura recursiva diferente (não divide o problema em subproblemas menores do mesmo tamanho).

### 🔎 Análise de Casos

| Caso        | Descrição                                                  | Complexidade           |
| ----------- | ---------------------------------------------------------- | ---------------------- |
| Melhor caso | Grafo completo onde o primeiro caminho testado já é válido | O(n)                   |
| Caso médio  | Depende do número e ordem das arestas                      | O(k × n!), onde k < n! |
| Pior caso   | Grafo desconexo ou sem caminho válido                      | O(n!)                  |

- A diferença entre os casos impacta diretamente o tempo de execução:
  - No melhor caso, encontramos solução rapidamente e interrompemos.
  - No pior caso, todas as possibilidades são exploradas sem sucesso.
  - Em grafos grandes, a execução se torna inviável sem heurísticas.

---

## 📚 Referências

- Aula: `AULA 02_Introdução à teoria da complexidade.pdf`
- Livro: Cormen, T. H. et al. “Algoritmos: Teoria e Prática”
- [Fundamentos de Projeto e Análise de Algoritmos - João Paulo Aramuni](https://github.com/joaopauloaramuni/fundamentos-de-projeto-e-analise-de-algoritmos/tree/main/PDF)

asd
