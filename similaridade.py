def construir_matriz_compras(lista_compras, n_clientes, m_produtos):    
    matriz_A = [[0]* m_produtos for _ in range(n_clientes)]  # Criamos uma matriz de zeros com n_clientes linhas e m_produtos colunas

    for i in range(n_clientes):
        for j in lista_compras[i]:
            matriz_A[i][j] = 1  # Marcamos com 1 onde o cliente i comprou o produto j

    return matriz_A



def construir_transposta(matriz_A, n_linhas, m_colunas):

    matriz_T= [[0]* n_linhas for _ in range(m_colunas)]  # Criamos uma matriz de zeros com m_colunas linhas e n_linhas colunas

    for i in range(n_linhas):
        for j in range(m_colunas):
            matriz_T[j][i] = matriz_A[i][j] # A transposta é obtida invertendo as posições de i e j


    return matriz_T


def multiplicar_matrizes(matriz_A, matriz_T, n_clientes, m_produtos):

    matriz_I = [[0]* n_clientes for _ in range(n_clientes)]

    for i in range(n_clientes):
        for j in range(n_clientes):

            soma = 0
            for k in range(m_produtos):
                soma += matriz_A[i][k] * matriz_T[k][j]

            matriz_I[i][j] = soma   


    return matriz_I 


            
def calcular_matriz_similaridade(matriz_I, lista_compras, n_clientes):
    
    matriz_S = [[0.0]* n_clientes for _ in range(n_clientes)]

    for i in range(n_clientes):

        tamanho_Pi = len(lista_compras[i])  # Número de produtos comprados pelo cliente i

        for j in range(n_clientes):

            if tamanho_Pi == 0:
                # Proteção: se o cliente 'i' não comprou nada, a distância é máxima (1.0)
                matriz_S[i][j] = 1.0
            else:
                #Pegamos a interseção (I_ij) que acabamos de calcular na matriz I
                intersecao = matriz_I[i][j]
